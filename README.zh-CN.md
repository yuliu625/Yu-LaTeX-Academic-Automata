# LaTeX Academic Automata

这个仓库是我学术写作系统中的自动化部分的构成。

这个仓库中的方法为非 latex 代码实现相关，所有方法均采用其他编程语言或工具，以此来实现自动化 latex 代码生成、latex 项目运维和集成、latex 项目管理。

自动化的方法可以减少与 latex 这门古老语言的直接交互，降低各种不必要的时间开销，从而将注意力更多集中在写作内容中。


## 我的学术写作工作流


### 通用化写作模板

我定义的通用学术协作项目框架。

> [Yu-LaTeX-Academic-Template](https://github.com/yuliu625/Yu-LaTeX-Academic-Template)

在开始写作前，使用该仓库作为基础的框架，之后根据具体的投稿模板进行写作。该模板根据 bridge pattern 进行设计，有效隔离了 写作原始资产、写作内容、投稿模板，可敏捷在多个投稿或报告之间进行迁移。

当前仓库中，managers/preprocessors 下有自动化生成 latex 项目框架的脚本。


### 个人包

我通用的个人 latex package 。

> [Yu-Lua-TeX-Utility](https://github.com/yuliu625/Yu-LaTeX-Lua-TeX-Utility)

在每个 latex project 中，同步基础包。包主要实现 补丁、常用包导入、yu 系列 macro。可统一在各个 latex project 中的控制和代码风格，有效减少 latex 调试和各种重复工作。


### 自动化持续集成

> [Yu-LaTeX-Academic-Automata](https://github.com/yuliu625/Yu-LaTeX-LaTeX-Academic-Automata)



## 🛠️ 模块体系

项目根据功能领域划分为 3 个模块:


### 项目控制

负责 LaTeX 整个生命周期的项目管理与文件流控制。



### 内容生成

负责将外部数据或内容转化为 LaTeX code 。



### 运维集成工具

负责将 LaTeX 写作环境与外部协作、版本控制系统无缝对接。



## 🔗 相关项目

本项目作为学术写作生态的一部分，需配合以下仓库使用以获得完整体验:

