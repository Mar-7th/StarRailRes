# StarRailRes

Honkai: Star Rail game resources, can be used as a bot resource library.

崩坏：星穹铁道游戏资源，可作为相关机器人资源库使用。

## Overview

The file structure of this project is as follows:

这个项目的文件结构如下：

```text
StarRailRes
  ├─ guide                  # Guide images
  ├─ icon                   # Icons for drawing
  ├─ image                  # Previews and portraits, etc.
  ├─ character_cn.json      # 角色资源索引
  ├─ character_en.json      # Character resouces index
  ├─ consumable_cn.json     # 消耗品资源索引
  ├─ consumable_en.json     # Consumable resouces index
  ├─ light_cone_cn.json     # 光锥资源索引
  └─ light_cone_cn.json     # Light cone resouces index
```

使用中文名称搜索时，通过 `character_cn.json` 等查找对应角色等的资源信息，所有相对路径均相对本工程的根目录。别名映射正在完善中，目前只能通过完整的原始名称（去除全部特殊符号）匹配。
