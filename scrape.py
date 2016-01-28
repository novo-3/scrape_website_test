from lxml import html
import requests

page = requests.get('http://www.csimfunds.com')
tree = html.fromstring(page.content)

