import telebot, os, re
import logging as log
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

log.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s',
    filename= u'status.log')

wake_stop = telebot.types.InlineKeyboardMarkup(row_width=1)
but1 = telebot.types.InlineKeyboardButton(text="Rg-Bot", callback_data="3")
but2 = telebot.types.InlineKeyboardButton(text="Dh-Bot", callback_data="1")
but3 = telebot.types.InlineKeyboardButton(text="Mom-Bot", callback_data="2")
but4 = telebot.types.InlineKeyboardButton(text="Sleep-All", callback_data="sleep")
but5 = telebot.types.InlineKeyboardButton(text="Wake-All", callback_data="wake_all")
wake_stop.add(but1,but2,but3)
wake_stop.row(but4,but5)

rg_settings = telebot.types.InlineKeyboardMarkup(row_width=2)
back_wake_menu = telebot.types.InlineKeyboardButton(text="Back", callback_data="back_wake_menu")
b1 = telebot.types.InlineKeyboardButton(text="Wake", callback_data="wake_3")
b2 = telebot.types.InlineKeyboardButton(text="Stop", callback_data="stop_3")
rg_settings.add(b1,b2)
rg_settings.row(back_wake_menu)

dh_settings = telebot.types.InlineKeyboardMarkup(row_width=2)
a1 = telebot.types.InlineKeyboardButton(text="Wake", callback_data="wake_1")
a2 = telebot.types.InlineKeyboardButton(text="Stop", callback_data="stop_1")
dh_settings.add(a1,a2)
dh_settings.row(back_wake_menu)

mom_settings = telebot.types.InlineKeyboardMarkup(row_width=2)
c1 = telebot.types.InlineKeyboardButton(text="Wake", callback_data="wake_2")
c2 = telebot.types.InlineKeyboardButton(text="Stop", callback_data="stop_2")
mom_settings.add(c1,c2)
mom_settings.row(back_wake_menu)

class HelperBot():

	__last_wake_msg = 0
	__last_start_msg = 0


	def __init__(self):
		try:
			with open('balance-3.txt', 'r') as f:
				self.rg = f.read().split('LTC ')
			# print(self.rg[0] +"\n"+ self.rg[-1])
			self.rgbalance = self.rg[0] +"\n"+ self.rg[-1].split(' + ')[0]
			self.rgreps = self.rg[-1].split(' + ')[-1]
		except:
			self.rgbalance = '???'
			self.rgreps = '???'
		try:
			with open('balance-2.txt', 'r') as f:
				self.mom = f.read().split('LTC ')
			# print(self.mom[0] +"\n"+ self.mom[-1])
			self.mombalance = self.mom[0] +"\n"+ self.mom[-1].split(' + ')[0]
			self.momreps = self.mom[-1].split(' + ')[-1]
		except:
			self.mombalance = '???'
			self.momreps = '???'
		try:
			with open('balance-1.txt') as f:
				self.dh = f.read().split('LTC ')
			self.dhbalance = self.dh[0] +"\n"+ self.dh[-1].split(' + ')[0]
			self.dhreps = self.dh[-1].split(' + ')[-1]
		except:
			self.dhbalance = '???'
			self.dhreps = '???'

	def changer_wake(self, mod=True, value=0):
		if mod:
			self.__class__.__last_wake_msg = value
			# print(self.__class__.__last_wake_msg)
		else:
			return self.__class__.__last_wake_msg

	def changer_start(self, mod=True, value=0):
		if mod:
			self.__class__.__last_start_msg = value
		else:
			return self.__class__.__last_start_msg

	def start_msg(self, message):
		return """
***HI evryvone my friend {0}!***
***📡📡📡📡📡📡📡STATS📡📡📡📡📡📡📡***
***3-Bot*** - {1}
repeats: {2}
***2-Bot -*** {3}
repeats: {4}
***1-Bot -*** {5}
repeats: {6}
***Good luck*** for cryptomaing""".format(message.from_user.first_name,
 self.rgbalance,
 self.rgreps,
 self.mombalance,
 self.momreps,
 self.dhbalance,
 self.dhreps
 )
		



@bot.message_handler(commands=['start'])
def start_msg(message):
	try:
		bot.delete_message(message.chat.id, message.message_id)
	except:
		pass
	check_id = HelperBot().changer_start(mod=False)
	if check_id != 0:
		try:
			bot.delete_message(message.chat.id, check_id)
		except:
			pass
	if message.from_user.username == 'Your_username of telegram':
		_id = bot.send_message(message.chat.id, text=HelperBot().start_msg(message), parse_mode='markdown')
		HelperBot().changer_start(value=_id.message_id)
		log.warning("LAST START:" + str(_id.message_id))
	else:
		notlegal = str(message.from_user.id)
		log.warning(u"{0}".format(notlegal) + u" wont take my balance")

@bot.message_handler(commands=['wakeup'])
def wake(message):
	if message.from_user.username == 'Your_username of telegram':
		try:
			bot.delete_message(message.chat.id, message.message_id)
		except:
			pass
		check_id = HelperBot().changer_wake(mod=False)
		if check_id != 0:
			try:
				bot.delete_message(message.chat.id, check_id)
			except:
				pass
		_id = bot.send_message(message.chat.id, text="All bots", reply_markup=wake_stop)
		HelperBot().changer_wake(value=_id.message_id)
		log.warning("LAST WAKE:" + str(_id.message_id))
	else:
		notlegal = str(message.from_user.id)
		log.warning(u"{0}".format(notlegal) + u" wont take my balance")

@bot.message_handler(commands=['status'])
def wake(message):
	pass

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
	if c.data == '3':
		bot.edit_message_text(chat_id=c.message.chat.id,
		 message_id=c.message.message_id,
		 text="3-Bot",
		 reply_markup=rg_settings)
	elif c.data == '1':
		bot.edit_message_text(chat_id=c.message.chat.id,
		 message_id=c.message.message_id,
		 text="1-Bot",
		 reply_markup=dh_settings)
	elif c.data == '2':
		bot.edit_message_text(chat_id=c.message.chat.id,
		 message_id=c.message.message_id,
		 text="2-Bot",
		 reply_markup=mom_settings)
	elif c.data == 'wake_3':
		os.system("sh api_bash.sh --run 3_bot.py")
		try:
			bot.delete_message(c.message.chat.id, c.message.message_id)
		except:
			pass
		bot.send_message(c.message.chat.id, text="Successful\nAll bots",
		 reply_markup=wake_stop)
	elif c.data == 'stop_3':
		try:
			bot.delete_message(c.message.chat.id, c.message.message_id)
		except:
			pass
		bot.send_message(c.message.chat.id, text="Successful\nAll bots",
		 reply_markup=wake_stop)
		os.system("sh api_bash.sh --kill 3_bot.py")
	elif c.data == 'wake_1':
		os.system("sh api_bash.sh --run 1_bot.py")
		try:
			bot.delete_message(c.message.chat.id, c.message.message_id)
		except:
			pass
		bot.send_message(c.message.chat.id, text="Successful\nAll bots",
		 reply_markup=wake_stop)
	elif c.data == 'stop_1':
		try:
			bot.delete_message(c.message.chat.id, c.message.message_id)
		except:
			pass
		bot.send_message(c.message.chat.id, text="Successful\nAll bots",
		 reply_markup=wake_stop)
		os.system("sh api_bash.sh --kill 1_bot.py")
	elif c.data == 'wake_2':
		os.system("sh api_bash.sh --run 2_bot.py")
		try:
			bot.delete_message(c.message.chat.id, c.message.message_id)
		except:
			pass
		bot.send_message(c.message.chat.id, text="Successful\nAll bots",
		 reply_markup=wake_stop)
	elif c.data == 'stop_2':
		try:
			bot.delete_message(c.message.chat.id, c.message.message_id)
		except:
			pass
		bot.send_message(c.message.chat.id, text="Successful\nAll bots",
		 reply_markup=wake_stop)
		os.system("sh api_bash.sh --kill 2_bot.py")
	elif c.data == 'wake_all':
		try:
			bot.delete_message(c.message.chat.id, c.message.message_id)
		except:
			pass
		bot.send_message(c.message.chat.id, text="Successful\nAll bots",
		 reply_markup=wake_stop)
		os.system("sh api_bash.sh --run")
	elif c.data == 'sleep':
		try:
			bot.delete_message(c.message.chat.id, c.message.message_id)
		except:
			pass
		bot.send_message(c.message.chat.id, text="Successful\nAll bots",
		 reply_markup=wake_stop)
		os.system("sh api_bash.sh --kill all")
	elif c.data == 'back_wake_menu':
		try:
			bot.delete_message(c.message.chat.id, c.message.message_id)
		except:
			pass
		bot.send_message(c.message.chat.id, text="Successful\nAll bots",
		 reply_markup=wake_stop)
		os.system("sh api_bash.sh --kill all")


def main():
	with open('status.log') as f:
		pattern = f.read()
	relust = re.split(r'LAST WAKE:', pattern)[-1]
	value = re.split(r'status_bot.py', relust)[0]
	HelperBot().changer_wake(value=value)
	relust = re.split(r'LAST START:', pattern)[-1]
	value = re.split(r'status_bot.py', relust)[0]
	HelperBot().changer_start(value=value)

if __name__ == '__main__':
	main()
	try:
		bot.polling(timeout=50000000)
	except:
		bot.polling(timeout=50000000)