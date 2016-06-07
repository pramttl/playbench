"""
usage : python2 geekbenchparser.py http://browser.primatelabs.com/geekbench3/4534575
"""

import sys,urllib2

from bs4 import BeautifulSoup

url = sys.argv[1]
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)


overall_table = soup.findAll("table", { "class" : "table geekbench3-show summary" })
print 'Single-Core Score: ' + str(overall_table[0].findAll('td')[1].contents[0])
print 'Multi-Core Score: ' + str(overall_table[0].findAll('td')[2].contents[0])


section_table = soup.findAll("table", { "class" : "table table-striped geekbench2-show section-performance" })
print 'Integer Performance Single-core '+ str(section_table[0].findAll('th')[1].contents[0]) 
print 'Integer Performance Multi-core '+ str(section_table[0].findAll('th')[4].contents[0])

print 'Floating Point Performance Single-core '+ str(section_table[1].findAll('th')[1].contents[0])
print 'Floating Point Performance Multi-core '+ str(section_table[1].findAll('th')[4].contents[0])

print 'Memory Performance Single-core '+ str(section_table[2].findAll('th')[1].contents[0])
print 'Memory Performance Multi-core '+ str(section_table[2].findAll('th')[4].contents[0])
