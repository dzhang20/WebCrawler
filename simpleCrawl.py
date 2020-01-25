import requests
import sys
import time
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
todo_lst = []
done_lst = []
crawl_speed = []
url_ratio = []
def web(page,WebUrl):
    todo_lst.append(WebUrl)

    while(page>0):
        #process the first url in todo list
        if len(todo_lst) == 0:
            break
        start_time = time.time()
        url = todo_lst.pop(0)
        http = httplib2.Http()
        # code = requests.get(url)
        #save the plain text of website into database?
        # plain = code.text
        status, response = http.request(url)
        # s = BeautifulSoup(plain, "html.parser")
        #search through the website for all the links and their description
        for link in BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('a')):
           # print(link)
            # title = link.get('title')
            # print(title)
            # new_url = link.get('href')
            # print(new_url)
            #maybe filter the url based on domain?
            #loop detection
            if link.has_attr('href'):
                new_url = link['href']
                
                if new_url in done_lst:
                    continue
                if "www" in new_url:
                    todo_lst.append(new_url)
                    print(new_url)

        done_lst.append(url)
        crawl_speed.append(time.time() - start_time)
        url_ratio.append(len(todo_lst)/len(done_lst))
        page = page - 1

        
#Starting URL: argv[1]
web(sys.argv[1],sys.argv[2])

for speed in crawl_speed:
    print(speed)
for url in url_ratio:
    print(url)
