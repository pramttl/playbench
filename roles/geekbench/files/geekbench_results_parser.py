"""
usage : python2 geekbenchparser.py http://browser.primatelabs.com/geekbench3/4534575

Returns comma separated list of scores
"""

import sys,urllib2

from bs4 import BeautifulSoup

url = sys.argv[1]
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)


overall_table = soup.findAll("table", { "class" : "table geekbench3-show summary" })

scores = []
scores.append(str(overall_table[0].findAll('td')[1].contents[0]))
scores.append(str(overall_table[0].findAll('td')[2].contents[0]))

section_table = soup.findAll("table", { "class" : "table table-striped geekbench2-show section-performance" })
scores.append(str(section_table[0].findAll('th')[1].contents[0]))
scores.append(str(section_table[0].findAll('th')[4].contents[0]))
scores.append(str(section_table[1].findAll('th')[1].contents[0]))
scores.append(str(section_table[1].findAll('th')[4].contents[0]))
scores.append(str(section_table[2].findAll('th')[1].contents[0]))
scores.append(str(section_table[2].findAll('th')[4].contents[0]))

#print 'Single-Core Score, Multi-Core Score, Integer Perf Single-core, Integer Perf Multi-core, Float Perf Single-core, Float Perf Multi-core, Memory Single Core, Memory Multi Core'
print "\t".join(scores)
