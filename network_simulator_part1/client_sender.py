import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

s = requests.Session()
retries = Retry(total=5,backoff_factor=0.1,status_forcelist=[500, 502, 503, 504])
s.mount('http://', HTTPAdapter(max_retries=retries))
# Above is network related configuration



ADDRESS_HUB = "127.0.0.1:5000"
ADDRESS_BRIDGE = "127.0.0.1:5000"
ADDRESS_SWITCH = "127.0.0.1:5000"
ADDRESS_DIRECT = "127.0.0.1:5000"


ADDRESS_CLIENT1= ["127.0.0.1","5001"]
ADDRESS_CLIENT2= ["127.0.0.1","5002"]
ADDRESS_CLIENT3= ["127.0.0.1","5003"]
ADDRESS_CLIENT4= ["127.0.0.1","5004"]
ADDRESS_CLIENT5= ["127.0.0.1","5005"]


headers = {'Content-type': 'application/json'}

choice = 0

while choice < 6:
	choice =  int(input("\n\n\n1. Send to clients via Hub\n2. Send to Clients via Switch\n3. Send to Clients via Bridge\n4. Send to Clients directly \n5. Send to Client2 Directly\n6. Exit\n ENTER CHOICE: "))
	
	if choice < 6:
		sender_id = int(input("\nWho is sending? 1. Client1 2. Client2 3.Client3 4.Client4 5.Client5\n Enter Choice [1-5]:"))
		receiver_id = int(input("\nWho is receiving? 1. Client1 2. Client2 3.Client3 4.Client4 5.Client5 \n Enter Choice [1-5]:"))
		data = input("\nEnter data to send:")


	#CONFIGURING SENDER
	if sender_id  == 1:
		IP_ME = ADDRESS_CLIENT1[0]
		PORT_ME = ADDRESS_CLIENT1[1]
	
	elif sender_id ==2:
		IP_ME = ADDRESS_CLIENT2[0]
		PORT_ME = ADDRESS_CLIENT2[1]

	elif sender_id ==3:
		IP_ME = ADDRESS_CLIENT3[0]
		PORT_ME = ADDRESS_CLIENT3[1]

	elif sender_id ==4:
		IP_ME = ADDRESS_CLIENT4[0]
		PORT_ME = ADDRESS_CLIENT4[1]

	elif sender_id ==5:
		IP_ME = ADDRESS_CLIENT5[0]
		PORT_ME = ADDRESS_CLIENT5[1]

	# CONFIGURING RECEIVER
	if receiver_id == 1:
		IP_R = ADDRESS_CLIENT1[0]
		PORT_R = ADDRESS_CLIENT1[1]

	elif receiver_id == 2:
		IP_R = ADDRESS_CLIENT2[0]
		PORT_R = ADDRESS_CLIENT2[1]

	elif receiver_id == 3:
		IP_R = ADDRESS_CLIENT3[0]
		PORT_R = ADDRESS_CLIENT3[1]

	elif receiver_id == 4:
		IP_R = ADDRESS_CLIENT4[0]
		PORT_R = ADDRESS_CLIENT4[1]

	elif receiver_id == 5:
		IP_R = ADDRESS_CLIENT5[0]
		PORT_R = ADDRESS_CLIENT5[1]


	if choice == 1:
		payload = { "sender_ip":IP_ME,"sender_port":PORT_ME, "receiver_ip":IP_R,"receiver_port":PORT_R, "data":data}
		response = s.get("http://"+ADDRESS_HUB+"/hub", json=payload, headers=headers, timeout=25)

	elif choice == 2:
		payload = { "sender_ip":IP_ME,"sender_port":PORT_ME, "receiver_ip":IP_R,"receiver_port":PORT_R, "data":data}
		response = s.get("http://"+ADDRESS_SWITCH+"/switch", json=payload, headers=headers, timeout=25)

	elif choice == 3:
		payload = { "sender_ip":IP_ME,"sender_port":PORT_ME, "receiver_ip":IP_R,"receiver_port":PORT_R, "data":data}
		response = s.get("http://"+ADDRESS_BRIDGE+"/bridge", json=payload, headers=headers, timeout=25)
	
	elif choice == 4:
		payload = { "sender_ip":IP_ME,"sender_port":PORT_ME, "receiver_ip":IP_R,"receiver_port":PORT_R, "data":data}
		response = s.get("http://"+ADDRESS_DIRECT+"/direct", json=payload, headers=headers, timeout=25)
	
	#elif choice == 5:
		#payload = { "sender_ip":IP_ME,"sender_port":PORT_ME, "receiver_ip":ADDRESS_CLIENT1[0],"receiver_port":ADDRESS_CLIENT1[1], "data":data}
		#response = s.get("http://"+ADDRESS_CLIENT2[0]+":"+str(ADDRESS_CLIENT2[1]), json=payload, headers=headers, timeout=25)
	
	print(response.text)
