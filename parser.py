import telebot
from telebot.types import Message
import requests
import urllib.request
from bs4 import BeautifulSoup

s = {}
new = {}
r = requests.get('http://ejudge.cfuv.ru/2018/I_semestr/standings/results_365.php')
content = r.text
soup = BeautifulSoup(content, "html.parser")

def parse():
	for tr in soup.find_all('tr'):
		for td in tr.find_all('td', { "bgcolor" : "#99cc99"}):
			k = td['title']
			if k not in s:
				num = td.string
				num = num[len(num) - 1]
				if num == '\xa0':
					num = '0'
				s[k] = num
				new[k] = num
parse()

token = '761658816:AAGGPOxG3taLfJ6cVw7nOE03l-zVECCYwwU'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['rec'])
def command_handler(message: Message):
	parse()
	ans = ''
	for i in new:
		ans += i + ' ' + s[i] + '\n'
	bot.reply_to(message, ans)
bot.polling(timeout=60)