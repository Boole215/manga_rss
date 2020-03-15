import dill, os, rss_commands
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




def isEmpty(file):
		return os.stat(file).st_size == 0;

inUse = True; # meaning: This program is 'inUse'
if(not isEmpty("all2d.dat")):
	saveFile = open("all2d.dat","rb");
	loadedFile = dill.load(saveFile);
	print(loadedFile);
	rss_commands.feedList = loadedFile[1];
	rss_commands.feedDict = loadedFile[0];
	saveFile.close();
	x = "{0} Feeds loaded.\n".format(len(rss_commands.feedList));
else: 
	print("\nPlease add a feed using the add command.\n");

while rss_commands.inUse:
	
	currentCommand = input();
	rss_commands.splitCommand(currentCommand);
	#print(inUse);

if(len(rss_commands.feedList) > 0):
	toSave = [rss_commands.feedDict,rss_commands.feedList];
	saveFile = open("all2d.dat","wb");
	dill.dump(toSave, saveFile);
	saveFile.close();  



#dumpfile = open("pickle.dat","rb");

#thisobj = dill.load(dumpfile);
