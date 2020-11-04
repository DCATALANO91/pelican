#!/usr/bin/env python
# -*- coding: utf-8 -*- #


AUTHOR = 'Dean'
SITENAME = 'Dean\'s Corner '
SITEURL = 'DCATALANO91.github.io'

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

SITELOGO = '/images/myimage.jpg'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Main Menu
MAIN_MENU = True
MENUITEMS = (('Archives', '/archives'),('Categories', '/categories'),('Tags', '/tags'),)


# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/dean-catalano-36bab4123/'),
          ('github', 'https://github.com/DCATALANO91'),
          )
		  
		  
DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'themes\\flex'