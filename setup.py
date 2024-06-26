import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="nonebot-plugin-osuverify",  # 项目名称，保证它的唯一性，不要跟已存在的包名冲突即可
    version="0.1.3",  # 程序版本
    author="A M D",  # 项目作者
    author_email="mas_alone@qq.com",  # 作者邮件
    description="通过osu!账号审核入群功能",  # 项目的一句话描述
    long_description=long_description,  # 加长版描述？
    long_description_content_type="text/markdown",  # 描述使用Markdown
    url="https://github.com/mas-alone/nonebot-plugin-sayoroll",  # 项目地址
    packages=setuptools.find_packages(),  # 无需修改
    classifiers=[
        "Programming Language :: Python :: 3.8",  # 使用Python3.8
        "License :: OSI Approved :: GNU Affero General Public License v3",  # 开源协议
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'httpx>=0.23.3',
        'nonebot2>=2.0.0rc3',
        'nonebot-adapter-onebot>=2.0.0b1'
    ]
)
