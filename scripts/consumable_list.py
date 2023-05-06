import json
from pathlib import Path

consumable_index_list = [
    Path("./consumable_cn.json"),
    Path("./consumable_en.json")
]

icon_path = Path("./icon/consumable")

def path_to_str(path):
    return str(path).replace("\\", "/")

def search_info(path, name):
    file_name = name.replace(" ", "").replace(":", "").replace("_", "").strip()
    files = path.glob("*.png")
    files_name = [x.stem for x in files]
    if file_name in files_name:
        return path_to_str(path / (file_name + ".png"))
    return None

def main():
    for consumable_index in consumable_index_list:
        consumable_index_new = dict()
        with open(consumable_index, "r", encoding="utf-8") as f:
            index = json.load(f)
        for k,v in index.items():
            item_dict = dict()
            item_dict["name"] = v["name"]
            item_dict["rarity"] = v["rarity"]
            item_dict["icon"] = search_info(icon_path, item_dict["name"]) or ""
            consumable_index_new[k] = item_dict
        with open(consumable_index, "w", encoding="utf-8") as f:
            f.write(json.dumps(consumable_index_new, indent=4,ensure_ascii=False))

if __name__ == "__main__":
    main()
