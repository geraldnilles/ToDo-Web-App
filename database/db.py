#------------------
# Database manager
#
# This process will run in its own thread and be in charge of maintaining the 
# master database.

class db:
	def __init__(self):
		self.addr_port = "/tmp/ToDo_DB_Socket"
		# Read Database from file
		
	def setup_socket(self):
		self.sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
		self.sock.timeout(60)
		self.sock.listen(2)
	
	def serve_forever():
		while(1):
			# Avoid Timeout errors
			try:
				# Receive Chunk of data	
				# Read first 4 bytes
				size_bin = self.sock.recv(4)
				# Convert those bytes into unsigned int
				size = struct.unpack("<H",size_bin)
				# Receive the rest of the packet
				data = self.sock.recv(size)
				# Merge the data with the database in memory
				self.merge(data)
				# Send the response
				self.sock.send(self.get_abridged_db)

			except socket.timeout:
				# Write JSON to disk
				pass

	# Searches the DB for a uuid
	def search_db(self,uuid):
		for i in self.db["items"]:
			if i["uuid"] == uuid:
				return i

		for c in self.db["categories"]:
			if c["uuid"] == uuid:
				return c

	def merge(self,new_db):
		# Forward Merger (Client to Server)
		for i in new_db["items"]:
			
		for c in new_db["categories"]:
			cat = self.search_db(c["uuid"])
			if cat:

			else:
		
		# Reverse Merger (Server to Client)
		for i in self.db["items"]:

		for c in self.db["categories"]

		


if __name__ == "__main__":
	db = create_db()
	db.setup_socket()
	db.serve_forever()
