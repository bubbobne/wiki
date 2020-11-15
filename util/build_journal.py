from mdutils.mdutils import MdUtils
from mdutils import Html
from mdutils.tools.Link import Inline
import os

daily_notes = os.listdir(path='../inbox/journal/dailynotes')
d = {}

for date in daily_notes:
    year, month, day = date[11:-2].split('-')
    if year in d:
        if month in d[year]:
            d[year][month].append(date)
        else:
            d[year][month] = [date]
    else:
        d[year] = {month: [date]}

print(d)

journal_file = MdUtils(
    file_name='../inbox/journal/journal.md', title='My journal')
journal_file.new_paragraph(
    "This is a collection of [daily](#daily_journal) and [weekly](#weekly-journal) notes.")

journal_file.new_header(level=1, title='Daily Journal')
for y in sorted(d.keys()):
    journal_file.new_header(level=2, title='Year: ' + y)
    for m in sorted(d[y].keys()):
        journal_file.new_header(level=2, title='mm: ' + m)
        # journal_file.new_list(Inline.new_link(
        #     i, i[:-4]) for i in sorted(d[y][m]))
        journal_file.new_list('[['+i[:-4]+']]' for i in sorted(d[y][m]))
journal_file.new_header(level=1, title='Weekly Journal')

journal_file.create_md_file()
