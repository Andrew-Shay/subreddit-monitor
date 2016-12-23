# Subreddit Monitor

This is just a really simple script that I was testing. It will be used in a larger project.  
It simply:  
1) Gets the RSS feed of a subreddit eg [https://www.reddit.com/r/python/new/.rss](https://www.reddit.com/r/python/new/.rss)  
2) Converts the RSS XML to JSON with [xmltodict](https://github.com/martinblech/xmltodict)  
3) Grabs the ID of the newest thread  
4) Prints a message when a newer thread appears  
5) Sleeps 5 minutes  
6) Repeats  

This project is not pip installable

## Requirements
Python 3.5 or 2.7  
requests  
xmltodict  