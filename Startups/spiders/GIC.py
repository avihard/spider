import json
import scrapy

file='C:/Users/rajkot/Desktop/Startup_Stem_Main/startup_stem/gic_data.txt'

def save(reg):
	global file
	with open(file,'w') as od:
		json.dump(reg,od)

class EventSpider(scrapy.Spider):
	name = "gic"

	def start_requests(self):
		urls = [
		'http://gtuinnovationcouncil.ac.in/upcoming-event-list/'
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		date=[]
		link=[]
		name=[]
		zone=[]
		
		date = response.xpath('''//div[@id="page"]/div[@class="site-main"]//div[@id="main-content"]/div[@class="block-content"]/div/div/div/article[@id="post-577"]/div/div/table/tbody/tr/td[@data-title="Date"]/text()''').extract() 
		link = response.xpath('''//div[@id="page"]/div[@class="site-main"]//div[@id="main-content"]/div[@class="block-content"]/div/div/div/article[@id="post-577"]/div/div/table/tbody/tr/td[@data-title="Event"]/a/@href''').getall()
		name = response.xpath('''//div[@id="page"]/div[@class="site-main"]//div[@id="main-content"]/div[@class="block-content"]/div/div/div/article[@id="post-577"]/div/div/table/tbody/tr/td[@data-title="Event"]/a/text()''').extract()
		zone = response.xpath('''//div[@id="page"]/div[@class="site-main"]//div[@id="main-content"]/div[@class="block-content"]/div/div/div/article[@id="post-577"]/div/div/table/tbody/tr/td[@data-title="Zone"]/text()''').extract()
		
		reg = []
		for d,l,n,z in zip(date,link,name,zone):
			reg.append((d,l,n,z))
		print(reg)
		print('reg length is --> ', len(reg))
		save(reg)


	#	filename = 'gic.html'
	#	with open(filename,'wb') as f:
	#		f.write(response.body)
	#	self.log('Saved file %s' %filename)


	#    response.xpath('''//div[@id="page"]/div[@class="site-main"]//div[@id="main-content"]/div[@class="block-content"]/div/div/div/article[@id="post-577"]/div/div/table/tbody/tr/td''').getall()