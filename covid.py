import scrapy

class CovidWebCrawler1(scrapy.Spider):
	name='slifer'
	start_urls=['https://www.mygov.in/corona-data/covid19-statewise-status']

	def parse(self,response):
		site=response.url
		w=response.css('div.field-name-field-select-state')
		x=response.css('div.field-name-field-total-confirmed-indians')
		y=response.css('div.field-name-field-cured')
		z=response.css('div.field-name-field-deaths')
		for i in range(len(x)):
			yield{
			'State Name':w[i].css('div.field-item::text').get(),
			'Confirmed':x[i].css('div.field-item::text').get(),
			'Cured/Discharged/Migrated':y[i].css('div.field-item::text').get(),
			'Death':z[i].css('div.field-item::text').get()
			}

class CovidWebCrawler2(scrapy.Spider):
	name='blackmagician'
	start_urls=['https://www.mygov.in/covid-19/']

	def parse(self,response):
		for item in response.css("div.mygov_champions_area"):
			yield {
			'active cases':item.css('div.active-case div.iblock_text span.icount::text').get(),
			'Cured/Discharged':item.css('div.discharge div.iblock_text span.icount::text').get(),
			'Deaths':item.css('div.death_case div.iblock_text span.icount::text').get(),
			'Migrated':item.css('div.migared_case div.iblock_text span.icount::text').get()
			}

class CovidWebCrawler3(scrapy.Spider):
	name='python'
	start_urls=['https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/']

	def parse(self,response):	
		a=response.css('tbody tr')
		for i in range(len(a)):
			c=a[i].css("td::text").getall()		
			yield{
			'Country':c[0],
			'No of Cases':c[1],
			'No of Deaths':c[2]
			}


