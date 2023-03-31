from c99api import EndpointClient

api = EndpointClient

api.key = 'your_api_key'

response = api.emailvalidator(email='test@c99.nl', json=False)
print(response)