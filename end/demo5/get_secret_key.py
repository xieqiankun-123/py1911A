import os
"""
生成24位的密钥
"""
secret_key = os.urandom(24)
print(secret_key)
