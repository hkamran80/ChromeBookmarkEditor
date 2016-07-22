# ChromeBookmarkEditor
Python module for easily adding, removing, and moving bookmarks on the Chrome bookmark menu in the context of the logged in user.

Currently working on adding support for adding folders / subfolders. Most of the implementation is there but haven't had time to finish. Pull requests are welcome.

Example Usage:
```
#!/usr/bin/python

from ChromeBookmarkEditor import ChromeBookmarks          # Import the module

bookmarks = ChromeBookmarks()                             # Create a Chrome Bookmarks instance to act on.

bookmarks.add("Reddit", "https://reddit.com")             # Add bookmark for Reddit
bookmarks.add("Apple", "https://www.apple.com", index=0)  # Add bookmark for Apple at 0th position
bookmarks.move("Apple", 0)                                # Move Apple bookmark back to 0th position
bookmarks.remove("Apple")                                 # Remove the Apple bookmark

bookmarks.write()                                         # Write changes to Bookmarks file

```
