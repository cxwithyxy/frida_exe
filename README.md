# frida_exe
Maybe you can use frida without python



## 使用

#### 启动命令

```
index.exe target_program.exe frida_script.js
```

#### 内置命令:

1. load 重新加载js脚本
1. exit 退出



## 构建

建议使用 virtualenv 

#### 安装依赖

```
pip install -r requirements.txt
```

但由于依赖库 file-tools 默认使用 gbk 编码读取文件，因此读取 utf8 文件会报错，要解决这问题，请安装我修改后的 file-tools 。

先卸载旧的 file-tools 

```
pip uninstall file-tools
```

安装我的  file-tools 

```
pip install git+https://github.com/cxwithyxy/file_tools.git
```

#### 打包EXE

```
pyinstaller index.spec
```

