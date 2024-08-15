#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively returns a list of titles of all hot articles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        hot_list.extend([child['data']['title'] for child in children])
        after = data.get('after')

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

