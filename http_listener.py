import datetime

while 1:
	try:
		protocol = input()
		cond = protocol.find("HTTP: GET")
		if cond >= 0:
			http = protocol[cond:]
			cond2 = http.find("HTTP/1.1")
			last_url = http[10:cond2]
			clock = protocol[0:8]
			cond3 = protocol.find("IP")
			cond4 = protocol.find(">")
			user = protocol[cond3+3:cond4-2]
			print(http)
			date = str(datetime.datetime.now())
			print("date: " + date[0:10] + " " +clock)
			cond = -1
			while cond <0:
				protocol = input()
				cond = protocol.find("Host:")
			print("URL: " + r"http://www."+protocol[6:] + last_url)
			print("user: " + user)
			print("---------------")
	except EOFError:
		break
