from datetime import date
from datetime import timedelta
import requests
from pprint import pprint
today = date.today()
prev_week=[]
week_start=today - timedelta(days=7)
#Email details
From = "abc@xyz.com"
To = "cdf@rst.com"
Subject = "Pull requests for previous week"
username = "hritikch24"
url= f"https://api.github.com/repos/grafana/grafana/pulls?state=all+created=>week_start+updated=>week_start"
result=requests.get(url).json()
print("From : {}".format(From))
print("To : {}".format(To))
print("Subject: {}".format(Subject))
print("Body:")

if(len(result)>0):
    for i in range(len(result)):
        requester=result[i]["user"]["login"]
        title=result[i]["title"]
        state=result[i]["state"]
        updated=result[i]["updated_at"]
        head=result[i]["head"]["label"]
        base=result[i]["base"]["label"]
        print("Pull request {} created by {} on {} from {} to {} is in {} state".format(title,requester,updated,head,base,state))
else:
    print("No pull request")
