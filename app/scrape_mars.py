# Created 8th, add the dependenies from the jupyter file 'mission_to_mars'
from splinter import Browser 
from bs4 import BeautifulSoup

# created 13th, call the function below and send the browser
news_title, news_paragraph = mars_news(browser)

# created 7th
def scrape_all:
    # created 9th, set up the browser, go to the jupyter file 'mission_to_mars' and pull in the code
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # created 9th
    data = {
        "news_title": news_title,
        <!-- I wasn't able to finish this section... just no time but it involves
        finding the outputs below and bringing them into the dictionary so we store it-->
    }

    # created 10th
    return data

# created 11th
def mars_news(browser):
    # created 14th, copy the code from the jupyter notebook 'mission_to_mars' and paste below
    # note, I pasted just the code that produced results and omitted the checkpoints along the way

# code paste from jupyter notebook begins here
    # Get the NASA Mars News
    # point the path to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    # set up the browser, specify chrome, the double asterisk are kwargs (key word arguments)
    browser = Browser('chrome', **executable_path, headless=False)
    # get NASA Mars news url
    url = 'https://mars.nasa.gov/news/'
    # open the site in the browser
    browser.visit(url)
    # pass wait time for css element to load
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=2)
    # use splinter to parse the html
    html = browser.html
    # put the html into beautifulsoup
    news_soup = BeautifulSoup(html, 'html.parser')
    # get the slide element using beautifulsoup
    slide_elem = news_soup.select_one('ul.item_list li.slide')
    # parse through the results
    slide_elem.find('div', class_="content_title")
    # get the news title
    news_title = slide_elem.find('div', class_="content_title").get_text()
    # pull the paragraph
    news_p = slide_elem.find('div', class_="article_teaser_body").text

    # JPL Space Images, get the featured image
    # get the url, using the same session as above
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    # visit the page
    browser.visit(url)
    # click the first link
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    browser.is_element_present_by_text('more info     ', wait_time=2)
    # it turns out to get the photo we need to click the 'more info' button
    more_info_elem = browser.find_link_by_partial_text('more info')
    # click the 'more info' button
    more_info_elem.click()
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    # get the image by drilling down into the class figure.lede, then an anchor (a) and then the image (img)
    # get("src") is the source link of the photo
    img_url_rel_path = img_soup.select_one('figure.lede a img').get("src")
    # make an img url by appending the beginning to it
    img_url = f'https://www.jpl.nasa.gov{img_url_rel_path}'

    # Visit the Mars twitter account and scrape the latest Mars weather tweet from the page
    # save the tweet text for the weather report as a variable called mars_weather
    url = 'https://twitter.com/marswxreport?lang=en'
    # visit the page
    browser.visit(url)
    # get HTML from page
    html = browser.html
    tweet_soup = BeautifulSoup(html, 'html.parser')
    # parse through the results
    tweet_soup.find(class_="TweetTextSize")
    # get the tweet's weather report, store it to a variable
    mars_weather = tweet_soup.find(class_="TweetTextSize").get_text()

    # Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet (mass, diameter, etc.)
    # use pandas to convert the data to a HTML table string
    
    # get dependency
    import pandas as pd

    # get the url
    url = 'https://space-facts.com/mars/'
    # use the read_html function in pandas to scrape tabular data
    mars_tables = pd.read_html(url)
    # Mars has data in the first and second table, pull in the first table in the list (item 0)
    mars_tbl1 = mars_tables[0]
    # pull in the columns
    mars_tbl1.columns=['Comparison', 'Mars', 'Earth']
    # generate an HTML table from the dataframe
    mars_tbl1_to_html_tbl = mars_tbl1.to_html()
    # strip out unwanted newlines from the code to clean up the table
    final_mars_tbl1 = mars_tbl1_to_html_tbl.replace('\n', '')
    # pull in the second table in the list (item 1)
    mars_tbl2 = mars_tables[1]
    # pull in the columns
    mars_tbl2.columns=['0', '1']
    # generate an HTML table from the dataframe
    mars_tbl2_to_html_tbl = mars_tbl2.to_html()
    # strip out unwanted newlines from the code to clean up the table
    final_mars_tbl2 = mars_tbl2_to_html_tbl.replace('\n', '')

    # visit the USGS astrogeology site to obtain high res images for each of Mars' hemispheres
    # save both the image & url for the full res hemisphere image and the hemisphere title containing the hemisphere name
    # use a python dictionary to store the data using the keys img_url and title
    # # append the dictionary with the image url string and the hemisphere title to a list, the list will contain one
    # dictionary for each hemisphere

    # get the url
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # visit the page
    browser.visit(url)
    html = browser.html
    hemi_soup = BeautifulSoup(html, 'html.parser')
    # create empty dictionary to store the image url and title
    hemisphere_image_urls = {}
    # create empty list 
    hi_list = []
 
    # get name, img, link of hemisphere 1
    # this section is anti-DRY but sometimes that the way it is... it needs a loop for sure
    h3_1 = browser.find_by_tag('h3')[0]
    h3_1 = h3_1.value
    # click the link #1
    browser.click_link_by_partial_text('cerberus_enhanced')
    # click the 'original' link to download high resolution image #1
    browser.click_link_by_partial_text('cerberus_enhanced.tif')
    # grab the url
    image_1_url = browser.url
    # append title and image path to dictionary
    hemisphere_image_urls = {"title": h3_1, "img_url": image_1_url}
    get_hemi_item = hemisphere_image_urls.items()
    # add to list
    hi_list.append(get_hemi_item)

    # get name, img, link of hemisphere 2
    # navigate back to the previous page
    browser.back()
    # get name of hemisphere #2
    h3_2 = browser.find_by_tag('h3')[1]
    h3_2 = h3_2.value
    # click the link #2
    browser.click_link_by_partial_text('schiaparelli_enhanced')
    # click the 'original' link to download the high resolution image #2
    browser.click_link_by_partial_text('schiaparelli_enhanced.tif')
    # grab the url
    image_2_url = browser.url
    # append title and image path to dictionary
    hemisphere_image_urls = {"title": h3_2, "img_url": image_2_url}
    get_hemi_item = hemisphere_image_urls.items()
    # add to list
    hi_list.append(get_hemi_item)

    # get name, img, link of hemisphere 3
    # navigate back to the previous page
    browser.back()
    # get name of hemisphere #3
    h3_3 = browser.find_by_tag('h3')[2]
    h3_3 = h3_3.value
    # click the link #3
    browser.click_link_by_partial_text('syrtis_major_enhanced')
    # click the 'original' link to download the high resolution image #3
    browser.click_link_by_partial_text('syrtis_major_enhanced.tif')
    # grab the url
    image_3_url = browser.url
    # append title and image path to dictionary
    hemisphere_image_urls = {"title": h3_3, "img_url": image_3_url}
    get_hemi_item = hemisphere_image_urls.items()
    # add to list
    hi_list.append(get_hemi_item)

    # get name, img, link of hemisphere 4
    # navigate back to the previous page
    browser.back()
    # get name of hemisphere #4
    h3_4 = browser.find_by_tag('h3')[3]
    h3_4 = h3_4.value
    # click the link #4
    browser.click_link_by_partial_text('valles_marineris_enhanced')
    # click the 'original' link to download the high resolution image #4
    browser.click_link_by_partial_text('valles_marineris_enhanced.tif')
    # grab the url
    image_4_url = browser.url
    # append title and image path to dictionary
    hemisphere_image_urls = {"title": h3_4, "img_url": image_4_url}
    get_hemi_item = hemisphere_image_urls.items()
    # add to list
    hi_list.append(get_hemi_item)
    # code paste from jupyter notebook ends here
    
    # created 11th
    return news_title, 
    # again not able to finish and flesh this out!! but close
    # I just need to include all the items to return that get sent to the
    # index.html file that populate the different bootstrap columns.
