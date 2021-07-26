# 运行
> chia运行脚本：\chiadoge\main.py <br>


# 打包
> 进入项目根目录 <br>
> pyinstaller -F main.spec
 
# 联网
请确保机器可以访问外网

# 注意
如果提示如下错误，找不到APScheduler
> pkg_resources.DistributionNotFound: The 'APScheduler' distribution was not found and is required by the application

将项目中如下两个文件夹复制
> ./venv/Lib/apscheduler<br>
> ./venv/Lib/APScheduler-3.7.0.dist-info

粘贴到本地机器的Python安装目录中
> %USERPROFILE%\AppData\Local\Programs\Python\Python39\Lib\site-packages

# pyinstaller打包报错：
> ModuleNotFoundError: No module named 'requests' <br>
> Failed to execute script chiadoge
> 
> 如何处理：<br>
> 随便找个py文件，在头部添加import requests，然后安装<br>
> 安装完毕后，再把import requests删除掉即可



记录：

chia configure - log - level=info
