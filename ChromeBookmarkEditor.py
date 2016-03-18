#!/usr/bin/python

import json
import os
import subprocess


class ChromeBookmarks(object):

	def __init__(self):
		self.epoch    = "13078095537020784" # Haven't reverse engineered the epoch date_added is calculated from so this is hard coded for now
		self.path     = self.get()
		self.json     = None
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
		self.json = js
		self.children = self.json['roots']['bookmark_bar']['children']
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

	def remove(self, title):
		for child in reversed(self.children):
			if child['name'] == title:
				self.children.remove(child)

	def write(self):
		bak_file = self.path + ".bak"
		os.remove(bak_file)
		self.json.pop("checksum", None)
		with open(self.path, "w") as outfile:
			json.dump(self.json, outfile)




