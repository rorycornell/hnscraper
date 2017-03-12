
import json # We will be using json to output the data from the website
import urllib2 # The library that accesses the internet and downloads the webpage data
from bs4 import BeautifulSoup # The library that searches the webpage data for html tags

def gethnfrontpage():  # A python function to return the stories off of the front page
   response = urllib2.urlopen("https://news.ycombinator.com/news") # urllib2 opens the website address and downloads the html
   stories = [] # An empty list of stories that will be filled once BeautifulSoup locates them
   soup = BeautifulSoup(response, "html.parser") # Tell BeautifulSoup to read the html that was downloaded by urllib2
   posts = soup.select(".storylink")
   '''
   Tell BeautifulSoup to select the html tag with the class storylink.
   I determined the html tag of the news.ycombinator links by viewing the source of the webpage.
   Here is a link that I pulled off of the page to use as an example. Notice the html class?
   <a href="https://www.nytimes.com/2017/03/10/opinion/sunday/can-sleep-deprivation-cure-depression.html" class="storylink">Can sleep deprivation cure depression?</a>
   '''
   for post in posts: # Now that the posts have been found by BeautifulSoup, they can now be outputted as json.
       stories.append({"title":post.text, "link":post["href"]}) # The post title as well as the link to the post will be included in the list of stories that we created earlier.
   return json.dumps(stories) # The function that we created returns the stories as json which will make them easy for us to display later.


print gethnfrontpage() # We can temporarily output the function to our terminal window to make sure that it works.
