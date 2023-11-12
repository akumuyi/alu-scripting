#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Gets the number of subscribers to the given subreddit."""
    # Define the Reddit API URL for the given subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set a custom User-Agent to avoid issues
    headers = {
        'User-Agent': 'MyRedditBot/1.0 (by YourUsername)'
    }
    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers)
        # Check if the response is successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract and return the number of subscribers
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            # Invalid subreddit or other issue
            return 0
    except requests.RequestException as e:
        # Request error
        print(f"Error: {e}")
        return 0
