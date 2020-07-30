import scrapy


class PythonWeeklySpider(scrapy.Spider):
    name = 'python_weekly'
    # allowed_domains = ['github.com']
    start_urls = ['https://github.com/PyChina/weekly/tree/master/content/python-weekly/']

    def parse(self, response):
        article_links = response.css('a[title^="issue"]::attr(href)').getall()
        preffix = 'https://github.com/PyChina/weekly/raw/master/content/python-weekly/'
        self.log(f'{len(article_links)} articles found.')
        for link in article_links:
            url = preffix + link.split('/')[-1]
            print(url)
            yield scrapy.Request(url, callback=self.dowload_file)
        # yield from response.follow_all(article_links, self.parse_article)

    def parse_article(self, response):
        title = response.css('#readme h3::text').re_first(r'.*?(\d+).*')
        h3_list = response.css('#readme h3')
        with open(f'{title}.txt', 'w', encoding='utf-8') as f:
            for cnt, h3 in enumerate(h3_list, start=1):
                temp = h3.xpath(f'./following-sibling::node()[count(preceding-sibling::h3)={cnt}]')
                f.write((''.join(temp.xpath('./descendant-or-self::text()').getall()).strip()))
        self.log('Saved file %s' % title)
    
    def dowload_file(self, response):
        title = response.url.split('/')[-1]
        with open(f'{title}', 'w', encoding='utf-8') as f:
            f.write(response.body.decode('utf-8'))


class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    subtitles = scrapy.Field()
