# Import library
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# Create Spider class
class newsToScrape(CrawlSpider):
    # Name of spider
    name = 'newsi'
    # Website you want to scrape
    allowed_domains = ["reuters.com"]
    start_urls = [
        'https://www.reuters.com/'
    ]
    rules = (
        Rule(LinkExtractor(allow='https://www.reuters.com/'), callback="parse_item", follow=True),
    )
    def parse_item(self, response):
        fullText=""
        if(response.xpath("//meta[@property='og:type']/@content").get().lower() == "article"):
            if(("corona" in response.xpath("//meta[@name='article:tag']/@content").get().lower() ) or ("covid" in response.xpath("//meta[@name='article:tag']/@content").get().lower()) or
               ("corona" in response.xpath("//meta[@property='og:title']/@content").get().lower()) or ("covid" in response.xpath("//meta[@property='og:title']/@content").get().lower())):
                for paragraph in response.css("p.Text__text___3eVx1j.Text__dark-grey___AS2I_p.Text__regular___Bh17t-.Text__large___1i0u1F.Body__base___25kqPt.Body__large_body___3g04wK.ArticleBody__element___3UrnEs::text").getall():
                    if(paragraph != ""):
                        fullText = fullText + paragraph
                yield dict(link=response.url,
                        author=response.css("a.AuthorName__author___1tcHiY::text").getall(),
                        datum=response.css("span.DateLine__date___12trWy::text").get(),
                        text=fullText.replace('Our Standards: ', ""))

