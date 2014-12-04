import tweepy


# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = "BpqGIEY4RFPfmzKmEGzqTw"
consumer_secret = "qRtrL6GzZxh3KC5zr2FHasswb6lG3oxAqtzlOmYhs"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token = "1718905052-DtEJsKOahr0OSEhAr7eqeExFZDdlUIvqjaDCuDw"
access_token_secret = "GYnZqQJrBuBwHNgGMXEbzf3xpvdoGSMb1dcb2Tg7Ik"

auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token, access_token_secret)

class StdOutListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        f.write (data)
	print ("Executing")
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':
    f = open('resp.txt','w')
    l = StdOutListener()
    
    streamer = tweepy.Stream(auth = auth1,listener=l)
    setTerms =[7.139987,-75.478149,-36.918399,-28.544560]
    streamer.filter(track = ['DebateNaGlobo'])
    streamer.filter(locations = setTerms)
