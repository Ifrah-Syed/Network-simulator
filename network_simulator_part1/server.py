from flask import Flask, jsonify, json, request
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

s = requests.Session()
retries = Retry(total=5,backoff_factor=0.1,status_forcelist=[500, 502, 503, 504])
s.mount('http://', HTTPAdapter(max_retries=retries))
# Above is network related configuration

headers = {'Content-type': 'application/json'}

app = Flask(__name__)

B_table={"port1":[],"port2":[]}
CAM_table = {}
ADDRESS_CLIENT1= ["127.0.0.1","5001"]
ADDRESS_CLIENT2= ["127.0.0.1","5002"]
ADDRESS_CLIENT3= ["127.0.0.1","5003"]
ADDRESS_CLIENT4= ["127.0.0.1","5004"]
ADDRESS_CLIENT5= ["127.0.0.1","5005"]


@app.route("/", methods=["GET", "POST"])
def hello_world():
	return "Hello, World!"


@app.route("/direct", methods=["GET", "POST"])
def direct():
	received_data = json.loads(request.data)
	print("FROM :"+str(received_data["sender_ip"])+'/'+str(received_data["sender_port"]))
	payload = {"sender_ip": received_data["sender_ip"], "sender_port": received_data["sender_port"],
			   "receiver_port": received_data["receiver_port"], "receiver_ip": received_data["receiver_ip"],
			   "data": received_data["data"]}
	response = s.get("http://" + received_data["receiver_ip"]+ ":" + str(received_data["receiver_port"]), json=payload, headers=headers,
					  timeout=25)
	print(response.text)
	if response.status_code == 200:
		return "success"


@app.route("/bridge", methods=["GET", "POST"])
def bridge_world():
	received_data = json.loads(request.data)
	print("\n\n\n********* RECEIVED DATA AT SWITCH *************\n\n")
	print("FROM :"+str(received_data["sender_ip"])+'/'+str(received_data["sender_port"]))
	payload = {"sender_ip": received_data["sender_ip"], "sender_port": received_data["sender_port"],
			   "receiver_ip": received_data["receiver_ip"], "receiver_port": received_data["receiver_port"],
			   "data": received_data["data"]}
	sen_ip = str(received_data["sender_ip"])
	sen_port = int(received_data["sender_port"])
	rec_ip = str(received_data["receiver_ip"])
	rec_port = int(received_data["receiver_port"])
	if B_table["port1"] == [] or B_table["port2"] == []:
		print("\n\n\n********* SENDING TO ALL *************\n\n")
	if sen_port == 5001 or sen_port == 5002:
		if sen_ip + "/" + str(sen_port) not in B_table["port1"]:
			B_table["port1"].append(sen_ip + "/" + str(sen_port))
		if rec_ip + "/" + str(rec_port) not in B_table["port2"] and rec_ip + "/" + str(rec_port) not in B_table[
			"port1"]:
			response1 = s.get("http://" + ADDRESS_CLIENT1[0] + ":" + str(ADDRESS_CLIENT1[1]), json=payload,
							  headers=headers,
							  timeout=25)
			if response1.text == "Received by Client1 Successfully":
				B_table["port1"].append(ADDRESS_CLIENT1[0] + '/' + ADDRESS_CLIENT1[1])
				print(B_table)

			response2 = s.get("http://" + ADDRESS_CLIENT2[0] + ":" + str(ADDRESS_CLIENT2[1]), json=payload,
							  headers=headers,
							  timeout=25)
			if response2.text == "Received by Client2 Successfully":
				B_table["port1"].append(ADDRESS_CLIENT2[0] + '/' + ADDRESS_CLIENT2[1])
				print(B_table)

			response3 = s.get("http://" + ADDRESS_CLIENT3[0] + ":" + str(ADDRESS_CLIENT3[1]), json=payload,
							  headers=headers,
							  timeout=25)
			if response3.text == "Received by Client3 Successfully":
				B_table["port2"].append(ADDRESS_CLIENT3[0] + '/' + ADDRESS_CLIENT3[1])
				print(B_table)

			response4 = s.get("http://" + ADDRESS_CLIENT4[0] + ":" + str(ADDRESS_CLIENT4[1]), json=payload,
							  headers=headers,
							  timeout=25)
			if response4.text == "Received by Client4 Successfully":
				B_table["port2"].append(ADDRESS_CLIENT4[0] + '/' + ADDRESS_CLIENT4[1])
				print(B_table)

			response5 = s.get("http://" + ADDRESS_CLIENT5[0] + ":" + str(ADDRESS_CLIENT5[1]), json=payload,
							  headers=headers,
							  timeout=25)
			if response5.text == "Received by Client5 Successfully":
				B_table["port2"].append(ADDRESS_CLIENT5[0] + '/' + ADDRESS_CLIENT5[1])
				print(B_table)
		else:
			print("\nSENDING TO :" + str(rec_ip) + str(rec_port))
			resp = s.get("http://" + rec_ip + ":" + str(rec_port), json=payload,
						 headers=headers,
						 timeout=25)
			print(resp.text)
			print(B_table)


	else:
		if sen_ip + "/" + str(sen_port) not in B_table["port2"]:
			B_table["port2"].append(sen_ip + "/" + str(sen_port))
		if rec_ip + "/" + str(rec_port) not in B_table["port1"] and rec_ip + "/" + str(rec_port) not in B_table[
			"port2"]:
			response1 = s.get("http://" + ADDRESS_CLIENT1[0] + ":" + str(ADDRESS_CLIENT1[1]), json=payload,
							  headers=headers,
							  timeout=25)
			if response1.text == "Received by Client1 Successfully":
				B_table["port1"].append(ADDRESS_CLIENT1[0] + '/' + ADDRESS_CLIENT1[1])
				print(B_table)

			response2 = s.get("http://" + ADDRESS_CLIENT2[0] + ":" + str(ADDRESS_CLIENT2[1]), json=payload,
							  headers=headers,
							  timeout=25)
			if response2.text == "Received by Client2 Successfully":
				B_table["port1"].append(ADDRESS_CLIENT2[0] + '/' + ADDRESS_CLIENT2[1])
				print(B_table)

			response3 = s.get("http://" + ADDRESS_CLIENT3[0] + ":" + str(ADDRESS_CLIENT3[1]), json=payload,
							  headers=headers,
							  timeout=25)
			if response3.text == "Received by Client3 Successfully":
				B_table["port2"].append(ADDRESS_CLIENT3[0] + '/' + ADDRESS_CLIENT3[1])
				print(B_table)

			response4 = s.get("http://" + ADDRESS_CLIENT4[0] + ":" + str(ADDRESS_CLIENT4[1]), json=payload,
							  headers=headers,
							  timeout=25)
			if response4.text == "Received by Client4 Successfully":
				B_table["port2"].append(ADDRESS_CLIENT4[0] + '/' + ADDRESS_CLIENT4[1])
				print(B_table)

			response5 = s.get("http://" + ADDRESS_CLIENT5[0] + ":" + str(ADDRESS_CLIENT5[1]), json=payload,
							  headers=headers,
							  timeout=25)
			if response5.text == "Received by Client5 Successfully":
				B_table["port2"].append(ADDRESS_CLIENT5[0] + '/' + ADDRESS_CLIENT5[1])
				print(B_table)


		else:
			print("\nSENDING TO :" + str(rec_ip)+'/'+str(rec_port))
			resp = s.get("http://" + rec_ip + ":" + str(rec_port), json=payload,
						 headers=headers,
						 timeout=25)
			print(resp.text)
			print(B_table)

	# if response1.status_code == 200 or response2.status_code == 200 and response3.status_code == 200 and response4.status_code == 200 and response5.status_code == 200:
	return "success"


@app.route("/switch", methods=["GET", "POST"])
def switch_world():
	received_data = json.loads(request.data)
	print("\n\n\n********* RECEIVED DATA AT SWITCH *************\n\n")
	print("FROM :"+str(received_data["sender_ip"])+'/'+str(received_data["sender_port"]))
	payload = {"sender_ip":received_data["sender_ip"],"sender_port":received_data["sender_port"], "receiver_ip":received_data["receiver_ip"],"receiver_port":received_data["receiver_port"], "data":received_data["data"]}
	sen_ip = str(received_data["sender_ip"])
	sen_port = str(received_data["sender_port"])
	rec_ip = str(received_data["receiver_ip"])
	rec_port = int(received_data["receiver_port"])
	key_rec= str(rec_ip+"/"+str(rec_port))
	key_sen= str(sen_ip+"/"+str(sen_port))


	if key_sen not in CAM_table:
		CAM_table[sen_ip+"/"+(sen_port)] = (sen_port)

	if CAM_table=={}:
		print("\n\n\n********* SENDING TO ALL *************\n\n")

	if key_rec not in CAM_table:
		response1 = s.get("http://" + ADDRESS_CLIENT1[0] + ":" + str(ADDRESS_CLIENT1[1]), json=payload, headers=headers,
						  timeout=25)
		if response1.text == "Received by Client1 Successfully":
			CAM_table[ADDRESS_CLIENT1[0]+'/'+ADDRESS_CLIENT1[1]] = (ADDRESS_CLIENT1[1])
			print("\n\n\n************************* SENDING TO ALL *************************************\n\n")
			print(response1.text)
			print("\n\n\n************************* UPDATING CAM TABLE *************************************\n\n")
			print(CAM_table)

		response2 = s.get("http://" + ADDRESS_CLIENT2[0] + ":" + str(ADDRESS_CLIENT2[1]), json=payload, headers=headers,
						  timeout=25)
		if response2.text == "Received by Client2 Successfully":
			CAM_table[ADDRESS_CLIENT2[0]+'/'+ADDRESS_CLIENT2[1]] = (ADDRESS_CLIENT2[1])
			print("\n\n\n************************* SENDING TO ALL *************************************\n\n")
			print(response2.text)
			print("\n\n\n************************* UPDATING CAM TABLE *************************************\n\n")
			print(CAM_table)

		response3 = s.get("http://" + ADDRESS_CLIENT3[0] + ":" + str(ADDRESS_CLIENT3[1]), json=payload, headers=headers,
						  timeout=25)
		if response3.text == "Received by Client3 Successfully":
			CAM_table[ADDRESS_CLIENT3[0]+'/'+ADDRESS_CLIENT3[1]] = (ADDRESS_CLIENT3[1])
			print("\n\n\n************************* SENDING TO ALL *************************************\n\n")
			print(response3.text)
			print("\n\n\n************************* UPDATING CAM TABLE *************************************\n\n")
			print(CAM_table)

		response4 = s.get("http://" + ADDRESS_CLIENT4[0] + ":" + str(ADDRESS_CLIENT4[1]), json=payload, headers=headers,
						  timeout=25)
		if response4.text == "Received by Client4 Successfully":
			CAM_table[ADDRESS_CLIENT4[0]+'/'+ADDRESS_CLIENT4[1]] = (ADDRESS_CLIENT4[1])
			print("\n\n\n************************* SENDING TO ALL *************************************\n\n")
			print(response4.text)
			print("\n\n\n************************* UPDATING CAM TABLE *************************************\n\n")
			print(CAM_table)

		response5 = s.get("http://" + ADDRESS_CLIENT5[0] + ":" + str(ADDRESS_CLIENT5[1]), json=payload, headers=headers,
						  timeout=25)
		if response5.text == "Received by Client5 Successfully":
			CAM_table[ADDRESS_CLIENT5[0]+'/'+ADDRESS_CLIENT5[1]] = (ADDRESS_CLIENT5[1])
			print("\n\n\n************************* SENDING TO ALL *************************************\n\n")
			print(response5.text)
			print("\n\n\n************************* UPDATING CAM TABLE *************************************\n\n")
			print(CAM_table)
	else:
		print("\nSENDING TO :" + str(rec_ip)+'/'+str(rec_port))
		resp = s.get("http://" + rec_ip + ":" + str(rec_port), json=payload,headers=headers,timeout=25)
		print(resp.text)
		print(CAM_table)

	#if response1.status_code == 200 or response2.status_code == 200 and response3.status_code == 200 and response4.status_code == 200 and response5.status_code == 200:
	return "success"


@app.route("/hub", methods=["GET", "POST"])
def hub_world():
		received_data = json.loads(request.data)
		print("\n\n\n************************* RECEIVED DATA AT HUB *************************************\n\n")
		print("FROM :"+str(received_data["sender_ip"])+'/'+str(received_data["sender_port"]))
		print("\n\n\n************************* SENDING TO ALL *************************************\n\n")

		payload = {"sender_ip":received_data["sender_ip"],"sender_port":received_data["sender_port"],"receiver_port":received_data["receiver_port"],"receiver_ip":received_data["receiver_ip"], "data":received_data["data"]}
		#for every client
		response1 = s.get("http://"+ADDRESS_CLIENT1[0]+":"+str(ADDRESS_CLIENT1[1]), json=payload, headers=headers, timeout=25)


		response2 = s.get("http://"+ADDRESS_CLIENT2[0]+":"+str(ADDRESS_CLIENT2[1]), json=payload, headers=headers, timeout=25)


		response3 = s.get("http://" + ADDRESS_CLIENT3[0] + ":" + str(ADDRESS_CLIENT3[1]), json=payload, headers=headers,
						  timeout=25)

		response4 = s.get("http://" + ADDRESS_CLIENT4[0] + ":" + str(ADDRESS_CLIENT4[1]), json=payload, headers=headers,
						  timeout=25)

		response5 = s.get("http://" + ADDRESS_CLIENT5[0] + ":" + str(ADDRESS_CLIENT5[1]), json=payload, headers=headers,
						  timeout=25)

		print(response1.text)
		print(response2.text)
		print(response3.text)
		print(response4.text)
		print(response5.text)

		if response1.status_code == 200 and response2.status_code ==200 and response3.status_code==200 and response4.status_code==200 and response5.status_code==200:
			return "Success"
		else:
			return "Failure to send to Clients"



if __name__=="__main__":
	app.run(host='127.0.0.1',port=5000)