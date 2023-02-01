import json
import os
import csv
def main():
    j = json.load(open("oreilly.json"))
    tostr = ["authors", "publishers", "topics", "topics_payload"]
    for o in j:
        for f in tostr:
            o[f] = json.dumps(o[f])
    with open(os.path.join("oreilly_mod.json"), 'a+', encoding='utf-8', errors="replace") as outfile:
        json.dump(j, outfile, indent=2)
    field_names = []
    for k in j[0]:
        field_names.append(k)
    with open('oreilly_mod.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(j)

if __name__ == "__main__":
    main()
