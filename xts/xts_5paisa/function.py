from Connect import XTSConnect

API_KEY = "2f5912b07b4542edb20182"
API_SECRET = "Jive806@oH"

source = "WEBAPI"



"""Make XTSConnect object by passing your interactive API appKey, secretKey and source"""
xt = XTSConnect(API_KEY, API_SECRET, source)

"""Using the xt object we created call the interactive login Request"""
response = xt.interactive_login()
print("Login: ", response)
