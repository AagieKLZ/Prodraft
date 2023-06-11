import requests

ChampName="wukong"
ChampFile="Wukong"

FileName=ChampFile+'.png'
pic_url='http://ddragon.leagueoflegends.com/cdn/8.10.1/img/champion/'+ChampName+'.png'
img_data = requests.get(pic_url).content
with open(FileName, 'wb') as handler:
	handler.write(img_data)
