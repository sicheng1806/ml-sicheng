# 新能源电厂调度问题

## 开始之前

### 1. 准备数据集

首先需要从[hf://datasets/sicheng1806/New-energy-power-plant/](https://huggingface.co/datasets/sicheng1806/New-energy-power-plant) 下载数据集至`dataset/data`文件夹下,如下:
```sh
dataset/data
├── S1.csv
├── W1_power.csv
└── W1_velocity.csv
```

也可以从`hugging-face`的镜像网站上下载[hf-mirror](https://hf-mirror.com/)。

### 2. 项目结构

- `scr/mylib` 此项目创建的临时性的库，可以在虚拟环境下使用.
- `scripts` 项目的脚本文件，与虚拟环境脱钩，用于完成一些一次性的准备过程。 
- `notebook` 项目的`jupyter`笔记本目录，内部运算量较大的用文件夹存储，支持在本地和`kaggle`上运行。
- `output` 项目的输出目录
- `ref` 参考文件
- `docs` 项目文档

### 3. 项目工具

项目并无严格的依赖，因为本身是由虚拟环境进行管理的，但是一些功能需要具有本地工具来进行管理:
- 虚拟环境管理工具: [uv](https://github.com/astral-sh/uv)
- 自动化管理工具: [nox](https://github.com/wntrblm/nox)
- kaggle交互工具: [kaggle-cli](https://www.kaggle.com/docs/api)

## 项目开发

### 如何运行

1. 初次clone项目后请使用`uv sync` 来安装python虚拟环境.
2. 同步虚拟环境后在`notebook\*`中使用此虚拟环境运行即可,一般为于`.venv\bin\python`.

### 自动化工具

- `nox -s lint` 代码格式检查
- `nox -s clean` 输出文件清理
- `kaggle kernels push -k notebook\< your-kaggle-kernel-path >` 将项目推送到kaggle并运行，需要密钥。
- `kaggle kernels output sicheng1806/lstm-new-energy-plant -p output/` 将kaggle kernel 运行结果下载到本地。 
