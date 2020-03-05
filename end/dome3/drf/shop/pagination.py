from rest_framework import pagination

"""
自定义的分页页面
"""


class MyPageNumberPagination(pagination.PageNumberPagination):
    page_size = 4
    page_query_param = 'page_num'
    page_size_query_param = 'num'
