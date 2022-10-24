# 档案手册

一个网页项目试验集成部署页面。

## 主页

原主页网页结构混乱，兼容性、扩展性较差，故此原主页入口已暂时关闭 ~~（页面里的关闭缘由是唬人的呵呵）~~ 。目前网站的索引页在[这里](https://geraniol.github.io/index_ex)。

## EX 版本

本项目很多网页都有 EX 版本，在网页后面增加 `index_ex` 即可访问。例如：
<br>`https://geraniol.github.io/` 是原主页（已暂停访问）
<br>`https://geraniol.github.io/index_ex` 是新索引页

## 目录结构

```
Root
|
+-- Data
|   +-- Pages                           --- 子页面
|   |   +-- Project_001_AnimeGirl       --- 互动桌面：插画少女
|   |   +-- Project_002_Star            --- 动态桌面：寂静星球
|   |   |   +-- ex                      --- 动态桌面：迷你星球
|   |   +-- Project_003_Chocolate       --- 互动桌面：巧克力
|   |   +-- Project_004_CodePage        --- 技术：代码框架自适应
|   |   |   +-- ex                      --- 技术：室友监视器
|   |   +-- Project_005_FlowPage        --- 应用：瀑布流作品展示
|   |   |   +-- ex                      --- 应用：气突苏
|   |   +-- Project_006_Switch          --- 技术：开关与音乐
|   |   +-- Project_007_EMuyv           --- 应用：电子木鱼
|   |   |   +-- ex                      --- 应用：全自动木鱼
|   |   +-- Project_008_Portfolio       --- 技术：卡片式作品展示
|   |   +-- Project_009_DevInf          --- 技术：设备开发信息
|   |   +-- Project_010_Daydream        --- 应用：视觉小说
|   |   +-- CUHKSZPASSPORT              --- 大学：通行证（已停用）
|   |   |   +-- ex                      --- 大学：通行证
|   |   +-- CUHKSZSU-Umbrella           --- 大学：学生会雨伞
|   |   +-- Recruitment                 --- 大学：学生会招新需求
|   |   +-- Lagrange                    --- 拉格朗日：档案
|   |   +-- ResearchSimulator           --- 拉格朗日：研究模拟器
|   +-- fonts
|   |   +-- qiantubifengshouxie.ttf     --- 字体（已停用；主页用）
|   +-- images
|       +-- Today's_Chicken
|           +-- logo.png                --- 主页 Logo
+-- index.html                          --- 主页（已停用）
+-- index_ex.html                       --- 索引页
+-- main.css                            --- 样式表（已停用；主页用）
```

## 开发计划

- 没有长期的固定计划。
- 由于文档结构欠佳，可能进行大规模删改，届时大部分原有链接都会失效。
- 继续添加前端应用性网页。
- 完善作品展示页面，添加更多作品。
- 除 HTML 文档本身外，可能还会上传由 Python 编写的 HTML 生成器。

:)
