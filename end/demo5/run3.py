from celery.result import AsyncResult
from gongchang import *
if __name__ == '__main__':
    res = AsyncResult("f2beb3d1-1356-42bd-bfb2-fc90f4bf2990", backend="redis://127.0.0.1:6379/10")
    print(res)
