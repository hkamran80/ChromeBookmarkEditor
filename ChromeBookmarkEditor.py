#!/usr/bin/python

from ScriptingBridge import SBApplication

class ChromeBookmarks(object):

	def __init__(self):
		self.chrome   = SBApplication.applicationWithBundleIdentifier_("com.google.Chrome")
		self.bar      = self.chrome.bookmarksBar()
		self.items    = self.bar.bookmarkItems()
		self.ids      = [item.id() for item in self.items]
		self.titles   = [item.title() for item in self.items]

	def add(self, title, url, index=-1):
		if title in self.titles:
			return
		if index == -1 or index > len(self.items):
			index = len(self.items)
		elif index < -1:
			index = 0
		if not self.ids:
			next_id = 1
		else:
			next_id = max(self.ids) + 1
		properties = dict(
			title=title,
			URL=url
		)
		bm = self.chrome.classForScriptingClass_("bookmark item").alloc().initWithProperties_(properties)
		if len(self.items) == 0:
			self.items.append(bm)
		else:
			self.items.insert(index, bm)
		self.ids.append(next_id)
		self.titles.append(title)

	def remove(self, title):
		if title not in self.titles:
			return
		for item in reversed(self.items):
			if item.title() == title:
				self.items.pop(item)
				return

	def removeAll(self):
		self.items,removeAllObjects()
		self.ids    = list()
		self.titles = list()

	def move(self, title, index):
		if title not in self.titles:
			return
		if index > len(self.items) or index == -1:
			index = len(self.items)
		elif index < -1:
			index = 0
		for item in self.items:
			if item.title() == title:
				to_mv = item
				break
		self.items.remove(to_mv)
		self.items.insert(index, to_mv)