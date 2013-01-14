YouTube Workflow for Alfred 2.0
======

A workflow for Alfred 2.0 which lets the user search for YouTube videos and have them returned to Alfred.

![](http://f.cl.ly/items/0c1m1O1o202S2N0f3A0q/Sk%C3%A6rmbillede%202013-01-13%20kl.%2018.34.26.png)

Usage
======

Typing `youtube` followed by a search query will show the results for the query. For example, `youtube rebecca black` will search for Rebecca Black videos.

Googles default amount of max results are used and the videos are ordered by relevance. This can be changed in the workflow by opening the script filter and editing the last line a bit.

	print(search("{query}", 0, "relevance"))

The first parameter is the search query. Don't change this. The second parameter, where it says 0, is the maximum amount of results to return. The default is zero, which causes the workflow to use Googles maximum amount of results. The third parameter is the ordering. By default videos are ordered by relevance. Possible values for this parameter are:

- relevance
- viewCount
- published
- rating

Commands
=====

Below is a list of the commands that the workflow provides. Parameters in brackets are required.

- **youtube (query)** Searches YouTube for videos matching the query.
- **youtubetoprated** Shows the top rated videos.
- **youtubetopfavorited** Shows the most favorited videos.
- **youtubemostviewed** Shows the most viewed videos.
- **youtubemostpopular** Shows the most popular videos.
- **youtubemostrecent** Shows the most recent videos.
- **youtubemostdiscussed** Shows the most discussed videos.
- **youtubemostresponded** Shows the videos with most responds.
- **youtuberecentlyfeatured** Shows videos which have recently been featured.
- **channel (user name)** Shows videos on a users channel.

Some of the above commands may have long names but notice that they all begin with *youtube* so writing just that will show all the other commands and thereby make them easy to access.

About
=====

This workflow is developed by [@simonbs](http://twitter.com/simonbs)