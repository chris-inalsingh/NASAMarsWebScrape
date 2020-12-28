import requests
import json 
from bs4 import BeautifulSoup as bs
import splinter 
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape_all():
    executable_path = {'executable_path' : 'chromedriver.exe'}
    return splinter.Browser('chrome', **executable_path, headless=False)





#Title and body text web scrape
def scrape():
    browser = scrape_all()

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    content = soup.find("div", class_='content_page')
    titles = content.find_all("div", class_='content_title')
    title_text = titles[0].text.strip()

    article = content.find_all("div", class_='article_teaser_body')
    article_text = article_text[0].text

    #IMG Webscrape
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html

    soup = bs(html, 'html.parser')
    featured_image = soup.find("article", class_='carousel_item')['style']

    latter = featured_image.split('/spaceimages/')[1].split("'")[0]

    former = url.split('?')[0]

    final_url = former + latter

    browser.find_by_id("full_image").click()

    browser.find_by_text("more info     ").click()

    html = browser.html
    soup = bs(html, 'html.parser')
    featured_img = soup.find("img", class_='main_image')['src']
    featured_img


    pic_url = f"https://www.jpl.nasa.gov{featured_img}"
    pic_url


    #Mars Weather Facts
    url = 'https://space-facts.com/mars/'
    browser.visit(url)

    Facts = pd.read_html(url)
    fact_df = Facts[0]
    fact_df.columns = ["Facts", "Fact Value"]
    fact_df

    fact_html = fact_df.to_html()
    fact_html

    ##Mars Hemispheres
    #Cerberus Hemisphere
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    html = browser.html

    soup = bs(html, 'html.parser')
    cerb_image = soup.find_all("div", class_='wide-image-wrapper')
    
    for key in cerb_image:
        img = key.find('li')
        cerb_img_link = img.find('a')['href']
    cerb_title = soup.find('h2', class_='title').text
    cerb_dict = {"Title": cerb_title, "img_url": cerb_img_link}
    cerb_dict

    #Schiaparelli Hemisphere
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)
    html = browser.html

    soup = bs(html, 'html.parser')
    schi_image = soup.find_all("div", class_='wide-image-wrapper')
    print(schi_image)

    for key in schi_image:
        img = key.find('li')
        schi_img_link = img.find('a')['href']
    schi_title = soup.find('h2', class_='title').text
    schi_dict = {"Title": schi_title, "img_url": schi_img_link}
    schi_dict

    #Syrtis Hemisphere
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)
    html = browser.html

    soup = bs(html, 'html.parser')
    syr_image = soup.find_all("div", class_='wide-image-wrapper')
    print(syr_image)

    for key in syr_image:
        img = key.find('li')
        syr_img_link = img.find('a')['href']
    syr_title = soup.find('h2', class_='title').text
    syr_dict = {"Title": syr_title, "img_url": syr_img_link}
    syr_dict


    #Valles Hemisphere
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    html = browser.html

    soup = bs(html, 'html.parser')
    val_image = soup.find_all("div", class_='wide-image-wrapper')
    print(val_image)

    for key in val_image:
        img = key.find('li')
        val_img_link = img.find('a')['href']
    val_title = soup.find('h2', class_='title').text
    val_dict = {"Title": val_title, "img_url": val_img_link}
    val_dict

    #Hemisphere Dictionary
    hemisphere_image_urls = cerb_dict, schi_dict, syr_dict, val_dict
    hemisphere_image_urls

    #adding python dictionary
    mars={}
    mars["title_text"]=title_text
    mars["article_text"]=article_text
    mars["pic_url"]=pic_url
    mars["mars_fact"]=fact_html
    mars["hemisphere_image_urls"]=hemisphere_image_urls
    
    browser.quit()

    return mars




