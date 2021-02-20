1.下载django库
pip install django
2.新建Django项目
django-admin startproject 项目名 （随便找一个文件的根目录即可)
3.启动Django项目
py manage.py runserver
eg:
PS D:\PycharmCode\taoxinyu\networkAPI\HTTP\Django\my_site> py .\manage.py runserver
你刚刚启动的是 Django 自带的用于开发的简易服务器，它是一个用纯 Python 写的轻量级的 Web 服务器。
我们将这个服务器内置在 Django 中是为了让你能快速的开发出想要的东西，因为你不需要进行配置生产级别的服务器（比如 Apache）方面的工作，除非你已经准备好投入生产环境了。
现在是个提醒你的好时机：千万不要 将这个服务器用于和生产环境相关的任何地方。这个服务器只是为了开发而设计的。(我们在 Web 框架方面是专家，在 Web 服务器方面并不是。)


4.项目 VS 应用---这个非常有用
目和应用有什么区别？应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者小型的投票程序。
项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用。


5.所以我们来创建一个应用
py manage.py startapp polls
eg:
PS D:\PycharmCode\taoxinyu\networkAPI\HTTP\Django\my_site> py .\manage.py startapp polls