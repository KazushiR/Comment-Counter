import wikipedia, praw, sqlite3, os, json, random, time
from datetime import datetime
from praw.models import MoreComments

conn = sqlite3.connect("nouns.db")
c = conn.cursor()
c.execute("SELECT * FROM Noun_Counter")

row = c.fetchall()

Automated_Response = "Hello, I am a bot that likes to give facts. I found something you referenced and will just randomly spit out this fact to you. Please ignore me if this bothers you, I am just a test bot and I am testing my programming out. \n\n\n"

time = datetime.today().strftime("%b %Y")
nouns = dict([(noun, occurence) for date, noun, occurence in row if date == time])
print(nouns)

os.chdir(r"C:\Users\krickert\Desktop\Python projects\Python Praw")
with open("config_cred.json") as r:
    data = json.load(r)
    reddit = praw.Reddit(client_id = data["client_id"],
                     client_secret = data["client_secret"],
                     username = data["username"],
                     password = data["password"],
                     user_agent = data["user_agent"])
    r.close()

subreddit = reddit.subreddit("praw_practice")

for i in subreddit.hot(limit = 1):
    subreddit_id = i.id
    submission = reddit.submission(id = subreddit_id)
    print(submission.title)
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        print(top_level_comment.body)
        comments = top_level_comment.body.split()
        noun_2 = [i for i,v in nouns.items() if i in comments]
        if not noun_2:
            continue
        else:
            print(noun_2)
            choice = random.choice([True, False])
            print(choice)
            if choice == True:
                try:
                    print("Needs to reply to comment")
                    Wikipedia = wikipedia.summary(random.choice(noun_2))
                    top_level_comment.reply(Automated_Response + Wikipedia)
                    time.sleep( 600 )
                except wikipedia.exceptions.DisambiguationError:
                    continue
            else:
                print("Do not reply to comment")
                continue
            
