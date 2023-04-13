<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-osuverify

_✨ NoneBot osu!用户审核入群 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/mas-alone/nonebot-plugin-osuverify.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-osuverify">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-osuverify.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

本插件可以实现验证osu!账号是否属实，如果属实即自动批准入群并修改其群名片为申请时输入的id
请在使用时通过`管理群`->`加群方式`->`需要身份认证`中开启`需要回答问题并由管理员审核`并将bot设为管理员

灵感来自nonebot_plugin_bf1_groptools

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-osuverify

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-osuverify
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-osuverify
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-osuverify
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-osuverify
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_osuverify"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| osu_amd | 是 | 无 | 填入osu!官网申请的apiV1 |

申请地址：https://osu.ppy.sh/p/api

填写示例：osu_amd="申请到的api"


## 🎉 使用
无图，无指令。
如果输入的osu!用户名官网查无此人，bot会拒绝，并提示用户输入正确的用户名。

如果验证通过，bot会自动修改用户的Q群备注为osu!用户名。
