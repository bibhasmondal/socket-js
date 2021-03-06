from websocket_server import WebsocketServer
from threading import Thread
import threading
class Server:
	clients = {}

	def client_left(self,client, server):
	    msg = "Client (%s) left" % client['id']
	    print (msg)
	    try:
	        self.clients.pop(client['id'])
	    except:
	        print ("Error in removing client %s" % client['id'])
	    #for cl in self.clients.values():
	        #server.send_message(cl, msg)


	def new_client(self,client, server):
	    msg = "New client (%s) connected" % client['id']
	    print (msg)
	    #for cl in self.clients.values():
	        #server.send_message(cl, msg)
	    self.clients[client['id']] = client


	def msg_received(self,client, server, msg):
	    #msg = "Client (%s) : %s" % (client['id'], msg)
	    #print (msg)
	    clientid = client['id']
	    for cl in self.clients:
	        if cl != clientid:
	            cl = self.clients[cl]
	            server.send_message(cl, msg)

	def __init__(self,ip,port):
	    server = WebsocketServer(port,ip)
	    server.set_fn_client_left(self.client_left)
	    server.set_fn_new_client(self.new_client)
	    server.set_fn_message_received(self.msg_received)
	    server.run_forever()

