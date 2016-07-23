# ChromeBookmarkEditor
Python module for easily adding, removing, and moving bookmarks on the Chrome bookmark menu in the context of the logged in user.

Example Usage:
```
#!/usr/bin/python

from ChromeBookmarkEditor import Chrome                                           # Import the module

chrome = Chrome()                                                                 # Create a Chrome instance to act on.

bookmarks_bar   = chrome.bookmarksBar                                             # Folder containing bookmarks for main bookmarks bar
other_bookmarks = chrome.otherBookmarks                                           # Folder containing bookmarks from "Other Bookmarks" dropdown

bookmarks_bar.addBookmark("Google", "http://google.com")                          # Add bookmark for Google to main bookmarks bar
other_bookmarks.addFolder("Fav Links")                                            # Add folder titled "Fav Links" to "Other Bookmarks" dropdown

some_bookmark   = bookmarks_bar.getBookmark("Google")                             # Get reference to bookmark
some_folder     = other_bookmarks.getFolder("Fav Links")                          # Get reference to folder
nested_folder   = some_folder.addFolder("Subreddits")                             # Add nested folder titled "Subreddits" to "Fav Links" folder
nested_bookmark = nested_folder.addBookmark("news", "https://reddit.com/r/news/") # Add bookmark to nested folder

some_bookmark.title()                                                             # Get title of bookmark
>>> u'Google'
some_bookmark.URL()                                                               # Get URL of bookmark
>>> u'http://google.com'
some_bookmark.setTitle_("Reddit")                                                 # Set bookmark title to "Reddit"
some_bookmark.setURL_("https://reddit.com")                                       # Set bookmark URL to "https://reddit.com"
some_bookmark.title()                                                             # Get updated title of bookmark
>>> u'Reddit'
some_bookmark.URL()                                                               # Get updated URL of bookmark
>>> u'https://reddit.com'
														                          # Folders can also have their titles updated
some_folder.title()                                                               # Get title of folder
>>> u'Fav Links'
some_folder.setTitle_("Favorites")                                                # Set folder title to "Favorites"
some_bookmark.title()                                                             # Get updated title of folder
>>> u'Favorites'

nested_bookmark.delete()                                                          # Remove bookmark
some_folder.delete()                                                              # Remove folder

bookmark_bar.removeAll()                                                          # Remove all bookmarks and folders from main bookmarks bar
```
