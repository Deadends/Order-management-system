from kiteconnect import KiteConnect
import pyotp
import requests

# Credentials
user_id = 'VJ4170'
password = 'arush123'
api_key = '12kder0f7fjb9waf'
api_secret = 'crebuz2yk6aqx0y8xqv43ogpkl5b8wm8'
totp_key = 'MDQJDQXZZEDAEQGQUGWPXVKOPIMTB6UG'

# Step 1: Generate TOTP using the TOTP key
totp = pyotp.TOTP(totp_key).now()
print(f"Generated TOTP: {totp}")

# Step 2: Initialize KiteConnect session
kite = KiteConnect(api_key=api_key)

# Step 3: Create a session automatically
def create_kite_session():
    try:
        # Login URL (for manual login)
        request_token = kite.login_url()
        print(f"Login at this URL manually: {request_token}")
        
        # Extract the request token after manually logging in to the provided URL
        # You need to manually retrieve the request_token here from the URL
        request_token = "uB6XPfuWALCTc6tLa2Vm7avn7y4Q4PLD"  # Manually replace this after logging in

        # Generate access token using request token and API secret
        data = kite.generate_session(request_token, api_secret=api_secret)

        # 2FA Authentication Check
        response_1 = requests.post("https://api.kite.trade/session/token", data={
            "api_key": api_key,
            "request_token": request_token,
            "checksum": data['access_token']  # Assuming access token is used here, adjust accordingly
        })

        if response_1.status_code == 200:
            print("2FA authentication successful!")
        else:
            print(f"2FA authentication failed. Status code: {response_1.status_code}")
            print(f"Response Text: {response_1.text}")

        print(f"Access Token: {data['access_token']}")
        print(f"Public Token: {data['public_token']}")

        # Set the access token for future API requests
        kite.set_access_token(data['access_token'])

        # Fetch and print profile information after successful login
        try:
            profile = kite.profile()
            print("Logged in successfully!")
            print(profile)
        except Exception as e:
            print("Failed to fetch profile. Not logged in.")
            print(f"Error: {e}")

    except Exception as e:
        print(f"Error during session creation: {e}")

# Step 4: Run the session creation
create_kite_session()   