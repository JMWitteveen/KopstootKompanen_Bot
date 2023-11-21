#!/usr/bin/python
import praw
import re
import os
from dotenv import load_dotenv

load_dotenv()
# Create the Reddit instance
#reddit = praw.Reddit('bot1')

reddit = praw.Reddit(client_id=os.getenv("REDDIT_API_KEY"),
		     client_secret=os.getenv("REDDIT_API_SECRET"),
		     user_agent=os.getenv("REDDIT_USERAGENT"),
		     username=os.getenv("REDDIT_USERNAME"),
		     password=os.getenv("REDDIT_PASSWORD"))


kopstoot_definition = "De Kopstoot Kompanen is een groep van ruim 1000 leden exclusief voor lange mensen. Mannen vanaf 1,95m en vrouwen vanaf 1,80m"

# Have we run this code before? If not, create an empty list
if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []

# If we have run the code before, load the list of comments we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))

# Get the top 10 values from our subreddit
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=10):
    # Iterate through comments in the submission
    for comment in submission.comments.list():
        # If we haven't replied to this comment before
        if comment.id not in comments_replied_to:
            # Do a case insensitive search
            if re.search("!KopstootKompanen", comment.body, re.IGNORECASE):
                # Reply to the comment
                print("Comment content: ", comment.body)
                comment.reply(kopstoot_definition)
                print("Bot replying to comment in submission: ", submission.title)

                # Store the current id into our list
                comments_replied_to.append(comment.id)

# Write our updated list back to the file
with open("comments_replied_to.txt", "w") as f:
    for comment_id in comments_replied_to:
        f.write(comment_id + "\n")
