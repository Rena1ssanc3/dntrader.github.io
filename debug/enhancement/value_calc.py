import json

with open('config.json') as f:
    config = json.load(f)
    prices = config['prices']
    exchange = config['exchange']
    gold_rate = exchange['gold'] / exchange['龙币']

with open('result.json') as f:
    results = json.load(f)

value_results = []
for r in results:
    total = sum(r[mat] * prices[mat] for mat in prices)
    gold = total * gold_rate
    value_results.append({"level": r["level"], "龙币": round(total, 2), "gold": round(gold, 2)})

with open('value_result.json', 'w', encoding='utf-8') as f:
    json.dump(value_results, f, ensure_ascii=False, indent=2)
