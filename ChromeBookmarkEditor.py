#!/usr/bin/python

import json
import os
import subprocess


class ChromeBookmarks(object):

	def __init__(self):
		self.epoch    = "13078095537020784" # Haven't reverse engineered the epoch date_added is calculated from so this is hard coded for now
		self.path     = self.get()
		self.ids      = None
		self.children = None
		self.read()

	def get(self):
		"""
		Gets expanded path to Chrome bookmarks json file.

		Returns:
			Expanded path to ~/Library/Application Support/Google/Chrome/Default/Bookmarks

		"""
		return os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/Bookmarks')

	def read(self):
		with open(self.path, "r") as infile:
			js = json.load(infile)
		self.children = js['roots']['bookmark_bar']['children']
		self.ids = [bm['id'] for bm in self.children]

	def add(self, title, url):
		new_child = dict(
			date_added=self.epoch,
			id=(max(self.ids) + 1),
			name=title,
			type="url",
			url=url,
		)
		self.children.append(new_child)





