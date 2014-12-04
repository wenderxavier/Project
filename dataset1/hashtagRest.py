request = twitter.request('search/tweets', {'q': '#DebateNaGlobo'})
tweet = None
for r in request:
    tweet = r
    break
print tweet