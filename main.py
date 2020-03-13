from rss_parsing import MangaFeed
import dill, os
'''
 Current commands
~~~~~~~~~~~~~~~~~~
- add
-- feed (title, url)

- remove
-- feed (feedTitle) (removes a feed)


- list
-- feed (lists feeds by their given titles) !TODO:Alphabetically sorted titles?
-- feed feedTitle (lists 10 chapters from feed)
-- !TODO: feed feedTitle N (N returns information regarding that entry in the feed)

- update
-- feedTitle (updated the given feed)
-- all       (updates all feeds), returns the names
			  of the feeds that had updates
'''

#Dill is what I'm going to be using to save the feeds that we already have.
#I'm not too sure as to where I'm going to place this quite yet, but I'm likely
#Going to make another file separate from this one, where I can put all the
#GUI functions that are going to work with the class/methods

# This program should continue to run until the user inputs 'quit' or 'exit'




def getPlace(feedTitle):
	placeDict = feedList[0];
	return placeDict[feedTitle];


def add(title, url):
	newFeed = MangaFeed(title,url);
	feedList.append(newFeed);


# The remove function is implemented assuming
# the first element in the feedlist is a hashmap
# with the feedTitle as the key and the value being
# their place in the list

def remove(feedTitle):
	placeDict = feedList[0];
	feedList = feedlist.pop(placeDict[feedTitle]);


def listFeed(input):
	if len(input) == 3 and input[1] == 'feed':
		MangaObj = feedList[getPlace(input[2])];
		MangaObj.retTenEntries();
	elif len(input) == 2 and input[1] == 'feed':
		for i in range(1,len(input)):
			print(i.retTitle() + "\n");
	else:
		print("format:\n   list feed (feedTitle)");

def updateFeed(input):
	print("This is the update function!");

def help(input):
	print("this is the help function!");

def splitCommand(input):
	input.split(" ");

	if input[0] == 'add':
		add(input[1], input[2]);

	elif input[0] == 'remove':
		remFeed(input[1],);

	elif input[0] == 'list':
		listFeed();

	elif input[0] == 'update':
		updateFeed();

	elif input[0] == 'exit':
		inUse = False;

	elif input[0] == 'help':
		help(input);
	
	else:
		print("Command not recognized.")


inUse = True; # meaning: This program is 'inUse'

saveFile = open("all2d.dat","rb");
feedList = dill.load(saveFile);

while inUse:
	x = "{0} Feeds loaded.\n".format(len(feedList))
	currentCommand = input(x);
	
saveFile.close();  
#dumpfile = open("pickle.dat","rb");

#thisobj = dill.load(dumpfile);
