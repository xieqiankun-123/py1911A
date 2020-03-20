"""
测试序列化与反序列化实现代码
"""
from itsdangerous import TimedJSONWebSignatureSerializer,SignatureExpired,BadSignature
import time
id = 1001

seriaUtil = TimedJSONWebSignatureSerializer("hellopy1911",expires_in=2)
serstr =  seriaUtil.dumps({"id":id}).decode("utf-8")
print("序列化结果",serstr)

time.sleep(5)

try:
    seriaUtil = TimedJSONWebSignatureSerializer("hellopy1911")
    obj = seriaUtil.loads(serstr)
    print("反序列化对象", obj["id"])
except SignatureExpired as e:
    print(e,"过期了")
except BadSignature as e:
    print(e,"秘钥错误")