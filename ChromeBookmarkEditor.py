#!/usr/bin/python

# Hide python rocket ship from popping up in Dock when run.
import AppKit
info = AppKit.NSBundle.mainBundle().infoDictionary()
info['CFBundleIconFile'] = u'PythonApplet.icns'
info['LSUIElement'] = True

from ScriptingBridge import SBApplication

chrome   = SBApplication.applicationWithBundleIdentifier_("com.google.Chrome")

class ChromeBookmarks(object):

	def __init__(self):
		self.chrome   = SBApplication.applicationWithBundleIdentifier_("com.google.Chrome")
		self.bar      = self.chrome.bookmarksBar()
		self.items    = self.bar.bookmarkItems()
		self.titles   = [item.title() for item in self.items]

	def add(self, title, url, index=-1):
		if title in self.titles:
			return
		elif index < -1:
			index = 0
		properties = dict(
			title=title,
			URL=url
		)
		bm = self.chrome.classForScriptingClass_("bookmark item").alloc().initWithProperties_(properties)
		if len(self.items) == 0 or index == -1 or index > len(self.items):
			self.items.append(bm)
		else:
			self.items.insert(index, bm)
		self.titles.append(title)

	def remove(self, title):
		if title not in self.titles:
			return
		for index, item in enumerate(self.items):
			if item.title() == title:
				self.titles.remove(item.title())
				self.items.pop(index)
				return

	def removeAll(self):
		self.items.removeAllObjects()
		self.titles = list()

	def move(self, title, index):
		if title not in self.titles:
			return
		elif index < -1:
			index = 0
		for i, item in enumerate(self.items):
			if item.title() == title:
				url = item.URL()
				break
		self.items.pop(i)
		properties = dict(
			title=title,
			URL=url
		)
		to_mv = self.chrome.classForScriptingClass_("bookmark item").alloc().initWithProperties_(properties)
		if index > len(self.items) or index == -1:
			self.items.append(to_mv)
		else:
			self.items.insert(index, to_mv)

class ChromeApp(object):

	def __init__(self):
		self.chrome  = SBApplication.applicationWithBundleIdentifier_("com.google.Chrome")

class Chrome(ChromeApp):

	def __init__(self):
		super(Chrome, self).__init__()
		self.bookmarksBar = Folder(self.chrome.bookmarksBar())
		self.otherBookmarks = Folder(self.chrome.otherBookmarks())

class Folder(ChromeApp):

	def __init__(self, root):
		super(Folder, self).__init__()
		self.root    = root
		self.folders = self.root.bookmarkFolders()
		self.bookmarks   = self.root.bookmarkItems()

	def getFolder(self, title):
		for folder in self.folders:
			if str(folder.title()) == title:
				return Folder(folder)
		return None

	def getBookmark(self, title):
		for bookmark in self.bookmarks:
			if str(bookmark.title()) == title:
				return bookmark
		return None

	def getItemByIndex(self, index):
		for folder in self.folders:
			if int(folder.index()) == index:
				return (folder, "Folder")
		for bookmark in self.bookmarks:
			if int(bookmark.index()) == index:
				return (bookmark, "Bookmark")
		return None

	def addFolder(self, title):
		properties = dict(
			title=title
		)
		new_folder = self.chrome.classForScriptingClass_("bookmark folder").alloc().initWithProperties_(properties)
		self.folders.append(new_folder)

	def addBookmark(self, title, url):
		properties = dict(
			title=title,
			URL=url
		)
		new_bookmark = self.chrome.classForScriptingClass_("bookmark item").alloc().initWithProperties_(properties)
		self.bookmarks.append(new_bookmark)

	def removeFolder(self, title):
		pass

	def removeBookmark(self, title):
		pass

