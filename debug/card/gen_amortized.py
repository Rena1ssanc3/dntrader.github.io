import json
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
probs = {"C": 0.34, "B": 0.40, "A": 0.20, "S": 0.05, "L": 0.01}

for lv in ["lv32", "lv40", "lv50", "lv60"]:
    with open(os.path.join(dir_path, f"{lv}.json"), encoding="utf-8") as f:
        cards = json.load(f)
    with open(os.path.join(dir_path, f"{lv}_cost.json"), encoding="utf-8") as f:
        costs = {c["name"]: c["cost"] for c in json.load(f)}

    for card in cards:
        cost = costs.get(card["name"], {})
        p = probs[card["grade"]]
        card["amortized_cost"] = {m: round(v / (5 * p), 2) for m, v in cost.items() if v > 0}

    with open(os.path.join(dir_path, f"{lv}.json"), "w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False, indent=2)
    print(f"{lv}.json updated")
