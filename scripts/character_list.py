import json
from pathlib import Path

character_index_list = [Path("./character_cn.json"), Path("./character_en.json")]

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


def search_info(path, name):
    file_name = name.replace(" ", "").replace(":", "").replace("_", "").strip()
    files = path.glob("*.png")
    files_name = [x.stem for x in files]
    #
    if file_name in files_name:
        return path_to_str(path / (file_name + ".png"))
    #
    if file_name in [
        "TrailblazerBoyPhysical",
        "TrailblazerGirlPhysical",
        "TrailblazerBoyFire",
        "TrailblazerGirlFire",
    ]:
        file_name = file_name.replace("Boy", "").replace("Girl", "")
    if file_name in files_name:
        return path_to_str(path / (file_name + ".png"))
    #
    if file_name in ["TrailblazerPhysical", "TrailblazerFire"]:
        file_name = file_name.replace("Physical", "").replace("Fire", "")
    if file_name in files_name:
        return path_to_str(path / (file_name + ".png"))
    #
    if file_name == "Trailblazer":
        file_name = "TrailblazerPhysical"
    if file_name in files_name:
        return path_to_str(path / (file_name + ".png"))
    #
    if file_name in ["TrailblazerPhysical", "TrailblazerFire"]:
        file_name = file_name.replace("Trailblazer", "TrailblazerGirl")
    if file_name in files_name:
        return path_to_str(path / (file_name + ".png"))
    #
    return None


def main():
    for character_index in character_index_list:
        character_index_new = dict()
        with open(character_index, "r", encoding="utf-8") as f:
            index = json.load(f)
        for k, v in index.items():
            item_dict = dict()
            item_dict["name"] = v["name"]
            item_dict["rarity"] = v["rarity"]
            item_dict["path"] = v["path"]
            item_dict["element"] = v["element"]
            item_dict["icon"] = search_info(icon_path, item_dict["name"]) or ""
            item_dict["preview"] = search_info(preview_path, item_dict["name"]) or ""
            item_dict["portrait"] = search_info(portrait_path, item_dict["name"]) or ""
            overview = []
            for character_overview_path in character_overview_path_list:
                overview_item = search_info(character_overview_path, item_dict["name"])
                if overview_item:
                    overview.append(overview_item)
            item_dict["character_overview"] = overview
            item_dict["character_material"] = (
                search_info(character_material_path, item_dict["name"]) or ""
            )
            character_index_new[k] = item_dict
        character_index_new = dict(
            sorted(character_index_new.items(), key=lambda x: x[1]["name"])
        )
        with open(character_index, "w", encoding="utf-8") as f:
            f.write(json.dumps(character_index_new, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
