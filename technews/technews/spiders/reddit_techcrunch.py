# -*- coding: utf-8 -*-
import scrapy


class RedditTechcrunchSpider(scrapy.Spider):
    name = "reddit-techcrunch"
    allowed_domains = ["https://www.reddit.com/", "https://www.techcrunch.com/" ]
    start_urls = ['https://www.reddit.com/search?q=site%3Atechcrunch.com/']

    def parse(self, response):

        reddit_links = response.css("div.search-result")
        for reddit_link in reddit_links:
            #search_result_header = reddit_link.xpath('//header[@class="search-result-header"]')
            #search_result_meta = reddit_link.xpath('//div[@class="search-result-meta"]')
            #search_result_footer = reddit_link.xpath('//div[@class="search-result-footer"]')

            search_result_title = reddit_link.css('a.search-title::text').extract_first()
            search_result_link = reddit_link.css('a.search-link::attr(href)').extract_first()
            yield {'URL': search_result_link , 'Title': search_result_title }


