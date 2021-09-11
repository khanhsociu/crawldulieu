from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from quotes.items import QuotesItem

class MySpider(BaseSpider):
    name = "quotes"
    allowed_domains = ["vietnamworks.com"]
    start_urls = ["https://www.vietnamworks.com/full-stack-developer-kv","https://www.vietnamworks.com/full-stack-developer-kv/page-2"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//div[@class='row m-0']")
        items = []
        for titles in titles:
            item = CraigslistSampleItem()
            item["title"] = titles.select("a/text()").extract()
            item["link"] = titles.select("a/@href").extract()
            items.append(item)
        return items