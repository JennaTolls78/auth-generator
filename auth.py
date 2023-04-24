import requests as req, base64


r = req.session()
login_url = "https://public-ubiservices.ubi.com/v3/profiles/sessions"

# Ubi account needed to generate token
email = "gmail.com"
password = ""

account_login = f'{email}:{password}'
login_encoded = ((account_login).encode('ascii'))
auth = (base64.b64encode(login_encoded)).decode('ascii')

# Headers and payload for sending request
auth_headers = {
    'Authorization': 'Basic ' + auth,
    'Ubi-AppId': '2c2d31af-4ee4-4049-85dc-00dc74aef88f',
    'Ubi-RequestedPlatformType': 'uplay',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Referer': 'https://connect.ubisoft.com/'
    }
auth_payload = {'rememberMe': 'false'}
# Send request
auth_request = r.post(login_url, headers=auth_headers, json=auth_payload)

# Get token and sessionid from the response
auth_response = auth_request.json()
auth_token = auth_response['ticket']
auth_sessionid = auth_response['sessionId']
print (f'{auth_token}')
