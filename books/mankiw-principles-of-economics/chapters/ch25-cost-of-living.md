# Chapter 25: Measuring the Cost of Living

## Core Idea
Price indexes make dollar amounts from different dates comparable. CPI tracks the cost of a representative consumer basket, but substitution, new goods, and quality changes limit its precision.

## Frameworks Introduced
- **CPI construction**: Fix a basket, collect each good's current price, calculate basket cost in each period, set a base-year basket cost to 100, and compute the percentage change for inflation.
- **Index-selection test**: CPI covers a fixed household-purchase basket including imports; the GDP deflator covers domestically produced final goods and services with a changing composition. Choose based on the purchasing power question.
- **Inflation adjustment**: Translate old dollars into current purchasing power by multiplying by `current CPI / old CPI`. Distinguish nominal from real interest using the Fisher approximation: real rate ≈ nominal rate − inflation.

## Key Concepts
- **Consumer price index**: Cost of fixed consumer basket relative to base-period cost.
- **Inflation rate**: Percentage change in a price index.
- **Substitution bias**: Fixed basket misses consumers' switching toward relatively cheaper goods.
- **Nominal interest rate**: Rate stated in dollars not adjusted for purchasing power.
- **Real interest rate**: Interest rate adjusted for inflation.

## Mental Models
- An index has a population, basket, and base year; check all three before comparing it with a personal bill.
- Nominal growth in wages or investment returns is not the same as a gain in purchasing power.

## Anti-patterns
- **Using one index for every comparison**: CPI and GDP deflator answer different questions.
- **Treating reported CPI as exact cost-of-living change**: It can miss substitution, quality, and new products.

## Worked Example
Mankiw asks how Babe Ruth's $80,000 salary compares with a present-day salary. A direct dollar comparison is misleading. Multiply the old salary by the ratio of present CPI to the CPI in Ruth's year to express it in current purchasing-power dollars. Then compare with current compensation, remembering the CPI is an average basket and may not match a particular person's spending.

## Key Takeaways
1. State the index and base period when converting historic values.
2. Separate nominal price or income changes from real purchasing power.
3. Account for CPI measurement biases when precision matters.

## Connects To
- **Ch 24**: GDP deflator is a different aggregate price index.
- **Ch 31**: Inflation theory explains persistent price-level growth.
