import tweepy
import time

#First parameter is Consumer Key, second is Consumer Secret
api = tweepy.API(auth)

#See rate limit
# api.rate_limit_status()

def most_followed(target):
# Who follows our target? 
  name = []
  count = []
  for f in tweepy.Cursor(api.followers, screen_name=target.screen_name).items():
    name.append(f.screen_name)
    count.append(f.followers_count)
    time.sleep(3)

# Who is our target's follower with most followers?
  max_index = count.index(max(count))
  max_follower = name[max_index]
  return max_follower

# Trying 2 degrees of separation
# Who follows our target's followers? Collect all and find the one with most followers
# Name array previously contains the screen names of our target's followers

# for i in name:
#   user = api.get_user('name[i]')
#   for f in tweepy.Cursor(api.followers, screen_name=user.screen_name).items():
#     name.append(f.screen_name)
#     count.append(f.followers_count)
#     time.sleep(3)
#     
# max_index_2degress = count.index(max(count))
# max_follower_2degrees = name[max_index]
# return max_follower_2degrees 

# p.s: I didn't try running the code because some of Matt's followers have huge number of followers

def most_active(target):
# Who is the most active user our target follows?
# Active being the user with highest sum of tweets and favorites 
  target_friends = api.friends(id=target.screen_name)
  name = []
  tweet = []
  fav = []
  for f in target_friends:
    name.append(f.screen_name)
    tweet.append(f.statuses_count)
    fav.append(f.favourites_count)
    time.sleep(3)

  activity = [sum(x) for x in zip(tweet, fav)]
  max_index = activity.index(max(activity))
  max_activity = name[max_index]
  return max_activity

#Get our target
matt = api.get_user('mcdickenson')

print most_followed(matt) # VirginAmerica
print most_active(matt)   # jseattle
    
