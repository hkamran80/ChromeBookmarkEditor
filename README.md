# ChromeBookmarkEditor
Python module for easily adding, removing, and moving bookmarks on the Chrome bookmark menu in the context of the logged in user.

Example Usage:
```
#!/usr/bin/python

from ChromeBookmarkEditor import ChromeBookmarks          # Import the module

bookmarks = ChromeBookmarks()                             # Create a Finder sidebar instance to act on.

bookmarks.add("Reddit", "https://reddit.com")             # Add bookmark for Reddit
bookmarks.add("Apple", "https://www.apple.com", index=0)  # Add bookmark for Apple at 0th position
bookmarks.swap("Apple", "Reddit")                         # Swap positions of Apple and Reddit bookmarks
bookmarks.remove("Apple")                                 # Remove the Apple bookmark

bookmarks.write()                                         # Write changes to Bookmarks file

```

## Notes

- Chrome must be closed / re-opened for changes to appear if it is open at the time of modification.
- Chrome must be launched at least once for its ~/Libray/Application Support directories to be generated before modification.
  (This could be scripted using subprocess.call('open', '/Application/Google Chrome.app') but this is left up to the user.)
