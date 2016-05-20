#!/usr/bin/python

# Hide python rocket ship from popping up in Dock when run.
import AppKit
info = AppKit.NSBundle.mainBundle().infoDictionary()
info['CFBundleIconFile'] = u'PythonApplet.icns'
info['LSUIElement'] = True

from ScriptingBridge import SBApplication

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

class Chrome(object):
	pass

def Bar(Chrome):
	pass

def Folder(Chrome):
	pass

def Item(Chrome):
	pass
