import os

import requests
from security import create_access_token
from model import Token


BASE_URL = "http://193.162.143.114:3456"
ID_USER = 2092707504


def auth(id_user):
    data = create_access_token({'sub': str(id_user)})
    return Token(access_token=data['access_token'],
                 token_type='Bearer')


def get(url):
    token = auth(ID_USER)
    headers = {"Authorization": token.token_type + ' ' + token.access_token,
               'Content-Type': 'application/json'}
    response = requests.get(BASE_URL+url,headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'status': 19, 'msg': 'response server ' + str(response.text)}


def get_proxy(country):
    url = f"/bot/search?cc={country}&city=&zip=&reg=&conn=&extars=&leases="
    response = get(url)
    if response['status'] != 0:
        return None
    id_proxy = response['data']['agents'][0]['id']
    ammount = response['data']['agents'][0]['priceShrC']
    ammount = float(ammount)/100


    url = f'/bot/buy?id={id_proxy}&amount={ammount}&type=rent'

    response = get(url)
    print(response)
    if response['status'] != 0:
        return None
    response = response['data']
    socks = f"{response['socks']['user']}:{response['socks']['pwd']}@{response['socks']['ip']}:{response['socks']['port']}"
    print(socks)
    return socks