# StarRailRes

Honkai: Star Rail game resources, can be used as a bot resource library.

崩坏：星穹铁道游戏资源，可作为相关机器人资源库使用。

## Overview

The file structure of this project is as follows:

这个项目的文件结构如下：

```text
StarRailRes
  ├─ guide                     # Guide images
  ├─ icon                      # Icons for drawing
  ├─ image                     # Previews and portraits, etc.
  ├─ scripts                   # Auto update index scripts
  |   ├─ character_list.py     # Character index update script 
  |   └─ light_cone_list.py    # Light cone index update script
  └─ index                     # Index files
      ├─ cn                    # 中文索引
      |  ├─ characters.json    # 角色数据与资源索引
      |  ├─ light_cones.json   # 光锥数据与资源索引
      |  ├─ nickname.json      # 角色与光锥名称词典
      |  ├─ elements.json      # 元素数据与资源索引
      |  └─ paths.json         # 命途数据与资源索引
      └─ en                    # English index
         ├─ characters.json    # Character data & resource index
         ├─ light_cones.json   # Light cone data & resource index
         ├─ elements.json      # Element data & resource index
         └─ paths.json         # Path data & resource index
```

使用 `id` 搜索时，可直接通过 `character.json` 等查找对应角色等的资源信息，所有相对路径均相对本工程的根目录。如需使用别名映射，可以在 `nickname.json` 的 `characters` 等中获取别名列表并构造反向词典查询。`nickname` 中所有名称不包含特殊符号。

When searching by id, use `character.json` to find the resources of the corresponding character, etc. All relative paths are relative to the root directory of this project.
