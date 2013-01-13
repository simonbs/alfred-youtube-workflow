##
# By @simonbs
# http://simonbs.dk/
##

import re
import gdata.youtube
import gdata.youtube.service
from to_xml import list_to_xml
import sys

#  Supported values for order by are
#  - relevance, viewCount, published, rating
def search(terms, max_results = 0, orderby = "relevance"):
  yt_service = gdata.youtube.service.YouTubeService()
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.vq = terms
  query.orderby = orderby
  query.racy = "include"
  if max_results > 0:
    query.max_results = max_results
  feed = yt_service.YouTubeQuery(query)
  return search_results(feed)
  
def search_results(feed):
  results = search_results_list(feed)
  print list_to_xml(results)

def search_results_list(feed):
  results = []
  for entry in feed.entry:
    result = parse_entry(entry)
    if result["uid"] is not None:
      results.append(parse_entry(entry))
  return results
    
def parse_entry(entry):
  title = entry.media.title.text
  video_id = get_video_id(entry)
  return { "uid": video_id,
           "arg": video_id,
           "title": entry.media.title.text.decode("utf-8"),
           "subtitle": "%s" % seconds_to_string(int(entry.media.duration.seconds)),
           "icon": "icon.png" }
    
def get_video_id(entry):
  r = re.compile("http://gdata.youtube.com/feeds/videos/(\w+)</ns0:id>")
  m = r.search(entry.id.ToString())
  if m is not None:
    return m.group(1)
    
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