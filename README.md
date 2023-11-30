# PyQtSS

用 PySide6 写的 ss-rust GUI客户端。

主要功能使用第三方的二进制文件，Python只完成设置操作。
这样设计架构，出于以下几点考虑：
- 性能稳定，功能保持与主版本一致
- 升级方便，替换文件即可完成升级
- 避免重复造轮子

## 组件
- [核心组件](dev_env_conf/bin.version)
- [Python库](dev_env_conf/requirements.txt)