
# Reddit Sentiment Analysis

## Overview

This is a simple Python script that utilizes the PRAW library to scrape comments from a specified subreddit on Reddit, analyzes the sentiment of the comments using both TextBlob and VADER (NLTK's sentiment analysis tool), and exports the results to an Excel file.


## Required dependencies

- Python 3.x
- PRAW (`pip install praw`)
- pandas (`pip install pandas`)
- TextBlob (`pip install textblob`)
- NLTK (`pip install nltk`)

## Output

The script provides sentiment analysis using both TextBlob and VADER. It categorizes comments as Positive, Negative, or Neutral and exports the results to an Excel file for further analysis.

## Acknowledgments

- PRAW: The Python Reddit API Wrapper
- NLTK: Natural Language Toolkit
- TextBlob: Simplified Text Processing

Feel free to contribute, report issues, or suggest improvements!

## Rationale...
This concept started when I wanted to find subjects to up my WAM for my uni degree... I decided to experiment with a straightforward sentiment analysis approach, focusing on posts related to a particular subject within the r/unimelb subreddit. The goal was to gauge the majority sentiments and opinions on a specific subject within the university community :)
