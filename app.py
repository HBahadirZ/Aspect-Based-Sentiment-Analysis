from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/sentiment_data')
def sentiment_data():
    df = pd.read_csv('Aspect_Sentiment_Scores.csv')
    sentiment_summary = {
        'Product_Quality': df['Product Quality'].mean(),
        'Delivery_Experience': df['Delivery Experience'].mean(),
        'Customer_Service': df['Customer Service'].mean(),
        'Pricing': df['Pricing'].mean(),
        'Packaging': df['Packaging'].mean(),
        'Positive': (df > 0).sum().sum(),
        'Negative': (df < 0).sum().sum(),
        'Neutral': (df == 0).sum().sum()
    }
    return jsonify(sentiment_summary)

if __name__ == '__main__':
    app.run(debug=True)
