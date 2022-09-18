from instagrapi import Client
from dotenv import load_dotenv
import os

load_dotenv()
username = str(os.getenv('IgName'))
password = str(os.getenv('IgPassword'))

name = str(input('Username : '))

cl = Client()
cl.login(username=username, password=password)
account = cl.account_info().dict()

info = cl.user_info_by_username(name).dict()

try:    
    print('Profil Id: '+info['pk'])
    print('Profil Name: '+info['username'])
    print('Profil Full Name: '+info['full_name'])
    private = str(info['is_private'])
    verified = str(info['is_verified'])
    print('Verified: '+verified)
    print('Profil Private: '+private)
    print('Business:')
    business = str(info['is_business'])
    print('Is Business: '+business)
    email = str(info['public_email'])
    print('Email: '+email)
except TypeError:
    pass