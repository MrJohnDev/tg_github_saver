import time,sys,telebot,wget,ssl,os

#Fix for CERTIFICATE_VERIFY_FAILED
ssl._create_default_https_context = ssl._create_unverified_context

bot = telebot.TeleBot('token')
user_id = 123456789


def create_dir(path):
	try:
		os.mkdir(path)
	except OSError:
		pass

def remove_file(path):
	try:
		os.remove(path)
	except OSError:
		pass

def github_download(message):
	github_url=message.text.split('/')
	for gh in enumerate(github_url):
		if(gh[1]=='github.com'):
			create_dir('github')
			github_download_url=f"https://github.com/{github_url[gh[0]+1]}/{github_url[gh[0]+2]}/archive/master.zip"
			file_name=f"github/{github_url[gh[0]+1]}_{github_url[gh[0]+2]}.zip"
			if(os.path.isfile(file_name)):
				remove_file(file_name)
			wget.download(github_download_url, file_name)
			bot.delete_message(message.chat.id,message.message_id)
			break


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	try:
		if(message.from_user.id==user_id):
			if(message.text.find('github.com')>-1):
				github_download(message)
	except Exception as e:
		print(e)
	
while True:
	try:
		#bot.polling(none_stop=True)
		print('\t✅ Working')
		bot.polling()
		sys.exit()
	except Exception as e:
		print(e)
		print('\t🔄 Restart')