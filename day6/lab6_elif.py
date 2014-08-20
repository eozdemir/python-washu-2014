from bs4 import BeautifulSoup
import csv 
from nltk.util import clean_html
import urllib2 
import time 
import re

# What page? 
page_to_scrape = 'http://101books.net/'

# What info do we want? 
headers = ["Page", "Post", "Date", "Url", "Comment Count"] # add , "Title"

# Where do we save info?
filename = "blog_info.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

# Open webpage
webpage = urllib2.urlopen(page_to_scrape)

# Parse it
soup = BeautifulSoup(webpage.read())
soup.prettify()

# tags = soup.findAll(href=re.compile(r"((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)"))
# links = []
# for tag in tags:
#   links.append(tag['href'])
# print links
# 
# for i in links:
#   webpages[i]=urllib2.urlopen(links[i]) # must be indices not unicode
#   time.sleep(1)
  
# soups = BeatifulSoup(webpages.read())

# Is post?
posts = soup.findAll("div", attrs = {'class':"entry"})
print len(posts)
for post in posts:
  p =  clean_html(str(post.find("a")['rel']))
  print p

# Author
# authors = soup.findAll("div", attrs = {'class': "single-post-meta"})
# for author in authors:
#   a = clean_html(str(author.find("div")))
#   print a

# Date
dates = soup.findAll("div", attrs = {'class':"post-date"})
print len(dates)
for date in dates:
  d = clean_html(str(date.find("p")))
  print d

# Title
titles = soup.findAll("div", attrs = {'class':"entry"})
print len(titles)
for title in titles:
  t = clean_html(title.find("a")['title'])
  t = t[18::]
  print t

# Url
urls = soup.findAll("div", attrs = {'class':"entry"})
print len(urls)
for url in urls:
  u = str(url.find("a")['href'])
  print u

# Comments
comments = soup.findAll("div", attrs = {'class':"post-comments"})
for comment in comments:
  c = clean_html(str(comment.find("a")))
  c = c[0:2]
  print c
  
for i in range(7):
  pages = range (1,8)
  page = pages[i]
  date = dates[i]
  d = clean_html(str(date.find("p")))
  title = titles[i]
  t = clean_html(title.find("a")['title'])[18::] # cannot write with csv writer
#   t = ("'" + str(t.encode("ascii")) + "'")
  post = posts[i]
  p = clean_html(str(post.find("a")['rel']))
  if p == "[u'bookmark']":   # post if bookmark
    post = 1
  else:
    post = 0  
  url = urls[i]
  u = str(url.find("a")['href'])
  comment = comments[i]
  c = clean_html(str(comment.find("a")))[0:2]
#   author = authors[i]
#   a = clean_html(str(author.find("div")))
  csvwriter.writerow([page, post, d, u, c, t])

readFile.flush()
readFile.close()