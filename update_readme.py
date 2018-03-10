#! env python3
'''
add new row to table in README.md
'''
import StringIO
import os
import sys
import re
import commands
import urllib2
import re

# from decimal import Decimal
from optparse import OptionParser

ROW_MASK = """| {level} | <a href="{url}" target="_blank">{title}</a> | <a href="https://github.com/lumega/codewars/blob/master/{path}">{path}</a> |\n"""

parser = OptionParser()
parser.add_option('-n', '--name', help='set name to display')

(options, args) = parser.parse_args()
path = args[0]
level = path.split("/")[-2]
with open(path) as code:
    url = (code.readline())[1:].strip()

info = urllib2.urlopen(url).read()
match = re.search('<title>(.*?)</title>', info)
title = match.group(1) if match else 'Kata'
row = ROW_MASK.format(
    level=level,
    url=url,
    title=title.replace("|", "-"),
    path=path
)
print row

with open('README.md', "r") as f:
    contents = f.readlines()

for i, c in enumerate(contents):
    if "| %s" % level in c:
        break
with open('README.md', "w") as f:
    contents.insert(i, row)
    f.write("".join(contents))

