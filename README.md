ToDo Web App
============

# Introduction
Now that i am married, i need to coordinate many things with my wive.  The most common example is our shopping list.  We end up trading many emails/text/calls when attempting to go grocery shopping.  It would be nice if there was a simple website where we could coordinate ToDo items between eachother.

## Goal
Make a categorized ToDo list that multiple people can use and interact with using a web browser.

# Basic Idea
Each User will maintain its own version of the ToDo list.  It will be stored locally as a JSON String.  We will use HTML5 Offline storage so that users can still use the ToDo list when there is no internet connection.

When the user does have an internet connection, it will sync its ToDo list with the server.  It will send the JSOn string to the server, the server will process the list and merge it with the master list, and the server will send back a reduced version of the master the list.

The reduced version of the master simply removed items that were deleted and are older than a month.  To avoid confusion when merging, the complete master list will contain every deleted item.  Therefore, if 2 users delete the same item, the server will not get confused when an item is removed and then re-removed later.  Its best to keep documentation of all items.  

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

## Database 1.0
To start, i will use a JSON string as my database.  This will keep it simple to start.

	{
		"categories"=[{
				name="Groceries",
				uuid="123242",
				time="i3084302,
				color="#ffC"
			}.{
				name="Tasks",
				uuid="84390",
				time="i3084302,
				color="#fCf"
			}
		],
		"items"=[
			{
				name="Fish",
				uuid="84394320",
				time="i3084302,
				status="open",
				category="123232"
			},{
				name="Bread",
				uuid="84394320",
				time="i3084302,
				status="open",
				category="123232"
			}
		]
	}

## Database 2.0
Eventually, i would like to use a Key-Value database, like BDB
