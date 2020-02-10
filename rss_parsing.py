import feedparser, dill
#Dill is what I'm going to be using to save the feeds that we already have.
#I'm not too sure as to where I'm going to place this quite yet, but I'm likely
#Going to make another file separate from this one, where I can put all the
#GUI functions that are going to work with the class/methods
from datetime import datetime
#one of the goalsis to take this RSS feed, and add it to a database of rss feeds
#that we're going to reach into whenever we open the application
#that is to be implemented later, since that's trickier than the rest
#for now I'm going to be implementing a class that'll let me do these operations
#in a way that looks prettier than calling a convoluted function.

class MangaFeed:

    def __init__(self,feedURL):
        self.thisFeed = feedURL;
        self.parsedURL = feedparser.parse(feedURL);
        self.topFeedTitles = [];
        self.lastUpdateTime = 0;
        self.feedTitle = __retFeedTitle();
        updateTitles();

    def __retparseTime():
        crnt = str(datetime.now());
        # '2020-02-04 00:58:10.692660' example length of a string output
        crnt = crnt[2:19]
        #parses the string into the format YY-MM-DD HH:MM:SS

    def __retFeedTitle():
        feedTitle = str(parsedURL.feed.title);
        #returns the title of the feed as a string

    def updateTitles():
        self.topFeedtitles = [];
        for i in range(10):
            topFeedTitles.append(crntFeed.entries[i].title);
        #This adds the title of the top 10 entries in the rss feed to the
        #list "topFeedTitles"
        self.lastUpdateTime = __retparseTime();
        #updates the lastUpdateTime to the current time (as the rss feed was
        #updated)
