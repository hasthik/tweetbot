import tweepy
import time
import requests
import json
from datetime import date
import calendar
import urllib.request
import random
from keys import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api
payload={"username":"Damiloski","artPoints":20100}
r=requests.get("https://mathbitcoin.com/expansive-world/profiles",params=payload)
data=json.loads(r.text)
count=1
curr_date = date.today()
print(calendar.day_name[curr_date.weekday()])
def upload_media(text, filename):
    media = api.media_upload(filename)
    api.update_status(text, media_ids = [media.media_id_string])
def randu():
    y=random.randint(1,25)
    q=random.randint(30,37)
    if(count%2==0):
        return y
    else:
        return q
while (1):
    i=1
    f = open("textfile.txt", "w")
    f.truncate(0)
    f.write("Top 4 @NFTitem Profiles\n")
    v=randu()
    imageno="1"+".png"
    print(v)
    web="https://coreminterstackprods3nftmine83689-nftmine6aababc1-1i1zrafm04pwk.s3.amazonaws.com/item-images/slime_"+str(v)+".png"
    urllib.request.urlretrieve(web, imageno)
    for profiles in data['profiles']:
        ap=0
        add=0
        user=0
        try:
            print("User Name : ", profiles['username'])
            f.write("User : "+profiles['username']+"\n")
        except Exception as e:
            user=1
        try:
            print("Art Points : ",profiles['artPoints'])
            f.write("Art Points : "+str(profiles['artPoints'])+"\n")
        except Exception as e:
            ap=1
        try:
            print("Address : ",profiles['address'])
            f.write("Address : "+profiles['address']+"\n")
        except Exception as e:
            add=1
        f.write("\n")
        i=i+1
        if(i>=5):
            break
    f.close()
    g = open("textfile.txt", "r")
    upload_media(g.read(),imageno)
    print(g.read())
    g.close()
    time.sleep(10)
    count=count+1
