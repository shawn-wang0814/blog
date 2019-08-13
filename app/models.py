# 与当前项目相关的模型文件，即所有的实体类在此编写

from . import db


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key=True)
    cate_name = db.Column(db.String(50),nullable=False)
    topics = db.relationship('Topic',backref='category',lazy='dynamic')

    def __init__(self,cate_name):
        self.cate_name = cate_name
    def to_dict(self):
        dict ={
            "id":self.id,
            "cate_name":self.cate_name
        }
        return dict


class BlogType(db.Model):
    __tablename__ = 'blogtype'
    id = db.Column(db.Integer,primary_key=True)
    type_name = db.Column(db.String(20),nullable=False)
    #增加与topic之间的关联关系和反向引用
    topics = db.relationship('Topic',backref='blogType',lazy='dynamic')


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    loginname = db.Column(db.String(50),nullable=False)
    uname = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    url = db.Column(db.String(200))
    upwd = db.Column(db.String(30),nullable=False)
    is_author = db.Column(db.SmallInteger,default=0)
    # 增加与topic之间的关联关系和反向引用
    topics = db.relationship('Topic',backref='user',lazy='dynamic')
    replies = db.relationship('Reply',backref='user',lazy='dynamic')
    voke_topic = db.relationship(
        'Topic',
        secondary='voke',
        backref=db.backref('voke_users',lazy='dynamic'),
        lazy="dynamic"
    )

class Topic(db.Model):
    __tablename__ = "topic"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    pub_date = db.Column(db.DateTime,nullable=False)
    read_num = db.Column(db.Integer,default=0)
    content = db.Column(db.Text,nullable=False)
    images = db.Column(db.Text)
    #关系：一（Category)对多（Topic）的关系
    category_id = db.Column(db.Integer,db.ForeignKey("category.id"))
    #关系：一（BlogType）对多（Topic)的关系
    blogtype_id = db.Column(db.Integer,db.ForeignKey('blogtype.id'))
    #关系：一（user)对多（topic）关系
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    replies = db.relationship('Reply',backref='topic',lazy='dynamic')


class Reply(db.Model):
    __tablename__ = 'reply'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text,nullable=False)
    reply_time = db.Column(db.DateTime)
    topic_id = db.Column(db.Integer,db.ForeignKey('topic.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))


Voke = db.Table(
    "voke",
    db.Column('id',db.Integer,primary_key=True),
    db.Column('user.id',db.Integer,db.ForeignKey('user.id')),
    db.Column('topic_id',db.Integer,db.ForeignKey('topic.id'))
)