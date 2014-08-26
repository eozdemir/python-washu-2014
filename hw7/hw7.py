from bs4 import BeautifulSoup
import csv
from nltk.util import clean_html
import urllib2
import time
import tweepy
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

# Web scraping from hw5
page_to_scrape = 'http://101books.net/archives/'  # A book blog
# headers = ["Date", "Title"]
# filename = "blog_info_ramram.csv"
# readFile = open(filename, "wb")
# csvwriter = csv.writer(readFile)
# csvwriter.writerow(headers)
webpage = urllib2.urlopen(page_to_scrape)
soup = BeautifulSoup(webpage.read())
soup.prettify()

# For title table
titles = soup.findAll("li", attrs = {'class':"clear"})
for title in titles:
    t = clean_html(title.find("a")['title'])
    t = t[18::]
    print "{0}".format(t.encode('ascii', 'ignore'))

title_array = []
author_array = ['Robert']*25
# p.s. The code for scraping the author name works but doesn't return a very clean string, that's why i generated the array like this
for i in range(25):
    title = titles[i]
    t = clean_html(title.find("a")['title'])[18::]
    t = t.encode('ascii', 'ignore')
    title_array.append(t)
# print title_array
# print author_array

#Connect to the local database
engine = sqlalchemy.create_engine('sqlite:////Users/elifozdemir/inclass.db', echo=True)
Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id")) # refers to id column in authors table
    # ForeignKey linking this one with another tables primary key
    def __init__(self, name, author=None):
        self.name = name
        self.author = author
    def __repr__(self):
        return "<Post('%s')>" % (self.name)

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship("Post", backref="author") # multiple posts by the same author
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "<author('%s')>" % (self.name)

Base.metadata.create_all(engine) # First time create tables
Session = sessionmaker(bind=engine) #Create a session to actually store things in the db
session = Session()

# Create titles in a loop and add them to the session
for i in range(len(title_array)):
    post_to_add = Post(title_array[i])
    session.add(post_to_add)

#Persist all of this information
session.commit()

#how to work with relations
robert = Author('Robert')

posts = session.query(Post).all()
for i in range(len(posts)):
    posts[i].author = robert

print posts[0].author
print posts[0].author.posts # all posts from the author of first post/ basically all posts since the author is the same
# equivalently
# print posts

# Using APIs from hw6
# I didn't use relation for this part, its only a user_table
api = tweepy.API(auth)

def followers(target):
    # Who follows our target?
    name = []
    count = []
    for f in tweepy.Cursor(api.followers, screen_name=target.screen_name).items():
        name.append(f.screen_name)
        count.append(f.followers_count)
        time.sleep(5)
    return (name, count)

#Get our target
matt = api.get_user('doanimen2')
# First I used Matt, but to make it run shorter I used a someone with only 4 followers
print followers(matt)

class User(Base):
    __tablename__ = 'users' # making a user-table as suggested in the class
    id = Column(Integer, primary_key=True)
    name = Column(String)
    count = Column(Integer)
    def __init__(self, name, count):
        self.name = name
        self.count = count
    def __repr__(self):
        return "<User('%s','%s')>" % (self.name, self.count)

Base.metadata.create_all(engine)
session2 = Session()

name = followers(matt)[0]
count = followers(matt)[1]

for i in range(len(name)):
    user_to_add = User(name[i], count[i])
    session2.add(user_to_add)

session2.commit()
users = session2.query(User).all()

for i in range(4):
    print users[i]


