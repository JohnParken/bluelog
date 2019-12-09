# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import random

from faker import Faker
from sqlalchemy.exc import IntegrityError

from bluelog import db
from bluelog.models import Admin, Category, Post, Comment, Link

fake = Faker()

# 生成管理员用户，设置 confired=True
def fake_admin():
    admin = Admin(
        username='baodongyue',
        blog_title='MSKJ',
        blog_sub_title="Welcome to NLP of MSKJ.",
        name='MSKJ',
        about='你好，此处是民生科技NLP组资源分享站。'
    )
    admin.set_password('baodongyue@123')
    # set confirmed=True
    admin.set_confirmed(True)
    db.session.add(admin)
    db.session.commit()

def fake_xc():
    xuchao = Admin(
        username = 'xuchaonet'
    )
    xuchao.set_password('iamxuchao@mskj')
    db.session.add(xuchao)
    db.session.commit()

def fake_bdy():
    baodongyue = Admin(
        username = 'bdy'
    )
    baodongyue.set_password('baodongyue@123')
    db.session.add(baodongyue)
    db.session.commit()


def fake_categories(count=1):
    category = Category(name='资源分享')
    db.session.add(category)

    for i in range(count):
        category = Category(name=fake.word())
        db.session.add(category)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def fake_posts(count=50):
    for i in range(count):
        post = Post(
            title=fake.sentence(),
            body=fake.text(2000),
            category=Category.query.get(random.randint(1, Category.query.count())),
            timestamp=fake.date_time_this_year()
        )

        db.session.add(post)
    db.session.commit()


def fake_comments(count=500):
    for i in range(count):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

    salt = int(count * 0.1)
    for i in range(salt):
        # unreviewed comments
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=False,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

        # from admin
        comment = Comment(
            author='Mima Kirigoe',
            email='mima@example.com',
            site='example.com',
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            from_admin=True,
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    db.session.commit()

    # replies
    for i in range(salt):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            replied=Comment.query.get(random.randint(1, Comment.query.count())),
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    db.session.commit()


def fake_links():
    民生科技有限公司 = Link(name='民生科技有限公司', url='http://www.mskj.com')
    中国民生银行 = Link(name='中国民生银行', url='http://www.cmbc.com.cn')
    db.session.add_all([民生科技有限公司, 中国民生银行])
    db.session.commit()
