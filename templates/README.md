# 说明 #
文件夹里的html都是后端测试时所用的，前端同学也可以参考。 <br> 
要点：模板（templates）理念；导航条；本地时间显示 <br>
flask的web开发理念是多用模板，所以找到的教程示例的html很多是基于模板（base.html）的。html存放位置也是在templates（不要改名）目录下 <br>
python代码中用到一些扩展，需要在cmd下进行安装（参考老师的pdf中flask的安装）。<br>
1. pip install flask-bookstrap <br>
&nbsp;&nbsp;&nbsp;&nbsp;用于支持base.html的导航栏模板，若前端不需要可删去<br>
2. pip install flask-moment <br>
&nbsp;&nbsp;&nbsp;&nbsp;显示本地化日期与时间，下载可能有点慢，若失败请重试。 <br>
&nbsp;&nbsp;&nbsp;&nbsp;计算机需要连接网络 <br>
&nbsp;&nbsp;&nbsp;&nbsp;会自动安装moment.js，无须另下 <br>
3. pip install flask-wtf <br>

安装扩展完成后，按老师的pdf中的方法，在cmd或pyCharm/vscode等下运行app.py，再用浏览器访问[http://127.0.0.1:5000/](http://127.0.0.1:5000/)等页面即可 （不运行app.py而直接打开html是看不到效果的）<br>

# 关于用例中的html内容的说明 #
## base.html ##
一个模板。可以看了其他html再看这个html。包含很多模块（block），每个block都以`{% block 模块名 %}`开始，以`{% end block %}`结束。
> navbar块：一个简易导航栏，由flask-bootstrap扩展支持。<br>
> scripts块：接收从后端发送来的**时间**信息（用例见index.html）<br>
> head块：显示浏览器标签页的小图标（同济校徽）<br>
> content块：内容。模板中为空。<br>
其他的html只需要在开头加上entends语句（见其他html）就可以引入base.html作为模板，并在相应的块填入内容 <br>

## index.html ##
目前只有时间显示功能（由flask-moment扩展支持）<br>
语句

    {{ moment(current_time).format('lll') }}
显示载入页面时的时刻<br>
注：格式可设置，例如将lll换成LLL则时分也呈中文形式。具体参考[http://momentjs.cn/](http://momentjs.cn/)。然而可用格式还是有限的。如不满足前端需求，一定向后端提出来，我们再找其他方案（或者有推荐方案也可）

语句

    {{ moment(current_time).fromNow(refresh=True) }}
显示距离该时刻过去的时间（自动更新，同样可设置格式）<br>
后端只负责发送时间数据，如何显示由前端决定。<br>

## 404.html ##
输入任何无对应html的网址，将跳转到此页面<br>
