# 针对用户业务逻辑处理的视图和路由定义

from . import user


@user.route('/user')
def user_view():
    return '这是user的页！'

