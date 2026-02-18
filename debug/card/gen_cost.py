import json
import os

dir_path = os.path.dirname(os.path.abspath(__file__))

materials = {
    "lv32": ["中级阿尔泰", "中级玛瑙", "中级钻石", "生命精髓"],
    "lv40": ["中级阿尔泰", "中级玛瑙", "中级钻石", "生命精髓"],
    "lv50": ["高级阿尔泰", "高级玛瑙", "高级钻石", "生命精髓"],
    "lv60": ["高级阿尔泰", "高级玛瑙", "高级钻石", "生命精髓"],
}

for lv, mats in materials.items():
    with open(os.path.join(dir_path, f"{lv}.json"), encoding="utf-8") as f:
        cards = json.load(f)
    names = list(dict.fromkeys(c["name"] for c in cards))
    cost_data = [{"name": n, "cost": {m: 0 for m in mats}} for n in names]
    out = os.path.join(dir_path, f"{lv}_cost.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(cost_data, f, ensure_ascii=False, indent=2)
    print(f"{lv}_cost.json generated ({len(names)} cards)")
