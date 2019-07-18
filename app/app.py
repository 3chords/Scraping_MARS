# lines 2,3,5 created first
from flask import Flask, render_template
from flask_pymongo import PyMongo
# bring in the python file 'scrape_mars'
import scrape_mars

# created 2nd
app = Flask(__name__)


# use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# created 4th
# define our routes, this one for our html index page
@app.route("/")
def index():

    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars) 

# created 5th but we don't code it out it's just a placeholder 
# this is the route where we do our scrape
@app.route("/scrape")
# created 6th, here is our scrape function
def scrape():
    # created 6th, the mars_data variable will hold the function scrape_all from
    # the file scrape_mars.py (see the file scrape_mars.py for step #7)
    mars = mongo.db.mars
    get_mars_data = scrape_mars.scrape_info()
    mars.update({}, get_mars_data, upsert=True)
    return "Site has been scraped!"

# created 3rd (this always bookends the code)
if __name__ == "__main__":
    app.run()

# Read this first:
# So that I have documentation about how to re-create this, I've included the steps and the lines
# associated with the steps. The comments are down here so they don't mess up the steps & lines! 