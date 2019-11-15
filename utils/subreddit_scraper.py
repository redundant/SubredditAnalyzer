import praw
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

with open("credentials.txt","r") as settings:
    # get rid of newline/eof
    client_id = settings.readline()[:-1]
    client_secret = settings.readline()[:-1]


reddit = praw.Reddit(client_id = client_id, client_secret = client_secret, user_agent="linux:1N807PTJOf8jxg<app ID>:0.0 (by /u/SilchasRuin)")

def scrape_comments(subreddit, quarantined=False):
    """ This function takes a subreddit name and scrapes comments of the top 100 posts of all time
    
        Input: subreddit: a string for the subreddit
                quarantined: whether or not the community is quarantined

        Effect: adds comment data to the project mongodb collection.
    """

    sub = reddit.subreddit(subreddit)

    if quarantined: 
        sub.quaran.opt_in()

    client = MongoClient()

    db = client.redditproject

    db.authenticate("redundant","monkey")
    
    # Top 100 of all time from the subreddit. All comments are expanded out
    for post in sub.top(limit = 100):
        comments = post.comments
        comments.replace_more(limit=None)

        for comment in comments.list():
            try:
                #do this one at a time because generating the whole list is memory intensive for my AWS instance.
                db.redditproject.insert_one({"_id":comment.id,"sub":subreddit,"body": comment.body, "time":comment.created_utc, "score": comment.score}) 

            except DuplicateKeyError:
                # let's just keep going adding points
                continue
scrape_comments("the_donald", True)
scrape_comments("fullcommunism",True)
