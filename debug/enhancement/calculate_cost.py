import json

with open('prob.json') as f:
    prob_data = json.load(f)['data']

with open('materials.json') as f:
    materials_data = json.load(f)['enhancement_materials']

def parse_rate(rate_str):
    if rate_str == '-':
        return 0
    return float(rate_str.rstrip('%')) / 100

def get_materials(level):
    return next(m for m in materials_data if m['level'] == level)

def get_prob(level):
    return next(p for p in prob_data if p['强化等级'] == level)

# Calculate expected cost for each level
C = [{mat: 0 for mat in ['生命精髓', '高级钻石', '强化保护药']} for _ in range(16)]

for level in range(1, 16):
    prob = get_prob(level)
    mat = get_materials(level)

    success = parse_rate(prob['成功率'])
    fail = parse_rate(prob['失败率'])
    disappear = parse_rate(prob['失败时消失概率'])
    downgrade_prob = parse_rate(prob['失败时降级概率'])
    downgrade_to_level = int(prob['降级等级']) if prob['降级等级'] != '-' else 0

    for material in ['生命精髓', '高级钻石', '强化保护药']:
        base_cost = mat.get(material, 0)

        if success == 1:
            C[level][material] = C[level - 1][material] + base_cost
        else:
            # Calculate sum of costs at all possible downgrade levels
            if downgrade_to_level > 0 and downgrade_prob > 0:
                sum_downgrade_costs = sum(C[level - 1 - i][material] for i in range(1, downgrade_to_level + 1))
                downgrade_term = fail * (downgrade_prob / downgrade_to_level) * sum_downgrade_costs
            else:
                downgrade_term = 0

            # C[n] = (C[n-1]×[1-f×P(disappear)] + base - f×(P(downgrade)/K)×Σ C[n-i]) / (1 - f×(P(disappear)+P(downgrade)))
            denominator = 1 - fail * (disappear + downgrade_prob)
            numerator = C[level - 1][material] * (1 - fail * disappear) + base_cost - downgrade_term
            C[level][material] = numerator / denominator

# Calculate results
results = []

for level in range(1, 16):
    results.append({
        "level": level,
        "生命精髓": round(C[level]['生命精髓'], 2),
        "高级钻石": round(C[level]['高级钻石'], 2),
        "强化保护药": round(C[level]['强化保护药'], 2)
    })

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
