# SubredditAnalyzer

This repo contains the code used for my fourth project at Metis Data Science bootcamp. Here I apply topic modeling and NLP techniques to study the spectrum of Reddit political subreddits. My spectrum (from right to left) spans covers The_Donald, conservative, politics, LateStageCapitalism, and FULLCOMMUNISM.

In the utils folder you find a script that (when edited with relevant subreddits and provided with an API key in the credentials file) will scrape the top 100 posts of all time for all comments and upload to a local MongoDB database. Many thanks to the people of the [Praw](https://github.com/praw-dev/praw/blob/master/docs/index.rst) project for their excellent documentation and API wrapper. 

In the Exploration notebook, I have the code used to pull the comments from the MongoDB database, do a decent job cleaning to perform Latent Semantic Analysis. The final thoughts are in the form of heatmaps of subreddit overlaps. These topics show an interesting connection in that the more extreme subreddits in The_Donald and FULLCOMMUNISM do not overlap with any others meaningfully, while the others do. 
