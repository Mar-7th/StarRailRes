import json
from pathlib import Path

light_cone_index_list = [Path("./index/cn/light_cones.json"), Path("./index/en/light_cones.json")]

icon_path = Path("./icon/light_cone")
preview_path = Path("./image/light_cone_preview")
portrait_path = Path("./image/light_cone_portrait")
light_cone_overview_path_list = [
    Path("./guide/Nwflower/light_cone"),
    Path("./guide/OriginMirror/light_cone"),
]


def path_to_str(path):
    return str(path).replace("\\", "/")


def search_info(path, file_name:str):
    files = path.glob("*.png")
    files_name = [x.stem for x in files]
    if file_name in files_name:
        return path_to_str(path / (file_name + ".png"))
    return None


def main():
    for light_cone_index in light_cone_index_list:
        light_cone_index_new = dict()
        with open(light_cone_index, "r", encoding="utf-8") as f:
            index = json.load(f)
        for k, v in index.items():
            item_dict = v
            item_dict["icon"] = search_info(icon_path, k) or ""
            overview = []
            for light_cone_overview_path in light_cone_overview_path_list:
                overview_item = search_info(light_cone_overview_path, k)
                if overview_item:
                    overview.append(overview_item)
            item_dict["light_cone_overview"] = overview
            light_cone_index_new[k] = item_dict
        with open(light_cone_index, "w", encoding="utf-8") as f:
            f.write(json.dumps(light_cone_index_new, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
