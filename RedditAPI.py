import praw, os, json, time, nltk
from praw.models import MoreComments
from collections import Counter

times = int(input("How many times?: "))

Author_final = {}
Author_time = {}
Comments_final = {}

Author_cnt = Counter()
comments_cnt = Counter()

All_Nouns = []

os.chdir(r"C:\Users\krickert\Desktop\Python projects\Twitter API")
with open("config_cred.json") as r:
    data = json.load(r)
    reddit = praw.Reddit(client_id = data["client_id"],
                     client_secret = data["client_secret"],
                     usernane = data["username"],
                     password = data["password"],
                     user_agent = data["user_agent"])
    r.close()

subred = reddit.subreddit("conservative")

#print(dir(x))
def comments(times):
    count = 0
    hot = subred.hot(limit = times)
    x = next(hot)
    for i in hot:
        subreddit_id=i.id
        submission = reddit.submission(id=subreddit_id)
        submission.comment_limit = times
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            new_comments = top_level_comment.body.split()
            for word in new_comments:
                comments_cnt[word.lower()] += 1
            tokenized = nltk.word_tokenize(top_level_comment.body)
            for word,pos in nltk.pos_tag(tokenized):
                if (pos == "NN" or pos == "NP"):
                    All_Nouns.append(word)
            {k: comments_cnt.get(k, 0) + Comments_final.get(k, 0 ) for k in set(comments_cnt) and set (Comments_final)}
            count+= 1
        utc_time = i.author.created_utc
        author_creation = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(utc_time))
        Author_time[i.author] = author_creation
    print("Finished with the comments portion!")

def authors(times):
    count = 0
    hot = subred.hot(limit = times)
    x = next(hot)
    for i in hot:
        subreddit_id=i.id
        submission = reddit.submission(id=subreddit_id)
        submission.comment_limit = times
        for comment in i.author.comments.new(limit = times):
            author_count = 0
            tokenized = nltk.word_tokenize(comment.body)
            for word,pos in nltk.pos_tag(tokenized):
                if (pos == "NN" or pos == "NP"):
                    All_Nouns.append(word)
            comments = comment.body.split()
            for word in comments:
                Author_cnt[word.lower()] +=1
                {k: Author_cnt.get(k, 0) + Author_final.get(k, 0 ) for k in set(Author_cnt) and set (Author_final)}
    print("Finished with the author portion!")
comments(times)
authors(times)


