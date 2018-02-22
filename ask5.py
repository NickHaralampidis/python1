import tweepy
from datetime import datetime,date,time,timedelta
from collections import counter
import sys
consumer_key="qHm6ByOidoyIVACcWMV9STs8D"
consumer_secret="QLuGaSTB12oDHpDjWfB6BW0UN8Me8N122oKZrcM67xyiJNuS11"
access_token="966668929707003909-H5dVdg6B4RaTjTb32dDg37y56kownRI"
access_token_secret="wVqOXG2CnQB0aiUJEfxOpgRZli0DqAi2D77p4husJCLTK"
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
auth_api = API(auth)
username=input()
list1=[]
newtweets = api.user_timeline(screen_name = username,count=10)
list1.append(newtweets)

for i in range (0,10):
	list1[i].split(" ")
flatlist=[]
for i in list1:
	for j in i:
		flatlist.append(j)
c=len(flatlist)
s=[]
k=0
for j in range (0,c):
	for i in range (0,c):
		if flatlist[j]==flatlist[i] and flatlist!="":
			k=k+1
		else:
			k=0
	s.append(k)
	k=0

max=s[0]
thesh=0
for i in range (1,c):
	if max<s[i]:
		max=s[i]
		thesh=i
print flatlist[thesh]
			
	
	
	