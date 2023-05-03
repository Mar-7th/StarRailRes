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
  ├─ character.json         # Character resouces index
  ├─ consumable.json        # Consumable resouces index
  ├─ light_cone.json        # Light cone resouces index
  ├─ mapping_cn.json        # 中英文名称对照文件
  ├─ mapping_jp.json        # 日本語/英語名対照ファイル
  └─ mapping_kr.json        # 한글/영어 이름 매핑 파일
```

使用中文名称搜索时，通过 `mapping_cn.json` 找到对应的资源索引名称，之后通过索引名称在 `character.json` 等文件中查找对应角色等的资源信息，所有相对路径均相对本工程的根目录。别名映射正在完善中，目前只能通过完整的原始名称匹配。
