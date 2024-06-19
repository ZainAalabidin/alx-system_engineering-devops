#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """
    Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """

    # URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    # Parameters for pagination and limiting results
    params = {"after": after, "count": count, "limit": 100}

    # Make the request to Reddit's API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    try:
        results = response.json()  # Parse the JSON response
        if response.status_code == 404:  # Check if subreddit is invalid
            raise Exception
    except Exception:
        print("")  # Print empty string for invalid subreddit
        return

    # Extract data from the JSON response
    results = results.get("data")
    after = results.get("after")  # Get the 'after' token for pagination
    count += results.get("dist")  # Increment the count of posts processed

    # Process each post in the current batch
    for c in results.get("children"):
        title = (
            c.get("data").get("title").lower().split()
        )  # Get and split the post title into words
        for word in word_list:
            if word.lower() in title:
                # Count occurrences of the word in the title
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times  # Initialize count if word is new
                else:
                    instances[word] += times  # Increment count if word already seen

    # Check if there are more pages to fetch
    if after is None:
        if len(instances) == 0:
            print("")  # Print empty string if no words matched
            return
        # Sort and print the results
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        # Recursively fetch the next page of results
        count_words(subreddit, word_list, instances, after, count)


# Example usage:
# count_words('python', ['python', 'programming', 'code'])
