import asyncio
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin.db import Event


# Fetch the service account key JSON file contents
cred = credentials.Certificate('firekey.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://exam-c84ff-default-rtdb.firebaseio.com/"

})
new = ''



def change(e: Event):
    print('Произошло изменение бд')
    print(e.data)


ref = db.reference('users')
ref.listen(change)

def set(nickname=None, name=None, surname=None, email=None, password=None):
    db.reference('users').child(nickname).child('name').set(name)
    db.reference('users').child(nickname).child('surname').set(surname)
    db.reference('users').child(nickname).child('nickname').set(nickname)
    db.reference('users').child(nickname).child('email').set(email)
    db.reference('users').child(nickname).child('password').set(password)
def fire_get():
    return ref.get()
