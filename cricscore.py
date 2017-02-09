from gi.repository import Notify
import requests,time
from bs4 import BeautifulSoup
url='http://www.espncricinfo.com/ci/engine/match/index.html?view=live'
url2='http://www.espncricinfo.com/india-v-bangladesh-2016-17/engine/match/1041761.html'
web=requests.get(url)
web2=requests.get(url2)
while True:
	bs=BeautifulSoup(web.content,'html.parser')
	bs2=BeautifulSoup(web2.content,'html.parser')
	inn1=bs.find_all('div',{'class':'innings-info-1'})[0].text
	inn2=bs.find_all('div',{'class':'innings-info-2'})[0].text
	status=bs.find_all('div',{'class':'match-status'})[0].text
	info = inn1+inn2+status
	team1=bs2.find_all('div',{'class':'team-1-name'})[0].text
	team2=bs2.find_all('div',{'class':'team-2-name'})[0].text
	match=team1+' vs '+team2
	Notify.init('Cricket Updates')
	notification=Notify.Notification.new(match,info)
	notification.show()
	time.sleep(120)