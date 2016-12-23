#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import traceback

import requests

if __name__ == "__main__":

    current_dir = os.path.dirname(os.path.abspath(__file__))
    id_path = os.path.join(current_dir, "newest_id.txt")
    print(current_dir)
    print(id_path)

    current_id = None
    try:
        with open(id_path, 'r') as f:
            current_id = f.read()
    except:
        pass

    print("Current ID: {}".format(current_id))
    print("Monitoring")

    subreddit = "python"
    url = "https://www.reddit.com/r/{}/new/.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    while True:
        try:
            response = requests.get(url, headers=headers)
            rss = response.json()

            newest_entry = rss['data']['children'][0]['data']
            newest_id = newest_entry['id']
            title = newest_entry['title']

            if current_id != newest_id:
                current_id = newest_id
                print("{} : {}".format(title[:40], current_id))
                with open(id_path, 'w') as f:
                    f.write(current_id)

        except Exception as e:
            traceback.print_exc()
            try:
                print(response.status_code)
                print(response.text)
            except:
                pass
        finally:
            time.sleep(60 * 5)
