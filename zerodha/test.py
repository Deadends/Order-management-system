from kiteconnect import KiteConnect
import pyotp
import os

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

# Step 3: Check if access token exists and is valid
def get_access_token():
    if os.path.exists("access_token.txt"):
        with open("access_token.txt", "r") as f:
            access_token = f.read().strip()
            kite.set_access_token(access_token)
            try:
                # Test if the access token is still valid
                kite.profile()
                print("Access token is still valid.")
                return True
            except Exception as e:
                print("Access token is invalid or expired. Logging in again.")
                return False
    return False

# Step 4: If access token doesn't exist or is invalid, request manual login
def create_new_session():
    # Step 4.1: Provide URL for manual login
    login_url = kite.login_url()
    print(f"Login at this URL to get the request token: {login_url}")

    # Step 4.2: Ask user to input the request token from the URL
    request_token = input("Enter the request token after logging in: ")

    # Step 4.3: Generate session with request token and API secret
    try:
        data = kite.generate_session(request_token, api_secret=api_secret)
        access_token = data['access_token']
        
        # Step 4.4: Save access token for future use
        with open("access_token.txt", "w") as f:
            f.write(access_token)
        kite.set_access_token(access_token)

        print(f"Access Token: {access_token}")
        print("Session created successfully.")
    except Exception as e:
        print(f"Error creating session: {e}")

# Step 5: Try to load access token, if not found or invalid, create a new session
if not get_access_token():
    create_new_session()

# Step 6: Test session by fetching profile data
try:
    profile = kite.profile()
    print("Logged in successfully!")
    print(profile)
except Exception as e:
    print(f"Error fetching profile: {e}")
