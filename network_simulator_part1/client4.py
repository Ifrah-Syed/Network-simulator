#This is client Receiver

from flask import Flask, jsonify, json, request
app = Flask(__name__)



IP_ME = "127.0.0.1"
PORT_ME = 5004




@app.route("/", methods=["GET", "POST"])
def client1():
	received_data = json.loads(request.data)
	sen = int(received_data["sender_port"])
	if sen != PORT_ME:
		print("\n\n\n*************************************\nData Reached to Client4 from "+ received_data["sender_ip"])
		print("\nData:"+ received_data["data"])
		print("\n\n***************************************")
		rec = int(received_data["receiver_port"])
		if rec == PORT_ME:
		   return "Received by Client4 Successfully"
		else:
		   return  "Message rejected by Client 4"
	else:
	      return "Message sent from Client4"

if __name__=="__main__":
	app.run(host=IP_ME,port=PORT_ME)