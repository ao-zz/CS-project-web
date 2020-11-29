# 说明 #
**本目录下的html不再更新** <br>
----------------------------------------<br>
flask集成了Jinja2作为模板引擎。所以用flask开发的html很多是基于模板的（base.html就是一个简单的模板）。html存放位置也是在templates（不要改名）目录下 <br>
**注**：可以存其他文件夹，但操作起来麻烦啊…… <br>
python代码中用到一些扩展，需要在cmd下进行安装。<br>
（清单见 requirments.txt）

安装扩展完成后，按老师的pdf中的方法，在cmd或pyCharm/vscode等下运行app.py，再用浏览器访问[http://127.0.0.1:5000/](http://127.0.0.1:5000/)等页面即可 （不运行app.py而直接打开html是看不到效果的）<br>

# 关于html内容的说明 #
Jinja2的中文文档见https://www.geek-book.com/src/docs/jinja2.11.x/jinja2.11.x/jinja.palletsprojects.com/en/2.11.x/ <br>
调用js、css等，需要用`url_for`方式，详见login.html <br>
部分操作，前后端都可以完成，有待沟通 <br>
