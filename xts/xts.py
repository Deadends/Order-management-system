from Connect import XTSConnect
# MarketData API Credentials
API_KEY = "2f5912b07b4542edb20182"
API_SECRET = "Jive806@oH"
source = "WEBAPI"

# Initialise
xt = XTSConnect(API_KEY, API_SECRET, source)


response = xt.interactive_login()
print("login: ",response)
print(response)
