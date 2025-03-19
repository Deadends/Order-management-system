from Connect import XTSConnect
# MarketData API Credentials
API_KEY = ""
API_SECRET = ""
source = "WEBAPI"

# Initialise
xt = XTSConnect(API_KEY, API_SECRET, source)


response = xt.interactive_login()
print("login: ",response)
print(response)
