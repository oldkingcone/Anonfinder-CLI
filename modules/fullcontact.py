import urllib.request
import json
import datetime
import random
import os
def request():
    req = urllib.request.Request('https://api.fullcontact.com/v3/person.enrich')
    req.add_header('Authorization', 'Bearer ')
    data = json.dumps({"twitter": "@xyz"}).encode()

    response = urllib.request.urlopen(req, data)
    data_response = json.load(response)

    for keyword in data_response:
        print(keyword)

    print(data_response.get("FullName"), data_response.get("twitter"))

def write(profile):
    file_name = "%s-%s-%s-%s" % ()
    if os.path.exists("../workspaces/FullContact/%s"):
        pass


def get_twitter():
   # twitter = data_response.get("twitter")
    return get_twitter()

def main(profile):
    """Runs normally with User input manually"""



