#python2.y
import os,sys,re,random,time
import requests

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[36m'
purple = '\033[35m'
reset = '\033[0m'
#initialize OS for display clear
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
try:
	os.mkdir('Video')
except OSError:
	pass

def loading():
	try:
		a = 50
		b = 0
		for c in range(a):
			a -= 1
			b += 1
			sys.stdout.write(yellow+"\rDownloading [%s%s] %s/%s"%("#"*b,"-"*a,b+50,'100')),;sys.stdout.flush()
			time.sleep(0.05)
	except KeyboardInterrupt:
		sys.exit()


print(green+"""         __                              _               
        / _\ ___  ___ _ __ ___   ___  __| |              
        \ \ / _ \/ __| '_ ` _ \ / _ \/ _` |              
        _\ \ (_) \__ \ | | | | |  __/ (_| |              
    ___ \__/\___/|___/_| |_| |_|\___|\__,_|  _           
   /   \_____      ___ __ | | ___   __ _  __| | ___ _ __ 
  / /\ / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
 / /_// (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
/___,' \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                         """)
print(red+'Download Video Facebook or Instagram\n')
print(yellow+'1. Video Instagram Downloader')
print(blue+'2. Video Facebook Downloader')

pilih = input(reset+'Select Menu: '+yellow)
if pilih == '1':
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	pass
	print(blue+" _____          _                                  ")
	print("|_   _|        | |                                 ")
	print(purple+"  | | _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___  ")
	print("  | || '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \ ")
	print(red+" _| || | | \__ \ || (_| | (_| | | | (_| | | | | | |")
	print(yellow+" \___/_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_|")
	print("                          __/ |                    ")
	print(blue+"                         |___/                     ")
	print(red+'-----Video - Downloader-----')
	print(reset+'Example :%s https://www.instagram.com/p/xxxxxxxxxx/'%green)
	print(reset+'Author : %sSterben404' % red+reset)
	urls = input('Link Video : '+green)
	print(yellow+'Checking Video...'+reset)
	def main_ig(req):
		try:
			url = urls.replace('web.facebook.com','www.facebook.com').replace('m.facebook.com','www.facebook.com')
			req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
		except requests.exceptions.MissingSchema:
			print(reset+'[ %s!%s ] URL Error' % (red,reset))
			exit()
		pass
		regex = re.search('(?<="og:video" content=")(.*?)(?=" />)', req.content)
		if regex == None:
			print(red+'Video Not Found or Video Private!'+reset)
			exit()
		else:
			nama = random.randrange(0,9999999999)
			loading()
			download = requests.get(regex.group(), headers={'User-Agent': 'Mozilla/5.0'})
			with open('Video/IG-%s'%nama+'.mp4','ab') as file:
				file.write(download.content)
				file.close()
			print(green+'\n\nDownload Video Success : '+yellow+'Video/%s' % nama+'.mp4'+reset)
	main_ig(urls)
elif pilih == '2':
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	pass
	print(blue+""" ________                      __                       __       
|_   __  |                    [  |                     [  |  _   
  | |_ \_|,--.   .---.  .---.  | |.--.    .--.    .--.  | | / ]  
  |  _|  `'_\ : / /'`\]/ /__\\ | '/'`\ \/ .'`\ \/ .'`\ \| '' <   
 _| |_   // | |,| \__. | \__., |  \__/ || \__. || \__. || |`\ \  
|_____|  \'-;__/'.___.' '.__.'[__;.__.'  '.__.'  '.__.'[__|  \_] """)
	print(red+'-----Video - Downloader-----')
	print(reset+'Example :%s https://web.facebook.com/story.php?story_fbid=xxxxxxxxxxxxxxxxxxxxxx'%green)
	print(reset+'Author :%s Sterben404'%red+reset)
	urls = input('Link Video : '+green)
	print(yellow+'Checking Video...'+reset)
	def main_fb(req):
		try:
			url = urls.replace('web.facebook.com','www.facebook.com').replace('m.facebook.com','www.facebook.com')
			req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
		except requests.exceptions.MissingSchema:
			print(reset+'[ %s!%s ] URL Error' % (red,reset))
			exit()
		pass
		regex = re.search('(?<=hd_src:")(.*)(?=",sd_src:)', req.content)
		if regex == None:
			print(red+'Video Not Found or Video Private!'+reset)
			exit()
		else:
			nama = random.randrange(0,9999999999)
			loading()
			download = requests.get(regex.group(), headers={'User-Agent': 'Mozilla/5.0'})
			with open('Video/%s'%nama+'.mp4','ab') as file:
				file.write(download.content)
				file.close()
			print(green+'\n\nDownload Video Success : '+yellow+'Video/%s' % nama+'.mp4'+reset)
	main_fb(urls)
else:
	print(reset+'[ %s!%s ] Menu Not Found' % (red,reset))
if __name__ == '__main__':
		print(red+'Coder By Sterben404'+reset)
