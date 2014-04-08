# This is a template for a Python scraper on Morph (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries. You can use whatever libraries are installed
# on Morph for Python (https://github.com/openaustralia/morph-docker-python/blob/master/pip_requirements.txt) and all that matters
# is that your final data is written to an Sqlite database called data.sqlite in the current working directory which
# has at least a table called data.
#!/usr/bin/env python

import scraperwiki
import requests
import lxml.html

html = requests.get("http://www.europarl.europa.eu/meps/en/full-list.html?filter=all&leg=").content
dom = lxml.html.fromstring(html)

for entry in dom.cssselect('.mep_details'):
    post = {
    'url': entry.cssselect('a')[0].get('href'),
    'politicalgroup': entry.cssselect('.name_pol_group')[0].text_content(),
    'name': entry.cssselect('.mep_name')[0].text_content(),
    }
    print post
scraperwiki.sqlite.save(unique_keys=['EirodeputatuSaraksts'], data={"EirodeputatuSaraksts": "Rakaris", "PatsSevSaimnieks": "Entuziasts"})
