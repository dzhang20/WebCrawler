# WebCrawler
## CS 6675 Project1
A Simple Web Crawler Program using BeautifulSoup

## Usage
> $python simpleCrawl.py {number_of_page_to_crawl} {seed_url(absolute url)}


E.X.
> $python simpleCrawl.py 1000 https://www.amazon.com
## Pros 
- Simple build and easy to use
- fast to crawl small number of websites
## Cons
- Did not implement parallelization(performance not good for crawling large amount of website)
- Did not implement filter and classification of websites (invalid url may still be valid to process)
## Statistic
Page# | #1 | #2 | #3 | #4 | #5 | #6 | #7 | #8 | #9 | #10 
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- 
len(todo)/len(done) | 45.0 | 41.0 | 41.3 | 37.8 | 32.2 | 41.7 | 39.1 | 40.2 | 43.3 | 45.1 
## Conclusion
For constructing a efficient and useful search engine, web crawler need to be very fast to crawl large number of pages, detect possible loops and filter out "bad" urls(some href tag may contain invalid url or just relative path on the server). Better result returned by the web Crawler to the database will imporve the total performance as well.