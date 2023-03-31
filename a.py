from c99api import APIHandler

APIHandler.key = 'HOZIH-Q5924-2GZQJ-RZ6PX'

r= APIHandler.emailvalidator(email='david@cgfsystems.com', json=True)

print(r)