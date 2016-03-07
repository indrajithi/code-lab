from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem

class MySpider(CrawlSpider):
    name = "craigs"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["https://stackoverflow.com/questions/"]

    rules = (
        Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath('//span[@class="pl"]')
        items = []
        for titles in titles:
            item = CraigslistSampleItem()
            item["title"] = titles.xpath("a/text()").extract()
            item["link"] = titles.xpath("a/@href").extract()
            items.append(item)
        return(items)
