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

#### 打包EXE

```
pyinstaller index.spec
```

