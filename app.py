#######################################
# encoded with UTF-8
# 各扩展的作用请见/templates/README.md
# 部分扩展有更新，建议使用新版写法
#######################################
import flask
from flask import render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy


app = flask.Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
# mysql+pymysql://username:password@hostname/database
# password改为自己的password
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql+pymysql://root:19mul19=361A@127.0.0.1:3306/test2?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = 'cd499f96a0a4fc9853a0d67d2acb29e'
# 密钥生成方法：打开IDLE，依次输入
# import uuid
# uuid.uuid4().hex
# 这样就能获得一串密钥


#######################################################################
class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    end_time = db.Column(db.Date)
    ddl = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Event %r>" % self.name


class User(db.Model):
    __tablename__ = 'user'  # 数据库中的表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64))
    event = db.relationship('Event', backref='user', lazy='dynamic')

    def __repr__(self):
        return "<User %r>" % self.name


class UserForm(FlaskForm):  # Form是扩展提供的基类
    # StringField是文本字段；其他字段类型（非常丰富）见 p35
    # Requied 是一个基本验证函数；其他验证函数（丰富）见 p35
    user_id = StringField('账号:', validators=[DataRequired()])
    name = ''
    password = StringField('密码:', validators=[DataRequired()])
    # password
    submit = SubmitField('登录')

# class EventForm(FlaskForm):  # 事件表单


################################################################
@app.route('/', methods=['GET', 'POST'])
def index():
    uform = UserForm()
    # 不要漏掉了()  ↑
    if uform.validate_on_submit():
        # 注：下面的登录是为了显示不同用户的资料，并不是合理的登录逻辑
        user = User.query.filter(User.id == uform.user_id.data,
                                 User.password == uform.password.data
                                 ).first()
        if user:
            old_user = session.get('user_id')
            if old_user != uform.user_id.data:
                flash('用户切换成功')
            session['known'] = True
            # event是事件list，包含所有找到的事件
            event = Event.query.filter(
                Event.user_id == uform.user_id.data).all()
            # 怎样把event传给前端页面？
        else:
            user = User(id=uform.user_id.data, password=uform.password.data)
            db.session.add(user)
            session['known'] = False
        session['name'] = user.name

        uform.user_id.data = ''
        uform.name = ''
        return redirect(url_for('index'))  # 视图函数的名字（而不是html的名字；考虑跳到event.html）
    return render_template('index.html',  # 显示对应的事件页面
                           uform=uform,
                           name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    # url_for('index', name=...)


@app.route('/about')
def about():
    return render_template('about.html')


#######################################
# 需要数据交互与数据库操作
#######################################
@app.route('/gantt/<event_id>')
def add(event_id):
    return render_template('gantt.html', event_id=event_id)


@app.route('/event/<user_id>')
def html_homepage(user_id):
    return render_template('event.html', user_id=user_id)


if __name__ == '__main__':
    app.run(debug=True)
