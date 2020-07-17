from bs4 import BeautifulSoup
import requests
import json
import csv

source = requests.get('https://champion.gg/statistics/').text


soup = BeautifulSoup(source, 'lxml')

stats = soup.find_all('script')
for s in stats:
    if s.string and "matchupData.stats" in s.string:
        target = s.string.strip().split(" = ")[1][:-1]        
x = json.loads(target)

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Champion', 'Role', 'Win Percent', 'Play Percent', 'Ban Rate', 'Kills', 'Deaths',
 'Assists', 'Largest Killing Spree', 'Damage Dealt', 'Damage Taken', 'Total Healing', 'Minions Killed', 'Gold Earned'])

for i in x:
	title = i['title']
	role = i['role']
	winPercent = i['general']['winPercent']
	playPercent = i['general']['playPercent']
	banRate = i['general']['banRate']
	kills = i['general']['kills']
	deaths = i['general']['deaths']
	assists = i['general']['assists']
	largestKillingSpree = i['general']['largestKillingSpree']
	damageDealt = i['general']['totalDamageDealtToChampions']
	damageTaken = i['general']['totalDamageTaken']
	health = i['general']['totalHeal']
	minionsKilled = i['general']['minionsKilled']
	goldEarned = i['general']['goldEarned']
	csv_writer.writerow([title, role, winPercent, playPercent, banRate, kills, deaths, assists, largestKillingSpree,
		damageDealt, damageTaken, health, minionsKilled, goldEarned])







