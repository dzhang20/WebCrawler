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
## Statistics
Page# | #1 | #2 | #3 | #4 | #5 | #6 | #7 | #8 | #9 | #10 
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- 
len(todo)/len(done) | 45.0 | 41.0 | 41.3 | 37.8 | 32.2 | 41.7 | 39.1 | 40.2 | 43.3 | 45.1 
crawl time | 0.13563895225524902 | 0.06535601615905762 | 0.07764625549316406 | 0.34067296981811523 | 0.2562441825866699 | 0.8546497821807861 | 0.22416400909423828 | 0.2243959903717041 | 0.21695303916931152 | 0.21660900115966797 
## Conclusion
For constructing a efficient and useful search engine, web crawler need to be very fast to crawl large number of pages, detect possible loops and filter out "bad" urls(some href tag may contain invalid url or just relative path on the server). Better result returned by the web Crawler to the database will imporve the total performance as well.