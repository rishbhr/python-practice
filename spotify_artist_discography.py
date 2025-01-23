import requests
import json

def get_token():
    client = ''
    secret = ''

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': client,
        'client_secret': secret,
    }

    response = requests.post(url, headers=headers, data=data)
    token = response.json()['access_token']
    return ("Bearer "+token)

def get_artist_id(token, artist):
    url = f'https://api.spotify.com/v1/search?q={artist}&type=artist'
    headers = {
        'Authorization': token,
    }
    response = requests.get(url, headers=headers)
    return response.json()



with open('/Users/rishbhrana/Documents/Dev/Python/artist.json', 'w', encoding='utf-8') as f:
    json.dump(get_artist_id(get_token(), 'Kanye West'), f, ensure_ascii=False, indent=4)

