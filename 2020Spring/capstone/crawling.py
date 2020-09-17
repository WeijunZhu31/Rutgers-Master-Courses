import re
import time
from lxml import etree
import requests
# from fake_useragent import UserAgent
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support import expected_conditions

label = input("Which label of news do you want to crawl: ")
url = "https://www.foxnews.com/" + label

# selenium
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url)
driver.maximize_window()
html = driver.page_source
# Set 3 seconds to close some overlay windows
time.sleep(3)


def get_source():
    # Load more of the web page
    j = 0
    for i in range(0, 270):
        j += 1
        # driver.find_element_by_xpath('//div[@class="button load-more js-load-more"]/a[@href="#"]').click()
        driver.find_element_by_xpath('(//div[@class="button load-more js-load-more"]/a[@href="#"])[1]').click()  # select the 1st element
        if j <= 200:
            time.sleep(1.5)
        elif 200 < j <= 500:
            time.sleep(3)
        elif 500 < j < 1500:
            time.sleep(3.5)
        else:
            time.sleep(3.5)
        # Do not forget set new html object!
        print(j)

    html = driver.page_source

    # lxml
    e = etree.HTML(html)

    # Get Title
    Title = e.xpath("//h4/a/text()")
    # print(Title)
    # print(len(Title))
    # Delete the repetitive title
    print('length of data: ', len(list(set(Title))))

    # Get Contents' links
    Content_url = e.xpath('//h4/a/@href')

    # Merge Content and Title_url into a zip object
    storage = zip(Title, Content_url)

    # add https://www.foxnews.com/ to get whole link of the articles
    title_list = []
    url_list = []
    for title, url in storage:
        title_list.append(title)
        url = str(url)
        if url.startswith(r"/"+label+r"/"):
            temp = "https://www.foxnews.com"
            url = temp + url
            url_list.append(url)
        else:
            url_list.append(url)

    # Set title and its url into dict
    storage = list(zip(title_list, url_list))
    # print(storage)

    # Close the window
    driver.quit()

    # Delete the urls of the videos link
    title_list = []
    url_list = []
    for element in storage:
        if element[1].startswith("https://www.foxnews.com"):
            title_list.append(element[0])
            url_list.append(element[1])

    storage = dict(zip(title_list, url_list))
    print("the length of the data after deleting videos", len(storage))
    print(storage)

    return storage


# Store contents of each link with a new txt file
def store_content(storage01, label):
    i = 0
    for url in storage01.values():
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        html = driver.page_source
        e = etree.HTML(html)
        # extract the content from html resource
        contents = e.xpath('//div[@class="article-body"]/p/text() | //div[@class="article-body"]/p/a/text()')
        # print(contents)
        # contents is list, we need to change list to string
        contents = ",".join(contents)
        # Then we need to remove the \xa0 in the content
        contents = contents.replace(r"\xa0", r"")
        # open one txt file, and store the contents inside
        with open(r'content/'+label+r'/{}.txt'.format(i), 'w', encoding='utf-8') as f:
            f.write(contents)

        driver.quit()
        print(i)  # the number of the page that you store
        i += 1


if __name__ == "__main__":
    storage01 = get_source()
    # store_content(storage01, label)

