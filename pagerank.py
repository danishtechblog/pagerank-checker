#!/usr/bin/python
# -*- coding: utf-8 -*-
#       +-------------------------------------------+
#       | Title: Google Pagerank Checker v1.0       |
#       | Web: https://danish.tech                  |
#       | Support: https://forum.danish.tech        |
#       +-------------------------------------------+
#

import requests
import sys, os, re
from bs4 import BeautifulSoup

os.system("clear")

title = "P A G E R A N K  -  C H E C K E R  V1.0"

if len(sys.argv) < 2:
   print(title)
   print("--------------------------------------")
   print("Usage: ./test.py example.com")
   print
   print("---------------------------------------")
   exit(1)
   
domain = sys.argv[1]
url = requests.get("http://pr.eyedomain.com/pr/"+domain)
soup = BeautifulSoup(url.text, "html5lib")
item = soup.findAll("h1")[0].text

print(title)
print("-----------------------------------------")
print("Domain: %s " % domain)
print("Pagerank: %s " % item)
print("-----------------------------------------")
