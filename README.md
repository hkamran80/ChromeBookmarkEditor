# ChromeBookmarkEditor
Python module for easily adding, removing, and moving bookmarks on the Chrome bookmark menu in the context of the logged in user.

Example Usage:
```
#!/usr/bin/python

from ChromeBookmarkEditor import ChromeBookmarks          # Import the module

bookmarks = ChromeBookmarks()                             # Create a Chrome Bookmarks instance to act on.

bookmarks.add("Reddit", "https://reddit.com")             # Add bookmark for Reddit
bookmarks.add("Apple", "https://www.apple.com", index=0)  # Add bookmark for Apple at 0th position
bookmarks.swap("Apple", "Reddit")                         # Swap positions of Apple and Reddit bookmarks
bookmarks.move("Apple", 0)                                # Move Apple bookmark back to 0th position
bookmarks.remove("Apple")                                 # Remove the Apple bookmark

bookmarks.write()                                         # Write changes to Bookmarks file

```

## Notes

- Chrome must be closed / re-opened for changes to appear if it is open at the time of modification.
- Chrome must be launched at least once for its ~/Libray/Application Support directories to be generated before modification.
I use the following snippet to launch Chrome for the first time. The `--no-first-run` flag blocks the annoying first-run prompts.
```
p = subprocess.Popen(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--no-first-run"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(4) # Allow app to launch. Not sure if this is needed but I do it anyways in case an older machine takes a while to launch the app.
p.kill()      # Kill app

```