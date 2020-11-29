# CS-project-web
## 11月28日更新 ##
1. 更新了一个note.md，作为观看b站教程的笔记。最大收获是了解了session机制，并发现了 输不存在用户会导致数据库新建该用户信息之bug の 产生缘由（！这个bug就是用来向数据库新建用户信息的方法！） <br>
2. 实现了事件字典的传递（原来，这种非输入型的数据，不是通过 FlaskForm 传给前端的……）
3. 放弃了使用flask-wtf做值接受，改为采用`request.form.get('user_id')`的方法

下一步的方向：
1. gantt图的实现
2. 蓝图设计与模块分离（分成多个.py，对应教程第7章）
3. 用户资料相关，包括登录逻辑的完善、注册、修改密码等。会用到数据库操作（极其简单）

## 原始内容 ##
一份极简陋的后端测试用例，为《flask web 开发》第5章及之前的内容。<br> 
注：书中提到的部分扩展的名称已经更新，如flask.ext.bootstrap -> flask_bootstrap（要安装哪些扩展见.py或/templates/README.md）<br>
因为html怎么写的不是后端要关心的事，所以用例里的html不用细看，只要关心教程里的python怎么写、用什么扩展就好（然而这份用例里的.py是肉眼可见的简陋……可以参考教材的配套代码库https://github.com/miguelgrinberg/flasky  或者直接CSDN找现成的说不定效率更高……）<br>
各文件夹的内容在相应的README中说明 <br>
