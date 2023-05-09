import json
from pathlib import Path

character_index_list = [Path("./index/cn/characters.json"), Path("./index/en/characters.json")]

icon_path = Path("./icon/character")
preview_path = Path("./image/character_preview")
portrait_path = Path("./image/character_portrait")
character_overview_path_list = [
    Path("./guide/Nwflower/character_overview"),
    Path("./guide/OriginMirror/character_overview"),
]
character_material_path = Path("./guide/Nwflower/character_material")


def path_to_str(path):
    return str(path).replace("\\", "/")


def search_info(path, file_name:str):
    files = path.glob("*.png")
    files_name = [x.stem for x in files]
    if file_name in files_name:
        return path_to_str(path / (file_name + ".png"))
    #
    if file_name.startswith("800") and int(file_name) % 2 == 0 :
        file_name = str(int(file_name)-1)
    if file_name in files_name:
        return path_to_str(path / (file_name + ".png"))
    return None


def main():
    for character_index in character_index_list:
        character_index_new = dict()
        with open(character_index, "r", encoding="utf-8") as f:
            index = json.load(f)
        for k, v in index.items():
            item_dict = v
            item_dict["icon"] = search_info(icon_path, k) or ""
            item_dict["preview"] = search_info(preview_path, k) or ""
            item_dict["portrait"] = search_info(portrait_path, k) or ""
            overview = []
            for character_overview_path in character_overview_path_list:
                overview_item = search_info(character_overview_path, k)
                if overview_item:
                    overview.append(overview_item)
            item_dict["character_overview"] = overview
            item_dict["character_material"] = (
                search_info(character_material_path, k) or ""
            )
            character_index_new[k] = item_dict
        with open(character_index, "w", encoding="utf-8") as f:
            f.write(json.dumps(character_index_new, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
