##
# By @simonbs
# http://simonbs.dk/
##

import re
import sys
import urllib
import json
from to_xml import list_to_xml

# Returns the top rated videos on YouTube.
def top_rated_videos(max_results = 0):
  return results("https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc", max_results)

# Returns the top favorited videos on YouTube.
def top_favorited_videos(max_results = 0):
  return results("https://gdata.youtube.com/feeds/api/standardfeeds/top_favorites?v=2&alt=jsonc", max_results)
  
# Returns the most viwed videos on YouTube.
def most_viewed_videos(max_results = 0):
  return results("https://gdata.youtube.com/feeds/api/standardfeeds/most_viewed?v=2&alt=jsonc", max_results)
  
# Returns the most popular videos on YouTube.
def most_popular_videos(max_results = 0):
  return results("https://gdata.youtube.com/feeds/api/standardfeeds/most_popular?v=2&alt=jsonc", max_results)

# Returns the most recent videos on YouTube.
def most_recent_videos(max_results = 0):
  return results("https://gdata.youtube.com/feeds/api/standardfeeds/most_recent?v=2&alt=jsonc", max_results)
  
# Returns the most discussed videos on YouTube.
def most_discussed_videos(max_results = 0):
  return results("https://gdata.youtube.com/feeds/api/standardfeeds/most_discussed?v=2&alt=jsonc", max_results)

# Returns the most responded videos on YouTube.
def most_responded_videos(max_results = 0):
  return results("https://gdata.youtube.com/feeds/api/standardfeeds/most_responded?v=2&alt=jsonc", max_results)

# Returns the recently featured videos on YouTube.
def recently_featured_videos(max_results = 0):
  return results("https://gdata.youtube.com/feeds/api/standardfeeds/recently_featured?v=2&alt=jsonc", max_results)

# Searches YouTube for results matching the terms and returns the results.
# Supported values for orderby are
# - relevance, viewCount, published, rating
def search_videos(terms, max_results = 0, orderby = "relevance"):
  url = "https://gdata.youtube.com/feeds/api/videos?v=2&alt=jsonc&q=%s&orderby=%s" % (terms, orderby)
  return results(url, max_results)

# Returns XML parsed results for the specified URL and maximum amount of results.
def results(url, max_results):
  url = max_results_url(url, max_results)
  items = items_at_url(url)
  return xml_results(items)
  
# Appends the maximum results to a URL.
# The maximum results is only added if the value is between 1 and 50
# which is the range Google allows.
# If the max results falls out of this range, Googles default max results is used.
def max_results_url(url, max_results):
  if max_results >= 1 and max_results <= 50:
    url = "%s&max-results=%s" % (url, max_results)
  return url
  
# Loads the items at the specified URL.
def items_at_url(url):
  conn = urllib.urlopen(url)
  response = conn.read()
  items = json.loads(response)["data"]["items"]
  return items
  
# Parses a list results into XML for Alfred.
def xml_results(items):
  results = results_list(items)
  print list_to_xml(results)

# Returns a list items loaded from the Google API as parsed items.
# A video is only included if it has a valid uid, meaning that it has a valid video ID.
def results_list(items):
  results = []
  for item in items:
    result = parse_item(item)
    if result["uid"] is not None:
      results.append(result)
  return results
  
# Parses a YouTube item into a dictionary for Alred and returns the dictionary.
def parse_item(item):
  video_id = item["id"]
  return { "uid": video_id,
           "arg": video_id,
           "title": item["title"],
           "subtitle": "by %s (%s)" % (item["uploader"], seconds_to_string(item["duration"])),
           "icon": "icon.png" }
    
# Converts seconds into a string cotnaing hours, minutes and seconds and returns the string.
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
  
# Main
if __name__ == "__main__":
  if len(sys.argv) == 2:
    top_rated_videos()
    # search_videos(sys.argv[1])
  else:
    print "Syntax is:\n  python youtube.py \"Your query\""