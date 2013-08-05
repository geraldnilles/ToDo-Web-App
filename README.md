ToDo Web App
============

# Goal
Make a categorized ToDo list that multiple people can use and interact with using a web browser.

## Basic Idea
Each User will maintain its over version of the ToDo list.  It will be stored locally as a JSON String.  We will use HTML5 Offline storeage so that users can still use the ToDo list when there is no internet connection.

When the user does have an internet connection, it will sync its ToDo list with the server.  It will send the JSOn string to the server, the server will process the list and merge it with the master list, and the server will send back a reduced version of the master the list.

The reduced version of the master simply removed items that were deleted and are olde rthan a month.  To avoid confusion when mergin, the complete master list will contain every deleted item.  Therefore, if 2 users delete the same item, the server will not get confused when an item is removed and then re-removed later.  Its best to keep documentation of all items.  

## Features
* Allow multiple users to create, delete, and modify todo items
* Categorize todo items
* Offline Operation
* Show 1 week of Google Calendar events

# User Interface
HTML / CSS / JS

# Syncing 
The most difficult part of making a single webapp with multiple collaberators is synicng and collition handling.  You could potentailly have multiple people editing the same item at the same time. 

# Offline Mode
This web app will need an offline mode so you can add, modify the list when offline. 

# Database
THe database will use a Berkeley DB (BDB).  BDB is a simple Key-value database.  however, you can use it to create more complex structures

## Structure

The Category List is the only object that has a hard coded key.  All of the other objects (Category Object or Item Object) will have randomely generated keys that are unique to the item.

### Category List
At the very root of the strucutre will be the Cateogry List.  This will be a JSON string listing the keys of the varous Category Objects.  This will be the only object that has a hard-coded key.  It will be "0".

### Category Objects
This object will contain info about a category.  It will consist of a JSON string dictionary.  The dictionary will contain the following
	{
		name: "[category name]",
		color: "#RRGGBB"
		items: [list of item object keys]
	}

### Item Objects
This obejct will cotain info about an item.  It will consist of a JSON string dictionary.  The dictionary will contain the following
	{
		name: "[item description]"
		status: 0-3
	}

The status will be an integer.  The integer will represent OPEN, DONE, or DELETED

## Example
The example below is not what the databse will look lke, but it helps to visualize the structure of the structure and how the BDB works. 

0:[123,456]
123:{name:"Groceries",color:"#ff0000",items:[1234,5678]}
456:{name:"Tasks",color:"#00ff00",items:[6666,6662]}
1234:{name:"Bread",status:0}
5678:{name:"Milk",status:1}
6666:...
6662:...



