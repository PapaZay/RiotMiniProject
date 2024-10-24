import requests
from urllib.parse import urlencode
import riotsettings
import os

#import from bashrc to keep key private
API_KEY = os.getenv("API_KEY")

def get_puud(gameName=None, tagLine=None, region=riotsettings.DEFAULT_REGION):
    if not gameName:
        gameName = input("Insert VALORANT Name:")

    if not tagLine:
        tagLine = input("Insert Tagline (ex:####):")


    params = {
        'api_key': API_KEY
    }

    api_url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}"

    try:
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error getting account data from API: {e}')
        return None
    
def get_actid(region=riotsettings.DEFAULT_REGION):
    params = {
        'api_key': API_KEY
    }

    api_url = f"https://na.api.riotgames.com/val/content/v1/contents"

    try:
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        data = response.json()

        return data
    except requests.exceptions.RequestException as e:
        print(f'Error getting account data from API: {e}')
        return None

    
def get_matchhistory(get_puud):

    api_url = f"https://na.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}"
    try:
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error getting account data from API: {e}')
        return None
