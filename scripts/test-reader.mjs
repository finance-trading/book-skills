import { readFileSync } from 'node:fs';
import { strict as assert } from 'node:assert';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
const root = dirname(dirname(fileURLToPath(import.meta.url)));
const site = join(root, 'website');
const shelf = readFileSync(join(site, 'book-browser.html'), 'utf8');
let reader = '';
try { reader = readFileSync(join(site, 'reader.html'), 'utf8'); } catch {}
assert.match(shelf, /reader\.html\?book=/, 'book cards open a separate reader');
assert.match(reader, /function renderMarkdown\(source\)/, 'Markdown renderer is present');
assert.match(reader, /escapeHtml/, 'Markdown output escapes HTML');
assert.match(reader, /chapter-list/, 'reader contains chapter navigation');
assert.match(reader, /contentBody/, 'reader contains chapter content');
console.log('Reader structure checks passed');
