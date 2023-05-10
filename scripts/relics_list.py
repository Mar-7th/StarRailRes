import json
from pathlib import Path

relic_index_list = [Path("./index/cn/relics.json"), Path("./index/en/relics.json")]

icon_path = Path("./icon/relic")

piece_dict = {
    "head":"0",
    "hands":"1",
    "body":"2",
    "feet":"3",
    "planar_sphere":"0",
    "link_rope":"1",
}

def path_to_str(path):
    return str(path).replace("\\", "/")


def search_info(path, file_name:str):
    files = path.glob("*.png")
    files_name = [x.stem for x in files]
    if file_name in files_name:
        return path_to_str(path / (file_name + ".png"))
    return None


def main():
    for relic_index in relic_index_list:
        relic_index_new = dict()
        with open(relic_index, "r", encoding="utf-8") as f:
            index = json.load(f)
        for k, v in index.items():
            item_dict = v
            item_dict["icon"] = search_info(icon_path, k) or ""
            for pk in item_dict["pieces"].keys():
                item_dict["pieces"][pk]["icon"] = search_info(icon_path, f"{k}_{piece_dict[pk]}") or ""
            relic_index_new[k] = item_dict
        with open(relic_index, "w", encoding="utf-8") as f:
            f.write(json.dumps(relic_index_new, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
