#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import logging
import os
import time
import traceback

import requests

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)-3s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(os.environ.get('SUBREDDIT_MONITOR_LOG', 'INFO'))

requests_logger = logging.getLogger('requests')
requests_logger.setLevel('CRITICAL')

LAST_ID = 'last_id'
NAME = 'name'


def _pretty_json(data):
    """
    Pretty string of JSON data

    :param data: JSON data
    :return: Pretty string
    :rtype: str
    """

    return json.dumps(data, sort_keys=True, indent=2)


def _load_reddit_data(data_path):
    """
    Load reddit_data.json

    :param str data_path: Absolute path to reddit_data.json. Default to cwd/reddit_data.json
    :return: Reddit Data
    :rtype: list[dict]
    """

    with open(data_path, 'r') as f:
        reddit_data = json.load(f)

    return reddit_data


def _save_reddit_data(data_path, reddit_data):
    """
    Saves reddit_data.json

    :param str data_path: Absolute path to reddit_data.json
    :param list[dict] reddit_data: Reddit data to write
    """

    with open(data_path, 'w') as f:
        f.write(_pretty_json(reddit_data))


def _get_newest_entry(subreddit_name):
    """
    Extracts newest subreddit entry from JSON RSS

    :param str subreddit_name: Subreddit to get entry for
    :return: Extracted rss data
    :rtype: dict
    """

    url = "https://www.reddit.com/r/{}/new/.json".format(subreddit_name)
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    rss = response.json()

    return rss['data']['children'][0]['data']


def _on_new_entry(newest_entry, newest_id, title):
    """
    Performs action on a new entry

    :param dict newest_entry: Newest entry of RSS
    :param str newest_id: ID of newest entry
    :param str title: Title of newest entry
    """

    print("\tAction")


def _monitor(data_path, reddit_data):
    """
    Start monitoring all subreddits

    :param str data_path: Absolute path to reddit_data.json
    :param list[dict] reddit_data: Reddit data
    """

    while True:
        for index, subreddit in enumerate(reddit_data):
            name = subreddit[NAME]
            last_id = subreddit[LAST_ID]

            try:
                newest_entry = _get_newest_entry(name)
                newest_id = newest_entry['id']
                title = newest_entry['title']
                short_title = title[:40]

                if last_id != newest_id:
                    reddit_data[index][LAST_ID] = newest_id
                    _save_reddit_data(data_path, reddit_data)

                    msg = "[{} : {}] {}".format(name, newest_id, short_title)
                    logger.info(msg)
                    _on_new_entry(newest_entry, newest_id, title)

            except Exception as e:
                logger.error("AN ERROR OCCURRED")
                traceback.print_exc()

            finally:
                time.sleep(5)


def main(data_path=None):
    """
    Start program

    :param str data_path: Absolute path to reddit_data.json. Default to cwd/reddit_data.json
    """

    if not data_path:
        data_path = os.path.join(os.getcwd(), 'reddit_data.json')
    logger.info("Data path: '{}'".format(data_path))

    reddit_data = _load_reddit_data(data_path)
    logger.debug(_pretty_json(reddit_data))

    logger.info("== Monitoring Subreddits ==")
    _monitor(data_path, reddit_data)


if __name__ == "__main__":
    main()
