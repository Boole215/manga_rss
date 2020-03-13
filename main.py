from rss_parsing import MangaFeed
import dill

#Dill is what I'm going to be using to save the feeds that we already have.
#I'm not too sure as to where I'm going to place this quite yet, but I'm likely
#Going to make another file separate from this one, where I can put all the
#GUI functions that are going to work with the class/methods

# This program should continue to run until the user inputs 'quit' or 'exit'

# Current commands
#~~~~~~~~~~~~~~~~~~
#- add
#-- feed (title, url)
#
#- remove
#-- feed (feedTitle) (removes a feed)
#
#
#- list
#-- feed (lists feeds by their given titles) !TODO:Alphabetically sorted titles?
#-- feed feedTitle (lists 10 chapters from feed)
#
#- update
#-- feedTitle (updated the given feed)
#-- all       (updates all feeds), returns the names
#			  of the feeds that had updates



inUse = True;


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
	if len(input) == 3:


def splitCommand(input):
	input.split(" ");

	if input[0] == 'add':
		add(input[1], input[2]);

	elif input[0] == 'remove':
		remFeed(input[1],);

	elif input[0] == 'list':
		listFeed();

saveFile = open('all2d.3dpd','rb');
feedList = dill.load(saveFile);

while inUse:

	currentCommand = input("{} Feeds loaded.\n".insert(len(feedList));
	




