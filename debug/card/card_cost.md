# Card Appraisal Cost — Amortized Analysis

## Mechanic

Each appraisal costs fixed materials and produces a random grade:

| Grade | Probability |
|-------|-------------|
| C     | 34%         |
| B     | 40%         |
| A     | 20%         |
| S     | 5%          |
| L     | 1%          |

You keep every card you get — "failed" rolls are not wasted.

## Core Idea

Over a large number of appraisals N, you produce cards in a predictable ratio. The total material cost is shared across all cards. Each card's amortized cost is its fair share of the total.

The key question: how do we assign "weight" to each grade?

## Weight Assignment

We assign weight by rarity — rarer cards should bear more of the cost. A natural weight is the inverse of probability (how many rolls it takes on average to see one):

```
w[grade] = 1 / p[grade]
```

| Grade | p    | w = 1/p |
|-------|------|---------|
| C     | 0.34 | 2.94    |
| B     | 0.40 | 2.50    |
| A     | 0.20 | 5.00    |
| S     | 0.05 | 20.00   |
| L     | 0.01 | 100.00  |

## Amortized Cost Formula

In N rolls, total material spent on material m:

```
total_cost = N * cost[m]
```

Cards produced, weighted:

```
total_weight = sum over all grades: N * p[g] * w[g]
             = sum over all grades: N * p[g] * (1/p[g])
             = N * num_grades
             = 5N
```

Cost per unit weight:

```
cost_per_weight = (N * cost[m]) / (5N) = cost[m] / 5
```

Amortized cost for a card of grade g:

```
amortized_cost(g, m) = w[g] * cost[m] / 5
                     = cost[m] / (5 * p[g])
```

## Simplified

```
amortized_cost(grade, material) = cost[material] / (5 * p[grade])
```

This is exactly 1/5 of the naive geometric cost, because you produce 5 "grade-slots" worth of value per roll (one card always falls into one of 5 grades).

## Amortized Cost Table

Per single appraisal cost unit (cost[m] = 1):

| Grade | p    | Amortized cost per unit |
|-------|------|------------------------|
| C     | 0.34 | 0.588                  |
| B     | 0.40 | 0.500                  |
| A     | 0.20 | 1.000                  |
| S     | 0.05 | 4.000                  |
| L     | 0.01 | 20.000                 |

## Example: 怪物卡片-副官翁扎卡 (lv32)

Per appraisal: 中级阿尔泰=2, 中级玛瑙=2

| Grade | Naive cost | Amortized cost | (per material) |
|-------|------------|----------------|----------------|
| C     | 5.88       | 1.18           | 阿尔泰/玛瑙 each |
| B     | 5.00       | 1.00           | 阿尔泰/玛瑙 each |
| A     | 10.00      | 2.00           | 阿尔泰/玛瑙 each |
| S     | 40.00      | 8.00           | 阿尔泰/玛瑙 each |
| L     | 200.00     | 40.00          | 阿尔泰/玛瑙 each |

## Verification

In 100 rolls (cost = 200 阿尔泰):
- 34 C cards × 1.18 = 40.0
- 40 B cards × 1.00 = 40.0
- 20 A cards × 2.00 = 40.0
- 5 S cards × 8.00 = 40.0
- 1 L card × 40.00 = 40.0
- **Total = 200.0** ✓ (matches 100 × 2)
