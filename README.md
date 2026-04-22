<div align="center">
  <h1 align="center">IPTV节目列表编辑器</h1>
</div>

<div align="center">一个蝇量级的运行于Openwrt系统中的IPTV列表编辑器和内容服务器</div>
<br>
<p align="center">
  <a href="https://github.com/wangweiwei104/IPTVEditor/releases/latest">
    <img src="https://img.shields.io/github/v/release/wangweiwei104/IPTVEditor" />
  </a>
  <a href="https://github.com/wangweiwei104/IPTVEditor/releases/latest">
    <img src="https://img.shields.io/github/downloads/wangweiwei104/IPTVEditor/total" />
  </a>
  <a href="https://github.com/wangweiwei104/IPTVEditor/fork">
    <img src="https://img.shields.io/github/forks/wangweiwei104/IPTVEditor" />
  </a>
  <a href="https://github.com/wangweiwei104/IPTVEditor/star">
    <img src="https://img.shields.io/github/stars/wangweiwei104/IPTVEditor" />
  </a>
</p>

## 界面
<p align="center">
  <a >
    <img src="home.png" alt="界面展示截图" />    
  </a>
  AI帮我写的界面
  <a >
    <img src="save.png" alt="界面展示截图" />    
  </a>
  挺好看的提示动画
</p>

## 功能

- ✅ TVbox系的空壳电视直播软件，如果你不想用网络提供的直播源，而是使用更稳定的自己提取的，你需要一个直播源的链接，这个项目可以在本地网络、以极低的代价、静态网页的方式实现，直播源地址为 http:/192.168.x.x(替换成你的路由器地址)/iptv/iptv.txt 或者 http:/192.168.x.x(替换成你的路由器地址)/iptv/iptv.m3u8
- ✅ 如果你每次都能自己把iptv.txt这个文件上传到路由器，那可以不使用这个项目了，但是如果你想每次可以方便且优雅的修改它，那你可以使用本项目，管理地址为http:/192.168.x.x(替换成你的路由器地址)/iptv
- ✅ 直接在网页中粘贴或者编辑你的直播源即可，自动在路由器中保存，不在需要命令行
- ✅ 只提供iptv.txt和iptv.m3u8两个文件的编辑，可以切换，可以记录上次修改的时间
- ✅ 好像就这一点功能，对于多个设备观看自己直播源的用户有点方便
- ✅ 不需要安装任何依赖，不用docker

## 安装方法
### 1 放置文件并设置文件权限
#### 建议在非系统分区放置iptv文件夹，在建立软连接至/www
```bash
ln -s /data/iptv /www/
```
确保/www下有个iptv

#### 设置权限
```bash
chmod 755 /www/iptv
chmod 755 /www/iptv/cgi-bin
chmod 755 /www/iptv/cgi-bin/save.cgi
chmod 644 /www/iptv/iptv.txt
chmod 644 /www/iptv/iptv.m3u8
```


### 2 修改uHTTPd配置 (/etc/config/uhttpd)

```bash
config uhttpd main
    # 用于调用本机的shell保存文件
    list interpreter ".cgi=/bin/sh"
    # 强制所有文本文件使用UTF-8编码，用于识别链接中的中文，如http://192.168.x.x/iptv/logo/山东卫视.png
    option index_options  'Charset=UTF-8'
```

无注释版

```bash
config uhttpd main
    list interpreter ".cgi=/bin/sh"
    option index_options  'Charset=UTF-8'
```

### 3 重启服务
```bash
/etc/init.d/uhttpd restart
```

## 更新日志

[更新日志](./CHANGELOG.md)

## 赞赏

<div>暂不需要~</div>


## 关注

不用


## 免责声明

本项目仅供学习交流用途，开发者不负任何责任

## 许可证

[MIT](./LICENSE) License &copy; 2025-PRESENT [wangweiwei104](https://github.com/wangweiwei104)

