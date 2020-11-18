from mdutils.mdutils import MdUtils
from mdutils import Html
from mdutils.tools.Link import Inline
import os
import sys
import requests


my_un = sys.argv[1]
my_pwd = sys.argv[2]
dijgo_file = MdUtils(file_name='../bookshelves/dijgo-article-to-read,md', title='My dijgo to read')
print(my_un)
r = requests.get('https://secure.diigo.com/api/v2/bookmarks?user=danieleandreis', auth=(my_un,my_pwd))
print(r)
dijgo_file.new_header(level=1, title='Link')
for y in sorted(r.json()):
    dijgo_file.new_header(level=2, title='Year: ' + y)
    dijgo_file.create_md_file()