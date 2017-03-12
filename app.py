from flask import Flask, render_template, request # We will want to create a pretty html view on our own so render_template and request need to be imported
import json # I have included json from scraper.py
import urllib2 # I have included urllib2 from scraper.py
from bs4 import BeautifulSoup # I have included BeautifulSoup from scraper.py
app = Flask(__name__) # Create an instance of flask.

def gethnfrontpage(): # I have pasted the function from scraper.py and removed the line print gethnfrontpage(). We will be instead sending the output of the function to flask
    response = urllib2.urlopen("https://news.ycombinator.com/news")
    stories = []
    soup = BeautifulSoup(response, "html.parser")
    posts = soup.select(".storylink")
    for post in posts:
        #title = post.text
        #link = post["href"]
        stories.append({"title":post.text, "link":post["href"]})
    return json.dumps(stories)

@app.route('/') # The root directory of the site.
def get_hn(): # The function to generate content
    frontpage = gethnfrontpage() # Running the gethnfrontpage function
    return render_template("hn.html", hn=json.loads(frontpage)) # Outputting the json from gethnfrontpage to a file named hn.html

if __name__ == '__main__':
    app.run(port=5000, debug=True)
# We are telling the script to run on localhost port 5000 and in debug mode to show error messages.
