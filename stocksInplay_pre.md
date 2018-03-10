
## selenium 跟 PhantomJS
因为网页要解析js脚本要用到selenium 跟 PhantomJS   
PhantomJS 是个没有gui的浏览器   
selenium 相当于浏览器的操控器，主要用到里面的webdriver，可以对浏览器做一些操作，如点击，提交。。。


#### 参考了：[从零开始写Python爬虫 --- 3.1 Selenium模拟浏览器](https://zhuanlan.zhihu.com/p/27115580) 

#### 安装 selenium
```
pip install selenium
```
[Selenium with Python中文翻译文档](http://selenium-python-zh.readthedocs.io/en/latest/)    
[selenium官网 使用文档](https://www.seleniumhq.org/)  
[selenium官方文档 爬虫相关的接口，用起来没有bs4那么方便](https://www.seleniumhq.org/docs/03_webdriver.jsp#introducing-the-selenium-webdriver-api-by-example)  
[selenium api 列表](https://seleniumhq.github.io/selenium/docs/api/py/index.html#drivers)

#### 安装[PhantomJS](http://phantomjs.org/download.html)
可以直接在官网下载phantomjs.exe文件，用vpn会下载快一点。下载的文件放到工程目录就好了。到时候可以用相对路径直接访问
``` python
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'.\phantomjs-2.1.1-windows\bin\phantomjs.exe')
```





