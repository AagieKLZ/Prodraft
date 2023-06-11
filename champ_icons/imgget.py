import requests

Champions=['Aatrox','Ahri','Akali','Alistar','Amumu','Anivia','Annie','Aphelios','Ashe','Aurelion Sol','Azir','Blitzcrank','Brand','Braum','Caitlyn','Camille','Cassiopeia','ChoGath','Corki','Darius','Diana','Dr Mundo','Draven','Ekko','Elise','Evelynn','Ezreal','Fiddlesticks','Fiora','Fizz','Galio','Gangplank','Garen','Gnar','Gragas','Graves','Hecarim','Heimerdinger','Illaoi','Irelia','Ivern','Janna','Jarvan IV','Jax','Jayce','Jhin','Jinx','KaiSa','Kalista','Karma','Karthus','Kassadin','Katarina','Kayle','Kayn','Kennen','KhaZix','Kindred','Kled','KogMaw','LeBlanc','Lee Sin','Leona','Lillia','Lissandra','Lucian','Lulu','Lux','Malphite','Malzahar','Maokai','Master Yi','Miss Fortune','Mordekaiser','Morgana','Nami','Nasus','Nautilus','Neeko','Nidalee','Nocturne','Nunu','Olaf','Orianna','Ornn','Pantheon','Poppy','Pyke','Qiyana','Quinn','Rakan','Rammus','RekSai','Renekton','Rengar','Riven','Rumble','Ryze','Samira','Sejuani','Senna','Seraphine','Sett','Shaco','Shen','Shyvana','Singed','Sion','Sivir','Skarner','Sona','Soraka','Swain','Sylas','Syndra','Tahm Kench','Taliyah','Talon','Taric','Teemo','Thresh','Tristana','Trundle','Tryndamere','Twisted Fate','Twitch','Udyr','Urgot','Varus','Vayne','Veigar','VelKoz','Vi','Viktor','Vladimir','Volibear','Warwick','Wukong','Xayah','Xerath','Xin Zhao','Yasuo','Yone','Yorick','Yuumi','Zac','Zed','Ziggs','Zilean','Zoe','Zyra']

for i in range(0,len(Champions)):
	FileName=Champions[i]+'.png'
	pic_url='http://ddragon.leagueoflegends.com/cdn/10.15.1/img/champion/'+Champions[i]+'.png'
	img_data = requests.get(pic_url).content
	with open(FileName, 'wb') as handler:
		handler.write(img_data)

