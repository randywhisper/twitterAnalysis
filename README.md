Twitter Analysis
======================
I test the code of user-timeline-tools from casmlab and collect the tweets from ten famous person, suck like Taylor Swift and Kobe Bryant, the famous singer and basketball player.

And I create another two files:</br>
```cloudWord.py``` ```tweetAmount.py```

[cloudWord.py](https://github.com/randywhisper/twitterAnalysis/blob/master/cloudword.py)  will make a word cloud of the tweets, and we can find the most frequency word in the tweets are "RT" and "U". If the stopwords contain "RT", we can get a more accurate result.
[tweetAmount.py](https://github.com/randywhisper/twitterAnalysis/blob/master/tweetAmount.py) will make a bar graph based on the data of tweets and fullname in the Database. We can find the relative frequency of tweets among the ten users.</br>
I have push the graph of cloudword and tweetAmount on Github.
Conclusion
---------------
As the data that we collect getting larger, we can make a more accurate analysis and predict. We can find out who use the Twitter most and how people post a tweet with, Phone or other Social Network? I have try to combine the data to analysis when people prefer to post tweets and what kind of topic people pay more attention to on the Twitter.

Recommendation
---------------
1. ```parseUserTimeLine.py```, there was an error in the main function when it load the data from the json file with a for-loop.
2. I am confused that I can not map the tweets to the twitter name when I query the database. So we can not find out which tweet is posted by the user.