# Enhancement Material Cost Expectation Calculation

## Overview
Calculate the expected material cost to successfully reach each enhancement level from level 0.

## State Machine Model

Let `C[n]` = expected cost to reach level n from level 0

## Failure Outcomes

On failure, two outcomes are possible:
1. **失败时消失概率 P(disappear)**: Nothing happens, item stays at level n-1 (retry needed)
2. **失败时降级概率 P(downgrade)**: Item downgrades by 1 to K levels uniformly (retains value at downgraded level)

Note: 降级等级 = K means the item can downgrade to level n-1, n-2, ..., or n-K with equal probability (1/K each).

## Cost Equation

When attempting to enhance from level n-1 to level n:

**Success (probability = p)**: Reach level n with cost = base_materials[n]

**Failure (probability = 1-p)**: Two sub-cases:
- **Nothing happens (probability = P(disappear))**: Stay at n-1, need to pay C[n] again
- **Downgrade to level n-i (probability = P(downgrade)/K)**: Need to pay from level n-i to n

Expected cost equation:
```
C[n] = C[n-1] + base[n] + (1-p) × [
    P(disappear) × (C[n] - C[n-1]) +
    Σ (P(downgrade)/K) × (C[n] - C[n-i]) for i = 1 to K
]
```

Expanding:
```
C[n] = C[n-1] + base[n] + (1-p) × P(disappear) × (C[n] - C[n-1]) +
       (1-p) × (P(downgrade)/K) × Σ(C[n] - C[n-i])
```

Simplifying:
```
C[n] = C[n-1] + base[n] + (1-p) × P(disappear) × C[n] - (1-p) × P(disappear) × C[n-1] +
       (1-p) × P(downgrade) × C[n] - (1-p) × (P(downgrade)/K) × Σ C[n-i]
```

Collecting C[n] terms:
```
C[n] × [1 - (1-p) × (P(disappear) + P(downgrade))] =
    C[n-1] × [1 - (1-p) × P(disappear)] + base[n] - (1-p) × (P(downgrade)/K) × Σ C[n-i]
```

Since success rate p = 1 - fail rate f:
```
C[n] = (C[n-1] × [1 - f × P(disappear)] + base[n] - f × (P(downgrade)/K) × Σ C[n-i]) /
       [1 - f × (P(disappear) + P(downgrade))]
```

Simplified form:
```
C[n] = (C[n-1] + base[n] + f × (P(downgrade)/K) × Σ C[n-i]) / (1 - f × (P(disappear) + P(downgrade)))
```

Note: The C[n-1] term simplifies because the numerator and denominator cancel out the P(disappear) effect on the previous level cost.

## Example

For level 9 (success: 35%, fail: 65%, disappear: 50%, downgrade: 50%, K=2):

```
C[9] = (C[8] + materials[9] + 0.65 × (0.5/2) × (C[8] + C[7])) / (1 - 0.65 × 1.0)
C[9] = (C[8] + materials[9] + 0.1625 × (C[8] + C[7])) / 0.35
```

This must be solved iteratively from level 1 to 15.
