To get a list of lines added or removed for a set of users for all commits and pushes in GitHub, you can use the GitHub API along with the requests library in Python. Here's an example program that demonstrates this:

```python
import requests

def get_code_changes(username):
    # Make a request to the GitHub API to get the user's commit history
    response = requests.get(f'https://api.github.com/users/{username}/events')

    # Check if the request was successful
    if response.status_code == 200:
        events = response.json()

        # Initialize a list to store the code changes
        code_changes = []

        # Iterate over the events to find push events
        for event in events:
            if event['type'] == 'PushEvent':
                # Iterate over the commits in the push event
                for commit in event['payload']['commits']:
                    # Get the commit details
                    commit_details = requests.get(commit['url']).json()

                    # Get the lines added and removed from the commit
                    lines_added = commit_details['stats']['additions']
                    lines_removed = commit_details['stats']['deletions']

                    # Add the code changes to the list
                    code_changes.append((commit['sha'], lines_added, lines_removed))

        # Return the list of code changes
        return code_changes
    else:
        return None

# Set of usernames
usernames = ['user1', 'user2', 'user3']

# Iterate over the usernames and get the code changes for each user
for username in usernames:
    code_changes = get_code_changes(username)
    if code_changes:
        print(f'Code changes for {username}:')
        for commit in code_changes:
            sha, lines_added, lines_removed = commit
            print(f'Commit: {sha}')
            print(f'Lines added: {lines_added}')
            print(f'Lines removed: {lines_removed}')
            print('---')
    else:
        print(f'Failed to retrieve code changes for {username}')
```

Make sure to replace the `usernames` list with the actual usernames you want to retrieve code changes for. The program will make requests to the GitHub API to fetch the commit history for each user and retrieve the lines added and removed from each commit. It will then print the code changes for each user, including the commit SHA, lines added, and lines removed.
