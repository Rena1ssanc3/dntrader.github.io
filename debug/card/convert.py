import json
import glob
import os

def parse_card_file(filepath):
    cards = []
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            parts = [p for p in parts if p]
            if len(parts) < 4:
                continue
            card = {"name": parts[0], "grade": parts[1], "value": int(parts[2])}
            stats = []
            i = 3
            while i + 1 < len(parts):
                stats.append({"stat": parts[i], "value": int(parts[i + 1])})
                i += 2
            card["stats"] = stats
            cards.append(card)
    return cards

def parse_prob_file(filepath):
    lines = [l.strip() for l in open(filepath, encoding="utf-8") if l.strip()]
    result = {"title": lines[0]}
    probs = {}
    for i in range(3, len(lines) - 1, 2):
        probs[lines[i]] = lines[i + 1]
    result["probabilities"] = probs
    return result

dir_path = os.path.dirname(os.path.abspath(__file__))
for txt_file in glob.glob(os.path.join(dir_path, "*.txt")):
    base = os.path.splitext(txt_file)[0]
    name = os.path.basename(base)
    if name == "prob":
        data = parse_prob_file(txt_file)
    else:
        data = parse_card_file(txt_file)
    out = base + ".json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"{os.path.basename(txt_file)} -> {os.path.basename(out)}")
