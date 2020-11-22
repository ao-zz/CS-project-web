# 数据库初始化，只用运行一次
# 为用户资料数据库创建一些测试数据
# 注：大批量的数据建立，宜通过sql脚本进行
import flask
from flask_sqlalchemy import SQLAlchemy


app = flask.Flask(__name__)
# 将密码（root:到@之间的内容）改为自己的数据库密码
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql+pymysql://root:19mul19=361A@localhost/test2?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


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


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    # 注：下列操作都是初始化操作；在函数中的操作方法见app.py
    # 新建用户
    user_alice = User(name='Alice',
                      password='123456'
                      )
    user_bob = User(name='小明',
                    password='654321'
                    )

    # 新建事件
    alice_event_a1 = Event(name='1 写作业！',
                           end_time='2020-12-01',
                           ddl='2020-12-12',
                           user=user_alice
                           )

    alice_event_a2 = Event(name='2 卷卷 卷！',
                           end_time='2020-12-31',
                           ddl='2021-01-12',
                           user=user_alice
                           )

    bob_event_b1 = Event(name='小明的第一件事',
                         end_time='2019-12-01',
                         ddl='2019-12-03',
                         user=user_bob
                         )

    db.session.add_all([alice_event_a1, alice_event_a2,
                        bob_event_b1, user_alice, user_bob])
    db.session.commit()
    ########################################################################
    # 修改
    alice_event_a1.name = '更改后的 1 写作业！'
    db.session.add(alice_event_a1)
    db.session.commit()

    # 删除
    # db.session.delete(user_alice)

    # 查询（print语句方便看结果。实际使用时可删）
    print(Event.query.filter_by(user=user_alice).all())
    # 查询执行函数all返回所有结果。其他常用函数见 P54
    user_event = Event.query.filter_by(user=user_alice)\
        .order_by(Event.end_time).all()
    print(user_event)

    app.run()
