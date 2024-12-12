# 新能源电厂调度问题的数学模型求解

这是为研究新能源电厂调度问题而创建的项目。项目维护一个个人的机器学习库`ml-learn`。并对相关的机器学习问题进行研究和解答。

## 项目结构

- `scr/mylib` 此项目创建的临时性的库，可以在虚拟环境下使用.
- `scripts` 项目的脚本文件，与虚拟环境脱钩，用于完成一些一次性的准备过程。 
- `notebook` 项目的`jupyter`笔记本目录，内部运算量较大的用文件夹存储，支持在本地和`kaggle`上运行。
- `output` 项目的输出目录
- `ref` 参考文件
- `docs` 项目文档

## 数据集

项目的数据集会发布在`kaggle`或`huggingface-hub` 平台上。此外可以直接通过项目的`python`库`ml_learn`中的相关函数进行使用。

数据集平台:
- [kaggle](https://www.kaggle.com)
- [huggingface-hub](https://huggingface.co/)

### 1. [新能源电厂数据集](docs/datasets/new-energy-plant.md)

- 上传至`kaggle`和`huggingface-hub`
- 关键词为`sicheng1806/new-energy-plant`
- 直接使用`ml-learn`的调用:
    ```py
    from ml_learn.new_energy_plant import Dataset
    df = DataSet.Solar.load_dataframe() # return a pandas DataFrame
    ```

## 如何安装`ml-learn`

:::{warning}
由于该项目属于个人项目，很不成熟，因此不会正式发布在`pypi`上，个人用于在`kaggle`上快速部署工具,请不要轻易安装在**系统的python环境**上，尽管其不会修改任何系统文件。
:::

### wheel

- `.whl`文件位于[Release](https://github.com/sicheng1806/ml-sicheng/release)页面.
- 通过`pip`安装:
```sh
pip install /path-or-url/to/wheel/file
```

:::{note}
该来源的发布较为及时，同步于标签号。
:::

### TestPypi

```sh
pip install -i https://test.pypi.org/simple/ ml-sicheng
```

:::{note}
该来源的发布同步于版本号。
:::

### Kaggle Dataset

搜索`sicheng1806/ml-learn`以加入Kaggle输入。

:::{note}
该数据库直接链接至github的release页面.
:::

## 项目开发

### 开发工具

项目并无严格的依赖，因为本身是由虚拟环境进行管理的，但是一些功能需要具有本地工具来进行管理:
- 虚拟环境管理工具: [uv](https://github.com/astral-sh/uv)
- 自动化管理工具: [nox](https://github.com/wntrblm/nox)
- kaggle交互工具: [kaggle-cli](https://www.kaggle.com/docs/api)

### 虚拟环境管理

1. 初次clone项目后请使用`uv sync` 来安装python虚拟环境.
2. 同步虚拟环境后在`notebook/*`中使用此虚拟环境运行即可,一般为于`.venv/bin/python`.

### 自动化工具

- `nox -s lint` 代码格式检查
- `nox -s clean` 输出文件清理
- `kaggle kernels push -k notebook/<path-to-kaggle-kernel>` 将项目推送到kaggle并运行，需要密钥。
- `kaggle kernels output <kernel-handle> -p output/` 将kaggle kernel 运行结果下载到本地。 
