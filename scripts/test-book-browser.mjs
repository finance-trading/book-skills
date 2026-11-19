// Run from repo root: node scripts/test-book-browser.mjs
import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import vm from 'node:vm';
import assert from 'node:assert/strict';

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const site = join(root, 'website');
const html = readFileSync(join(site, 'book-browser.html'), 'utf8');
const script = html.match(/<script>([\s\S]*?)<\/script>/)?.[1];
assert.ok(script, 'inline page script exists');

const data = JSON.parse(readFileSync(join(site, 'books-index.json'), 'utf8'));
for (const [bookName, book] of Object.entries(data)) {
  const coverPath = join(site, 'covers', `${bookName}.svg`);
  assert.ok(existsSync(coverPath), `${bookName} has a local cover`);
  assert.match(readFileSync(coverPath, 'utf8'), /<svg\b[\s\S]*<\/svg>/, `${bookName} cover is valid SVG`);
  assert.ok(book.chapters.length > 0, `${bookName} has chapters`);
  for (const chapter of book.chapters) {
    const path = join(root, 'books', bookName, chapter.path);
    assert.ok(existsSync(path), `${bookName}/${chapter.path} exists`);
    const source = readFileSync(path, 'utf8');
    assert.equal(chapter.title, source.match(/^#\s+(.+)$/m)?.[1], `${chapter.path} title matches H1`);
  }
  // refs must list exactly the top-level md files that exist on disk (except SKILL.md)
  const refFiles = readdirSync(join(root, 'books', bookName))
    .filter(name => name.endsWith('.md') && name !== 'SKILL.md')
    .sort();
  const listedRefs = (book.refs ?? []).map(ref => ref.path).sort();
  assert.deepEqual(listedRefs, refFiles, `${bookName} refs match disk`);
}

const elements = {};
function element() {
  return {
    innerHTML: '', textContent: '', value: '', style: {},
    classList: { add() {}, remove() {}, toggle() {}, contains: () => false },
    addEventListener() {}, scrollIntoView() {}, querySelectorAll: () => [], click() {},
  };
}
const document = {
  getElementById: (id) => (elements[id] ??= element()),
  querySelector: () => null,
  querySelectorAll: () => [],
  createElement: () => element(),
};
const fetchLog = [];
const fetch = async (url) => {
  fetchLog.push(url);
  const path = join(site, url.replace(/^\//, ''));
  const content = existsSync(path) ? readFileSync(path, 'utf8') : '';
  return { ok: !!content, text: async () => content, json: async () => JSON.parse(content) };
};
const ctx = vm.createContext({ document, window: { location: { href: '' }, scrollTo() {}, addEventListener() {} }, fetch, console });
vm.runInContext(script, ctx);

await vm.runInContext('loadBookIndex()', ctx);
vm.runInContext('renderBooks()', ctx);
assert.match(elements.booksGrid.innerHTML, /onclick="openReader\('fisher-growth-stocks'\)"/);
assert.match(elements.booksGrid.innerHTML, /15章/);
assert.doesNotMatch(elements.booksGrid.innerHTML, /📖/, 'chapter badge no longer uses an emoji');
assert.match(html, /\.book-stats\s+\.count\s*\{[\s\S]*linear-gradient/, 'chapter badge uses a cover-style gradient badge');
assert.match(html, /\.book-image\s*\{[\s\S]*?flex:\s*0 0 140px[\s\S]*?height:\s*150px/, 'cover area is compact 140x150');
assert.match(html, /@media \(max-width: 600px\)[\s\S]*?flex:\s*0 0 96px[\s\S]*?height:\s*110px/, 'mobile cover area stays compact');
assert.match(html, /grid-template-columns:\s*repeat\(auto-fill, minmax\(300px, 1fr\)\)/, 'book grid stays compact');
for (const slug of Object.keys(data)) {
  assert.match(elements.booksGrid.innerHTML, new RegExp(`covers/${slug}\\.svg`), `${slug} card renders its cover`);
}
assert.doesNotMatch(elements.booksGrid.innerHTML, /chapter\.html/);
assert.match(html, /onclick="clearSearch\(\)"/);
assert.match(script, /function clearSearch\(\)[\s\S]*searchInput\.value\s*=\s*['"]['"]/);
assert.match(script, /fetch\('books-index\.json',\s*\{\s*cache:\s*'no-store'\s*\}/, 'shelf fetches the latest index');
console.log('Book browser regression tests passed.');
