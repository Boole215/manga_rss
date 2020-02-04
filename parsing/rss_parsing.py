import feedparser
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

    def updateTitles():
        self.topFeedtitles = [];
        for i in range(10):
            topFeedTitles.append(crntFeed.entries[i].title);
        #This adds the title of the top 10 entries in the rss feed to the
        #list "topFeedTitles"
