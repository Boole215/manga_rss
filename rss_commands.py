from rss_parsing import MangaFeed
feedList = [];
feedDict= {};
inUse = True;

def getPlace(feedTitle):
	placeDict = feedList[0];
	return placeDict[feedTitle];


def add(title, url):
	newFeed = MangaFeed(title,url);
	feedDict[title] = len(feedList);
	feedList.append(newFeed);
	#print("\n \n \n Current feedDict and feedList:\n\n");
	#print(feedDict)
	#print("\n");
	#print(feedList);
	#print("\n");



def remFeed(feedTitle):
	global feedList;
	global feedDict;
	#Find the feed's place in the list
	place = feedDict[feedTitle];
	#remove the feed from the list
	feedList.pop(place);
	
	#now, decrement the value for each title after kaguya, if there are any feeds left
	if(len(feedList) > 0):
		for i in range(place, len(feedDict)):
			crntTitle = feedList[feedDict[i]].retTitle();
			feedDict[crntTitle] = feedDict[crntTitle] - 1;

		#then deletes the feed that we had removed from the feedList from the dict

	del feedDict[feedTitle];

def listFeed(input):
	#print(len(input));
	if len(input) == 3 and input[1] == 'feed':
		MangaObj = feedList[feedDict[input[2]]];
		for i in MangaObj.retTenEntries():
			print("\b"+ i + "\n");

	elif len(input) == 2 and input[1] == 'feed':
		if(len(feedList) > 0):
			print("\n Feeds\n ~~~~~");
			for i in range(len(feedList)):
				print(" "+ feedList[i].retTitle() + "\n");
		else:
			print("\nYou currently have no feeds, why not add one?\n");

	else:
		print("format:\n   list feed (Optional: feedTitle)");

def updateFeed(input):
	if(len(input) > 2 or len(input) == 1):
		print("Usage: update (feedName)")
	else:
		if(input[1] in feedDict):
			place = feedDict[input[1]];
			feedList[place].update();
			print("\nFeed updated.\n");
		else: 
			print("\nFeed not found.\n");
def help(input):
	print("this is the help function!");

def splitCommand(input):
	input = input.split(" ");
	#print(input);

	if input[0] == 'add' and len(input) == 3:
		add(input[1], input[2]);

	elif input[0] == 'remove' and len(input) == 2:
		remFeed(input[1]);

	elif input[0] == 'list':
		listFeed(input);

	elif input[0] == 'update':
		updateFeed(input);

	elif input[0] == 'exit' or input[0] == 'quit':
		global inUse 
		inUse = False;

	elif input[0] == 'help':
		help(input);
	
	else:
		print("Command not recognized.")