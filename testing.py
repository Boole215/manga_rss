from rss_parsing import *


#This works for getting the top 10 chapters from the feed shown.

first_feed = MangaFeed("https://rss.app/feeds/ZjRfTMQnCvrZ0ziI.xml");
first_feed.updateTitles();
first_feed.moveTenEntries(1);
crntTitles = first_feed.retTenEntries()

for i in range(len(crntTitles)):
	print(""+crntTitles[i]);


# What is left to be implemented now is a way to interact with the program. 

# Allowing for the user to input feeds, update them, "scroll" through the titles
#