from requests_oauthlib import OAuth1Session
import secret_data
import json
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

client_key = secret_data.client_key
client_secret = secret_data.client_secret

resource_owner_key = secret_data.access_token
resource_owner_secret = secret_data.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)



python_obj = json.loads(r.text) #type(python_obj) is a dictionary!

lst = python_obj['statuses']

onedict = lst[4]

# print (r.text)
# print(type(python_obj))
# print(python_obj.keys())
# print(type(lst))
# print(type(lst[4]))
# print(onedict.keys())
# print ("ASDLFKMASDLFKMASLDKFMASLFDKM")
# print(onedict['text'])
# print(onedict['user']['name'])

for i in lst: 
	print("Author: ",i['user']['name'])
	print("Text: ", i['text'])
