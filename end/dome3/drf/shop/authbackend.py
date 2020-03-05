from django.contrib.auth import backends
from django.db.models import Q

from .models import User


class MyLoginBackend(backends.BaseBackend):
    """
    自定义认证类
    """

    def authenticate(self, request, **kwargs):
        """
        :param request:
        :param kwargs:认证参数
        :return:如果认证成功则返回用户信息，否则返回None
        """
        username = kwargs["username"]
        password = kwargs["password"]
        user = User.objects.filter(Q(username=username) | Q(email=username) | Q(telephone=username)).first()
        if user:
            if user.check_password(password):
                return user
            else:
                return None
        else:
            return None
