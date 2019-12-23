# Skyranker

I'm really interested in how people are ranking the Star Wars movies.
My intent with this app is to pull rankings of the movies from Twitter and look for patterns.


## Configuration

You'll need a `.env` file in the home directory with the following Twitter API keys: `CONSUMER_KEY`, `CONSUMER_SECRET`, `ACCESS_TOKEN`, and `ACCESS_SECRET`.

// TODO 
1. Make a tweet database
2. Parse tweets to determine rankings (include 9-only ranking, and full ranking for those that rank Solo et al.)
3. Search users to get additional info
4. Wonder if there's a way to normalize likes (likes/day, or some such). Most likes will come the first day, so older tweets will fall off, but newer tweets won't have enough data.
5. 

// Thoughts
Attributes to track:
1. Did they rank Solo/Rogue One
2. Did they rank The Mandalorian
3. How many recent tweets are about star wars (or tweets around the same time)
4. Followers
5. Tweet likes/retweets
