from bs4 import BeautifulSoup
import csv 
from nltk.util import clean_html
import urllib2 
import time 

# What page? 
page_to_scrape = 'http://101books.net/archives/'  # A book blog

# What info do we want? 
headers = ["Page", "Post", "Date", "Url", "Title", "Author", "Comment Count"]

# Where do we save info?
filename = "blog_info_ramram.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

# Open webpage
webpage = urllib2.urlopen(page_to_scrape)

# Parse it
soup = BeautifulSoup(webpage.read())
soup.prettify()

# Links to posts
links = soup.findAll("li", attrs = {'class':"clear"})
l = []
for link in links:
  l.append(str(link.find("a")['href']))
# print l

# Is post?
posts = soup.findAll("li", attrs = {'class':"clear"})
print len(posts)
for post in posts:
  p =  clean_html(str(post.find("a")['rel']))
  print p

# Date
dates = soup.findAll("li", attrs = {'class':"clear"})
print len(dates)
for date in dates:
  d = clean_html(str(date.find("span")))
  print d

# Title
titles = soup.findAll("li", attrs = {'class':"clear"})
print len(titles)
for title in titles:
  t = clean_html(title.find("a")['title'])
  t = t[18::]
  print "{0}".format(t.encode('ascii', 'ignore')) 

# Url
urls = soup.findAll("li", attrs = {'class':"clear"})
print len(urls)
for url in urls:
  u = str(url.find("a")['href'])
  print u
  
# Author and comments are specified within the links, cannot be accessed from archive page
# So this part of code visits links of the posts to get author and comment info
# Author is the same for every post
authors = []
comments = []
for i in range(25):
  openlink = urllib2.urlopen(l[i])
  soup = BeautifulSoup(openlink.read())
  soup.prettify()
  author = soup.findAll("div", attrs = {'class': "single-post-meta"})
  authors.append(author)
  comment = soup.findAll("div", attrs = {'class':"comment-number clear"})
  comments.append(comment[0])       # using the attribute name didn't work well, the comment was the first attribute
  time.sleep(3)


# Getting most recent 25 posts  
for i in range(25):
  pages = range (1,26)
  page = pages[i]
  date = dates[i]
  d = clean_html(str(date.find("span")))
  title = titles[i]
  t = clean_html(title.find("a")['title'])[18::]
  t = t.encode('ascii', 'ignore')
  post = posts[i]
  p = clean_html(str(post.find("a")['rel']))
  if p == "[u'bookmark']":   			# assigned as post (boolean gives 1) if its a bookmark
    post = 1
  else:
    post = 0  
  url = urls[i]
  u = str(url.find("a")['href'])
  author = str(authors[i])
  a = clean_html(str(author)) # i get more than the author info here but this was what i could get so far
  comment = comments[i]
  c = clean_html(str(comment.find("span")))
  csvwriter.writerow([page, post, d, u, t, a, c])

readFile.flush()
readFile.close()