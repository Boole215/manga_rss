import feedparser
from datetime import datetime
#one of the goalsis to take this RSS feed, and add it to a database of rss feeds
#that we're going to reach into whenever we open the application
#that is to be implemented later, since that's trickier than the rest
#for now I'm going to be implementing a class that'll let me do these operations
#in a way that looks prettier than calling a convoluted function.

class MangaFeed:

    def __init__(self, userTitle, feedURL):
        self.userTitle = userTitle;
        self.thisFeed = feedURL;
        self.parsedURL = feedparser.parse(feedURL);
        self.topFeedTitles = [];
        self.lastUpdateTime = 0;
        self.feedTitle = str(self.parsedURL.feed.title);
        self.crntPlace = 9;

    def __retparseTime(self):
        crnt = str(datetime.now());
        # '2020-02-04 00:58:10.692660' example length of a string output
        crnt = crnt[2:19]
        #parses the string into the format YY-MM-DD HH:MM:SS

    def __retFeedTitle(self):
        return str(parsedURL.feed.title);
        #returns the title of the feed as a string

    def updateTitles(self):
        self.topFeedtitles = [];
        for i in range(10):
            self.topFeedTitles.append(self.parsedURL.entries[i].title);
        #This adds the title of the top 10 entries in the rss feed to the
        #list "topFeedTitles"
        self.lastUpdateTime = self.__retparseTime();
        #updates the lastUpdateTime to the current time (as the rss feed was
        #updated)


    def retTenEntries(self):
        return self.topFeedTitles;


    def moveTenEntries(self, d):
        self.topFeedTitles = [];
        localPlace = self.crntPlace;
        if(d == 1 or d == -1):
            i = 0;
            for i in range(10):
                if(localPlace+(i*d) <= len(self.parsedURL.entries) and (localPlace+(i*d)) >= 0):
                    self.topFeedTitles.append(self.parsedURL.entries[localPlace+i*d].title);
                else:
                    break;


            self.crntPlace = self.crntPlace + (i*d);

        else:
            print("You have reached the bounds of the feed.");
    def retTitle(self):
        return self.userTitle;
