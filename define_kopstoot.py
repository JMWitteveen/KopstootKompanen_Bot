#!/usr/bin/python
import praw
import re
import random


reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pythonforengineers")

kopstoot_definition = "De Kopstoot Kompanen is een groep van ruim 1000 leden exclusief voor lange mensen. Mannen vanaf 1,95m en vrouwen vanaf 1,80m"

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("!KopstootKompanen", comment.body, re.IGNORECASE):
            
            comment.reply(kopstoot_definition)
            print("replied!")
            