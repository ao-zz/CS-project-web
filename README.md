# CS-project-web
## 11月28日更新 ##
1. 更新了一个note.md，作为观看b站教程的笔记。最大收获是了解了session机制，并发现了 输不存在用户会导致数据库新建该用户信息之bug の 产生缘由（！这个bug就是用来向数据库新建用户信息的方法！） <br>
2. 实现了事件字典的传递（原来，这种非输入型的数据，不是通过 FlaskForm 传给前端的……）

## 原始内容 ##
一份极简陋的后端测试用例，为《flask web 开发》第5章及之前的内容。<br> 
注：书中提到的部分扩展的名称已经更新，如flask.ext.bootstrap -> flask_bootstrap（要安装哪些扩展见.py或/templates/README.md）<br>
因为html怎么写的不是后端要关心的事，所以用例里的html不用细看，只要关心教程里的python怎么写、用什么扩展就好（然而这份用例里的.py是肉眼可见的简陋……可以参考教材的配套代码库https://github.com/miguelgrinberg/flasky  或者直接CSDN找现成的说不定效率更高……）<br>
各文件夹的内容在相应的README中说明 <br>
目前后端（可能的）工作方向：<br> 
1. 根据user_id**发送**需要的数据包（flask开发）（可能是前端目前最需要后端做的，方向应该是用表单（FlaskForm类）） <br>
2. 根据user_id，**通过flask工具**从MySql中**查找**（后续再实现新建、修改、删除）对应的信息（flask-MySql，已经初步实现） <br>
3. MySql数据库的框架构建（MySql）。要有2张基本的表，1张存用户信息，1张存各项事件，并且后者还是前者的子表，即所有用户在一张表里，每个用户下又有一个事件表。实现方式是利用~~CSDN~~ “外键”（有一说一，找一份现成的也不是不行）。但是要想让前端能测试，前端的电脑上也得安装MySql并创建数据库（python可以完成数据初始化，但是库还得自己先建）。 <br>
