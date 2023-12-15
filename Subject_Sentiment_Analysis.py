import praw
import pandas as pd
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
import time

# Initialize the VADER sentiment analyzer
vader_analyzer = SentimentIntensityAnalyzer()

def clean_text(text):
    # Remove @mentions, # symbols, RT, hyperlinks, and colons
    return re.sub(r'@[A-Za-z0–9]+|#|RT[\s]+|https?:\/\/\S+|:', '', text)

def get_sentiment_vader(text):
    # Get the compound score from VADER
    compound_score = vader_analyzer.polarity_scores(text)['compound']
    return "Positive" if compound_score >= 0.05 else "Negative" if compound_score <= -0.05 else "Neutral"

def get_insight(score):
    return "Negative" if score < 0 else "Neutral" if score == 0 else "Positive"

# Define user agent
user_agent = "praw_SA"

# Create an instance of Reddit class
reddit = praw.Reddit(
    client_id="YtPgsGksq45lQquYsd5fyg",
    client_secret="sQivsOCQEKXn1lUdRpm6Cm2GkfikwA",
    user_agent=user_agent
)

# Create subreddit instance
subreddit_name = "unimelb"
subreddit = reddit.subreddit(subreddit_name)

# Creating lists for storing scraped data
comments_list = []

# Creating search query
subject_name = input("Enter the subject name: ")
subject_code = input("Enter the subject code: ")
search_q = f"{subject_name} {subject_code}"

start_time = time.time()

# Looping over posts and scraping data
for submission in subreddit.search(search_q, limit=None):
    submission.comments.replace_more(limit=None)

    for comment in submission.comments.list():
        if subject_name not in submission.title and subject_code not in submission.title and \
           subject_name not in comment.body and subject_code not in comment.body:
            break

        comments_list.append(clean_text(comment.body))

# Create a DataFrame with cleaned comments
df = pd.DataFrame({'Comments': comments_list})

# Analyze sentiment with TextBlob
df['Subjectivity'] = df['Comments'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
df['Polarity'] = df['Comments'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['Insight_TextBlob'] = df['Polarity'].apply(get_insight)

# Analyze sentiment with VADER
df['Sentiment_VADER'] = df['Comments'].apply(get_sentiment_vader)

# Display data
print(f"Subreddit: {subreddit.display_name}\nNumber of relevant comments: {len(df)}\n")
print(df)
print(f"Neutral comments (TextBlob): {df['Insight_TextBlob'].value_counts().get('Neutral', 0)}")
print(f"Positive:negative ratio (TextBlob) -> {df['Insight_TextBlob'].value_counts().get('Positive', 0)}:{df['Insight_TextBlob'].value_counts().get('Negative', 0)}")
print(f"Neutral comments (VADER): {df['Sentiment_VADER'].value_counts().get('Neutral', 0)}")
print(f"Positive:negative ratio (VADER) -> {df['Sentiment_VADER'].value_counts().get('Positive', 0)}:{df['Sentiment_VADER'].value_counts().get('Negative', 0)}")

# Save DataFrame to Excel file
excel_file_path = 'sentiment_analysis_results.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Results exported to {excel_file_path}")
print("--- %s seconds ---" % (time.time() - start_time))
