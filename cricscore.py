from gi.repository import Notify
import requests,time
from bs4 import BeautifulSoup
url='http://www.espncricinfo.com/ci/engine/match/index.html?view=live'
while True:
	web=requests.get(url)
	bs=BeautifulSoup(web.content,'html.parser')
	inn1=bs.find_all('div',{'class':'innings-info-1'})[0].text
	inn2=bs.find_all('div',{'class':'innings-info-2'})[0].text
	status=bs.find_all('div',{'class':'match-status'})[0].text
	info = inn1+inn2+status
	match='Live Score'
	Notify.init('Cricket Updates')
	notification=Notify.Notification.new(match,info)
	notification.show()
	time.sleep(120)
