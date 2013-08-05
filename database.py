######
# Database.py
#
# This module will manage the database.  The database is a custom structure
# that uses a Berkeley DB backend.

import os

class db:
	# Constructor Function
	def __init__(self,db_path # Path to the database file on the filesystem 
			):
		self.fn = db_path

		# Check if databse fle already exists
		if os.path.exists(self.fn):
			# If so, open the db
			db = bsddb.open(self.fn)
			# Verify that the "0" key is present
		else:
			db = bsdb.oepn(self.fn, "w")
			db["0"] = "[]"

	# add_object
	# Generic method for adding object to the database
	#
	# @param obj - A JSON object dictionary that describes the object
	# @returns The key of the new object
	def add_object(self,obj,parent_key):
		# Generate a new object key
		obj_key = self.gen_key()
		# Add new object to the database
		db[obj_key] = json.dumps(obj)

		# Load the parent object
		p_obj = json.loads(db[parent_key])
		# Verify that the parent is a category
		if not children in p_obj.keys:
			# Generate an error
			return -1
		# Add the new object key to the category list
		p_obj["children"].append(obj_key)
		# Converr the parent object into a string and load into db
		db[parent_key].modify(json.dumps(p_obj))

		return obj_key

	# remove_object
	# Generic method for removing an object from the database
	#
	# @param obj_key - The key of the object you want to remove
	# @param parent_key - (Optional) key of the parent object
	# @returns 0 if sucessful, otherwsie an error code
	def remove_object(self,obj_key,parent_key=None):
		# Verify that they are not trying to remove the root object
		if obj_key=="0":
			return -1

		# Check that the key exists in the library

		# Load the object for parsing 
		obj = json.loads(db[obj_key])
		# Recusively delete all children
		for x in obj["children"]:
			ret = self.remove_object(x)
			# Stop if there was an error
			if ret != 0:
				return ret

		# Remove the element itself
		db.remove[key]

		# Remove Element from Parent's list
		if parent_key == None:
			# Find the Parent Key

		# Load the parent object
		pobj = json.loads(db[parent_key])
		# Remove the object key from the parent list
		pobj["children"].pop[obj_key]
		# Update the database
		db[parent_key]=json.dumps(pobj)

		return 0

	# Clean Database
	# Scans the database and removes items that are older than a year
	# and marked as deleted.  It also removes empty categories
	#
	# @param key - Defaults to root.  The current object key being scanned
	# @returns zero if successful.
	def clean_db(self, key="0"):
		obj = json.loads(db[key])

		if "children" in obj:
			# This object is a category or the root
			if len(obj["children"]) == 0:
				if key != "0": # If its a category) (Not root)					# Remove the category
					self.remove_object(key)
			else:
				for c in obj["children"]:
		else: 
			# This object is an item
	
			if time.time() - obj["time"] > 365*24*60*60 and obj["status" == DELETED:
				# Object is older than a year and deleted
				self.remove_object(key)




	# Sync Database
	# This function reads a JSON string and syncs it with the local 
	# database
	#
	# @param c_json - A JSON string containing a client's copy of the db
	# @returns 0 if sucessful. 
	def sync(self,c_json):
		# Load this Client JSON into a client object
		c_obj = json.loads(c_json)

		# For each category in the client object
		for c_cat in c_obj:
			# Check if Category already exists in the server db
			if c_cat["name"] in db.keys():
				# Create a new category
				obj = {
					name=c_obj["name"],
					color=c_cat["color"],
					children = []
					}
				# Add the object to the database
				self.add_object(obj,"0",c_obj["name"])

			# For each item in this category
			for c_item in c_cat["children"]:
				# Check if Category already exists
				if c_item["uid"] in db.keys():
					# Load the Server's version of the item
					s_obj = json.loads(db[c_item["uid"]])
					# Check which item is "newer"
					if c_item["time"] > s_obj["time"]:
						# Remove the old item
						self.remove_object(c_item["uid"])
						self.add_object(...)
					else:
						# Do nothing. Ignore the client item
				else: # The item is new
					self.add_object()
	

	
	# Get Client DB
	# This method generates a JSON string that represents a client DB
	#
	# @returns A json string
	def get_client_db(self):
		client_db = []
		# Get a List of Categories from the self.db
		for c in categories:
			new_cat = {	
					name=c["name"],
					color=c["color"],
					children=[]
					}
			# Get a list of Items
			for i in items:
				# if Item is deleted
					# if item is older than a month
						continue
				
				# add item to new_cat["children"]

		return json.dumps(client_db)

					
## Example JSON Client Database String
"""
[
	{
		name="Fresh Food",
		color="#ffffff",
		children=[
				{
					uid="123sdjk10432j
					name="Carrots",
					time="1234567890",
					status="0"
				},
				{
					uid=fwnofq3rui
					name="Lettuce",
					time="1212132322",
					status="1"
				},
				{
					uid=jkfldsf394,
					name="Milk",
					time=343434334,
					status="2"
				}
			]
	},
	{
		name="Tasks",
		color="#123456",
		children=[
				{
					uid=19802jfkldss
					name="Sell Car"
					time="1232323131"
					status=0
				}
			]
	}

]
"""
## Example BDB Key-Value
"""
"0" ==> "["Fresh Food", "Tasks"]
"Fresh Food" ==> {
			name="Fast Food",
			color="#000000",
			children=[
				"123sdjk10432j",
				"fwnofq3rui"
			]
		}
"Tasks ==>"
"123sdjk10432j" ==> {
			uid=123sdjk10432j,
			name=Carrots
			time=1234567890
			status=0
		}
"fwnofq3rui" ==> {
			uid=fwnofq3rui,
			name=
			time=
			status=
		}
"""
		
