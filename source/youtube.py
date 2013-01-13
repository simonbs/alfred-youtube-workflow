##
# By @simonbs
# http://simonbs.dk/
##

import re
import sys
import urllib
import json
from to_xml import list_to_xml

#  Supported values for order by are
#  - relevance, viewCount, published, rating
def search(terms, max_results = 0, orderby = "relevance"):
  url = "https://gdata.youtube.com/feeds/api/videos?v=2&alt=jsonc&q=%s&orderby=%s" % (terms, orderby)
  if max_results > 0:
    url = "%s&max-results=%s" % (url, max_results)
  conn = urllib.urlopen(url)
  response = conn.read()
  items = json.loads(response)["data"]["items"]
  return search_results(items)
  
def search_results(items):
  results = search_results_list(items)
  print list_to_xml(results)

def search_results_list(items):
  results = []
  for item in items:
    result = parse_item(item)
    if result["uid"] is not None:
      results.append(result)
  return results
    
def parse_item(item):
  video_id = item["id"]
  return { "uid": video_id,
           "arg": video_id,
           "title": item["title"],
           "subtitle": "by %s (%s)" % (item["uploader"], seconds_to_string(item["duration"])),
           "icon": "icon.png" }
    
def seconds_to_string(seconds):
  hours = seconds / 3600
  minutes = (seconds % 3600) / 60
  seconds = seconds % 3600 % 60
  result = ""
  if hours > 0:
    result = "%sh" % (hours)
  if minutes > 0:
    if hours > 0:
      result = "%s " % (result)
    result = "%s%sm" % (result, minutes)
  if seconds > 0:
    if hours > 0 and minutes == 0 or minutes > 0:
      result = "%s " % (result)
    result = "%s%ss" % (result, seconds)
  return result
  
if __name__ == "__main__":
  if len(sys.argv) == 2:
    search(sys.argv[1])
  else:
    print "Syntax is:\n  python youtube.py \"Your query\""