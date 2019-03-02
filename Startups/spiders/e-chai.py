import scrapy
import numpy as np
import json
#from startup_stem import db

file='C:/Users/rajkot/Desktop/Startup_Stem_Main/startup_stem/e-chai_data.txt'

def save(reg):
	global file
	with open(file,'w') as od:
		json.dump(reg,od)


class EventSpider(scrapy.Spider):
	name = "e-chai"
	def start_requests(self):
		urls = [
		'https://echai.in/events/upcoming'
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		dom = "https://echai.in"
		date=[]
		link=[]
		name=[]
		zone=[]
		com = response.xpath("//div[@id='upcoming_events']/div[@class='panel panel-default']/div[@class='panel-body tbl-events']/div[@class='tbl-event']/div[@class='event-date']/div[2]/text()").getall() 
		for i in range(len(com)):
			we = com[i].strip(' \n')
			date.append(we.strip())	
		res = response.css("div.tbl-event__title a::attr(href)").extract()
		for i in range(len(res)): 
			link.append(dom + res[i])
		roz = response.css("a.calendar-event__link::text").getall()
		for i in range(len(roz)):
			we = roz[i].strip(' \n')
			name.append(we.strip())
		zone = response.xpath("//div[@id='upcoming_events']/div[@class='panel panel-default']/div[@class='panel-body tbl-events']/div[@class='tbl-event']/div[2]/div[3]/text()").extract()
		
		print(date)
		print(link)
		print(name)
		print(zone)		
		
		reg = []
		for d,l,n,z in zip(date,link,name,zone):
			reg.append((d,l,n,z))
		#print(reg)
		#print('reg length is --> ', len(reg))
		save(reg)
	
