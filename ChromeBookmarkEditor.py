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
		Checks to see Bookmarks json file exists.. 

		Returns:
			Expanded path to ~/Library/Application Support/Google/Chrome/Default/Bookmarks

		"""
		return os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/Bookmarks')
