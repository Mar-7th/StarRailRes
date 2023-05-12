# StarRailRes

Honkai: Star Rail game resources, can be used as a bot resource library.

崩坏：星穹铁道游戏资源，可作为相关机器人资源库使用。

## Overview

New index files structure:

```text
StarRailRes
└─ index
   └─ [language]
      ├─ paths.json                     # path / 命途
      ├─ elements.json                  # element / 元素
      ├─ characters.json                # character basic info / 角色基本信息
      ├─ character_ranks.json           # character rank / 角色星魂
      ├─ character_skills.json          # character skill / 角色技能
      ├─ character_skill_trees.json     # character skill tree / 角色行迹
      ├─ light_cones.json               # light cone / 光锥基本信息
      ├─ light_cone_ranks.json          # light cone rank / 光锥叠影
      ├─ light_cone_promotions.json     # light cone promotion / 光锥晋阶与等级
      ├─ relics.json                    # relic basic info / 遗器基本信息
      ├─ relic_sets.json                # relic set / 遗器套装信息
      ├─ relic_main_affixs.json         # relic main affix / 遗器主词条组
      └─ relic_sub_affixs.json          # relic sub affix / 遗器副词条组
```

The file structure of this project is as follows:

这个项目的文件结构如下：

```text
StarRailRes
├─ guide                    # Guide images
├─ icon                     # Icons for drawing
├─ image                    # Previews and portraits, etc.
|─ index                    # Index files
|  ├─ cn                    # 中文索引
|  |  ├─ characters.json    # 角色数据与资源索引
|  |  ├─ light_cones.json   # 光锥数据与资源索引
|  |  ├─ relics.json        # 遗器数据与资源索引
|  |  ├─ elements.json      # 元素数据与资源索引
|  |  ├─ paths.json         # 命途数据与资源索引
|  |  └─ nickname.json      # 角色与光锥名称词典
|  └─ en                    # English index
|     ├─ characters.json    # Characters data & resource index
|     ├─ light_cones.json   # Light cones data & resource index
|     ├─ relics.json        # Relics data & resource index
|     ├─ elements.json      # Element data & resource index
|     └─ paths.json         # Path data & resource index
└─ scripts                  # Auto update index scripts
    ├─ characters_list.py   # Characters index update script 
    ├─ light_cones_list.py  # Light cones index update script
    └─ relics_list.py       # Relics index update script
```

使用 `id` 搜索时，可直接通过 `characters.json` 等查找对应角色等的资源信息，所有相对路径均相对本工程的根目录。如需使用别名映射，可以在 `nickname.json` 的 `characters` 等中获取别名列表并构造反向词典查询。`nickname` 中所有名称不包含特殊符号。

When searching by id, use `characters.json` to find the resources of the corresponding character, etc. All relative paths are relative to the root directory of this project.
