"""
This file is for when the crawling.py gets error or stops
by some reasons, and I will use this file to continue crawling the data.
"""
from lxml import etree
from selenium import webdriver


def store_content(storage01, label):
    i = index
    for url in storage01:
        # driver = webdriver.Chrome(executable_path='./chromedriver.exe')
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
        with open(r'content/' + label + r'/{}.txt'.format(i), 'w', encoding='utf-8') as f:
            f.write(contents)

        driver.quit()
        print(i)  # the number of the page that you store
        i += 1


def store_date(storage01, label):
    i = index
    for url in storage01:
        driver = webdriver.Chrome()
        driver.get(url)
        # driver.maximize_window()
        html = driver.page_source
        e = etree.HTML(html)
        # extract the data from html resource
        date = e.xpath('//time/text()')
        # print(contents)
        # contents is list, we need to change list to string
        date = ",".join(date)
        # Then we need to remove the \xa0 in the content
        date = date.replace(r"\xa0", r"")
        # open one txt file, and store the contents inside
        with open(r'news_date/' + label + r'/{}.txt'.format(i), 'w', encoding='utf-8') as f:
            f.write(date)

        driver.quit()
        print(i)  # the number of the page that you store
        i += 1


if __name__ == "__main__":
    ###############################################################
    label = input("which label do you want to crawl: ")
    with open(r"news_link/{}.txt".format(label), "r", encoding="utf-8") as f:
        # Read the txt flies, and ignore the line-feed.
        raw_content = f.read().splitlines()
    for line in raw_content:
        # Delete the \ in the dict
        storage01 = line.strip('\\')

    # Extract the link from dict, and save into a listpo
    storage01 = list(eval(storage01).values())
    # print(storage01)

    ###### Set the index which we should start at #######
    index = int(input("which index do you want to start (start at 0): "))
    ################################################
    storage01 = storage01[index:]
    # check the index we start!!!
    # print(storage01)
    ################################################################

    ###### Start to store_content  ######
    # store_content(storage01, label)
    ###### Start to store_date  ######
    store_date(storage01, label)
