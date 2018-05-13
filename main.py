from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

page_nmu = 59

while True:
    url = 'https://tabelog.com/tw/tokyo/rstLst/'+ str(page_nmu) +'/?SrtT=rt'
    print(url)

    page_nmu = page_nmu + 1

    try:
        response = urlopen(url)
    except HTTPError:
        print('done')
        break


    html = BeautifulSoup(response)
    # print(html)

    total_list = html.find('ul', {
        'id': 'js-map-search-result-list'
    })
    shop_list = total_list.find_all('li', {
        'class': ['list-rst', 'js-list-item']
    })

    for shop in shop_list:
        blog_url =  shop.find('a')['href']
        en_name = shop.find('a').contents[0]
        ja_name = shop.find('small', {
            'class': 'list-rst__name-ja'
        }).contents[0]
        rating = shop.find('b', {
            'class': 'c-rating__val'
        }).contents[0]
        # url = blog_url + '#anchor-rd-detail'
        # response = urlopen(url)
        # html = BeautifulSoup(response)
        # table = html.find('table', {'class': ['c-table', 'rd-detail-info']})
        # cat = table.find('span', {'property': 'v:category'}).contents[0]
        # print(ja_name, en_name, rating, cat, blog_url)


        print(ja_name, en_name, rating, blog_url)

#print(shop_list)

