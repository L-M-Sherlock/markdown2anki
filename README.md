# markdown2anki

 将md笔记转换成可以导入Anki的格式

# 项目结构

```
├── Basic
│	├── 近世代数note.md # 转 Basic 的笔记格式样例
│	└── anki_basic.txt # 可导入 Anki 的 txt
├── Cloze
│	├── 计算机组成原理Notenote.md # 转 Cloze 的笔记格式样例
│	└── anki_cloze.txt # 可导入 Anki 的 txt
├── note2basic.py # note 转 basic 卡片
├── note2cloze.py # note 转 cloze 卡片
├── utils.py # 封装一下意思意思
└── 模板.apkg # 配套笔记的模板
```

# 使用方法

模仿笔记样例格式写自己的笔记，将md文件放入对应的文件夹（Baisc/Cloze），然后改写 note2basic.py/note2cloze.py 中的路径，最后运行对应脚本即可得到可导入Anki的txt文件。

建议配合本项目提供的模板一同使用。

# 鸣谢

本项目由知乎专栏《[AnkiX高考](https://zhuanlan.zhihu.com/ankigaokao)》赞助提供。