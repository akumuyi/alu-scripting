#!/usr/bin/python3
""" This script takes a subreddit name as input
and returns the number of subscribers to that subreddit.

Usage:
    python number_of_subscribers.py <subreddit>

Args:
    subreddit (str): The name of the subreddit to
    get the number of subscribers for.

Returns:
    int: The number of subscribers to the given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Gets the number of subscribers to the given subreddit.

    Args:
        subreddit (str): The name of the subreddit to get
        the number of subscribers for.

    Returns:
        int: The number of subscribers to the given subreddit.
    """

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


if __name__ == "__main__":
    # Get the subreddit name from the command line argument
    subreddit = sys.argv[1]

    # Get the number of subscribers to the subreddit
    subscribers = number_of_subscribers(subreddit)

    # Print the number of subscribers to the console
    print(f"The subreddit {subreddit} has {subscribers} subscribers.")
