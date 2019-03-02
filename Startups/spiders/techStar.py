import json
import scrapy

file='C:/Users/rajkot/Desktop/Startup_Stem_Main/startup_stem/techStar_data.txt'

def save(reg):
	global file
	with open(file,'w') as od:
		json.dump(reg,od)

class EventSpider(scrapy.Spider):
	name = "tech"

	def start_requests(self):
		urls = [
		'http://www.techstars.com/events/'
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		date=[]
		link=[]
		name=[]
		zone=['various Temecula, CA USA',
			   ' ',
			   '310 S Harrington Street, NC USA',
			   'various Temecula, CA USA',
			   'Moonshine grill, 303 Red River St. Austin, TX, USA',
			   'We work, 1900 Market, Philadelphia, USA',
			   ' ',
			   '800 Wilshire Boulevard LA USA',
			   'Croedcast USA',
			   'Tavern 29, 47 E 29th st. NY USA'	
		]
		
		date = response.css("span.tribe-event-date-start::text").extract()
		link = response.css("h2.tribe-events-list-event-title a::attr(href)").extract()
		roz = response.css("a.tribe-event-url::text").extract()
		for i in range(len(roz)):
			we = roz[i].strip(' \n\t')
			name.append(we.strip())
	#	zone = response.xpath('''//div[@id="page"]/div[@class="site-main"]//div[@id="main-content"]/div[@class="block-content"]/div/div/div/article[@id="post-577"]/div/div/table/tbody/tr/td[@data-title="Zone"]/text()''').extract()
		
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