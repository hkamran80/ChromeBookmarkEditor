#!/usr/bin/python

import json
import os
import subprocess


class ChromeBookmarks(object):

	def __init__(self):
		self.path     = self.get()
		self.ids      = None
		self.children = None

	def get(self):
		"""
		Gets expanded path to Chrome bookmarks json file.

		Returns:
			Expanded path to ~/Library/Application Support/Google/Chrome/Default/Bookmarks

		"""
		return os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/Bookmarks')
