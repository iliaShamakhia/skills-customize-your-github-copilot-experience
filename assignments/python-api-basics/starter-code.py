import json
from urllib.request import urlopen

API_URL = "https://jsonplaceholder.typicode.com/posts/{}"


def fetch_post(post_id):
    """Fetch a post from the JSONPlaceholder API."""
    pass


def print_post_summary(post):
    """Display a readable summary of a post."""
    pass


if __name__ == "__main__":
    post_id = int(input("Which post would you like to view? "))
    post = fetch_post(post_id)
    print_post_summary(post)
