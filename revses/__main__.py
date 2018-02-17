#!/usr/bin/env python3
from revses import ReviewSession

def main():
    root_directory = '/home/lyco/Pictures'
    directories = {
        'good': 'GOOD',
        'reviewed': 'ALL',
    }

    settings = {
        'extentions': ['jpeg', 'jpg', 'png'],
        'size': [432, 432],
    }

    session = ReviewSession(root_directory, directories, settings)

if __name__ == "__main__":
    main()
