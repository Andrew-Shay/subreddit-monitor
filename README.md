# Subreddit Monitor

This is just a really simple script that I was testing. It will be used in a larger project.  
It simply:  
1) Gets the RSS feed of multiple subreddits eg [https://www.reddit.com/r/python/new/.json](https://www.reddit.com/r/python/new/.json)  
3) Grabs the ID of the newest thread  
4) Prints a message and performs an action when a newer thread appears  
5) Sleeps 5 seconds  
6) Repeats  

This project is not pip installable

## Configure

One or more subreddits can be monitored.  
This is controlled via `reddit_data.json`. It maps a name of a subreddit to the last id that was recorded.  
By default the file should be named `reddit_data.json` and be in the cwd.  
This will be automatically rewritten when new data is found.  

```json
[
  {
    "last_id": null,
    "name": "news"
  },
  {
    "last_id": null,
    "name": "aww"
  }
]
```

### Environment Variables
- `SUBREDDIT_MONITOR_LOG` controls logging level eg `DEBUG`, `INFO`, `ERROR`
- `SUBREDDIT_MONITOR_SLEEP` seconds to sleep before checking next subreddit eg `5`, `120`
 - Warning: Anything less than `5` may cause errors
- `SUBREDDIT_MONITOR_DATA` absolute path to reddit data file eg `/Users/foo.bar/Documents/reddit_data.json`

## Using this project
This is just a sample project, so you should download the source code and modify it to fit your needs.  
Logic is in `subreddit_monitor/__main__.py` and you can simply modify `_on_new_entry()` to get started.

## Requirements
Python 3.5 or 2.7  
requests  