from nltk import sent_tokenize
from textblob import TextBlob
import pandas as pd
import nltk
import matplotlib.pyplot as plt


aspects = {
    'Product Quality': ['quality', 'durable', 'material', 'design'],
    'Delivery Experience': ['delivery', 'shipping', 'courier', 'time'],
    'Customer Service': ['service', 'support', 'help', 'customer care'],
    'Pricing': ['price', 'expensive', 'cheap', 'value'],
    'Packaging': ['packaging', 'box', 'wrap', 'condition']
}

def extract_aspect_sentences (review, aspects):
    aspect_sentences = {aspect: [] for aspect in aspects}
    sentences = sent_tokenize(review)
    for sentence in sentences:
        for aspect, keywords in aspects.items():
            if any(keyword in sentence.lower() for keyword in keywords):
                aspect_sentences[aspect].append(sentence)
    return aspect_sentences

def analyze_aspect_sentiments(aspect_sentences):
    aspect_scores = {}
    for aspect, sentences in aspect_sentences.items():
        if sentences:
            scores = [TextBlob(sentence).sentiment.polarity for sentence in sentences]
            aspect_scores[aspect] = sum(scores) / len(scores) # the average sentiment score
        else:
            aspect_scores[aspect] = 0 # if there are no sentences 0
    return aspect_scores

path = r'C:\Users\bahad\OneDrive\Desktop\Aspect-Based Sentiment Analysis\Sample_Customer_Reviews.csv'

df = pd.read_csv(path)
df = df.dropna(subset=['Customer_Review'])  # Remove rows with missing reviews


all_aspect_scores = []

for review in df['Customer_Review']:
    aspect_sentences = extract_aspect_sentences(review, aspects)
    aspect_scores = analyze_aspect_sentiments(aspect_sentences)
    all_aspect_scores.append(aspect_scores)

aspect_scores_df = pd.DataFrame(all_aspect_scores)
aspect_scores_df.to_csv('Aspect_Sentiment_Scores.csv', index=False)


# Example: Bar chart for average sentiment scores for each aspect
average_scores = aspect_scores_df.mean()
average_scores.plot(kind='bar')
plt.title('Average Sentiment Score by Aspect')
plt.ylabel('Sentiment Score')
plt.show()
