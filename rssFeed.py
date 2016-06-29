# use six module to make code for both python2 & python3:
from six.moves import urllib


from bs4 import BeautifulSoup

req = urllib.request.urlopen('http://www.nationaljournal.com/politics?rss=1')

xml = BeautifulSoup(req, 'xml')

for item in xml.findAll('link')[3:]:
   url = item.text
   news = urllib.request.urlopen(url).read()
   print news
   print 20*"#"