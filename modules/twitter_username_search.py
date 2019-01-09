import tweepy

con_key="YOURS"
con_sec="YOURS"
access_token='YOURS'
access_secret='YOURS

auth = tweepy.OAuthHandler(consumer_key=con_key,
                           consumer_secret=con_sec)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

users = ["elonmusk", "microsoft"] #append your users here.

for user_name in users:
	user = api.get_user(screen_name = user_name)
	print("Found Username: {}\nLocation: {}\n".format(user.id, user.location))
	for item in api.user_timeline(user_name):
		print("Username's Timeline {}: {}\n".format(user_name, item))
