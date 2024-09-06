
# Aspect-Based Sentiment Analysis Dashboard

This project is an Aspect-Based Sentiment Analysis Dashboard designed to analyze customer reviews and display the sentiment scores of different aspects such as Product Quality, Delivery Experience, Customer Service, Pricing, and Packaging. The dashboard provides insights into customer feedback trends using interactive visualizations.

## Features

- **Aspect-Based Sentiment Analysis**: Analyzes sentiments for different aspects mentioned in customer reviews.
- **Interactive Visualizations**: Displays data using bar charts and pie charts powered by Plotly for a better understanding of customer sentiment.
- **Real-Time Data Fetching**: Connects to a backend server using Flask to fetch and display up-to-date data dynamically.

## Project Structure

- **`Aspect_based_sentiment_analysis.py`**: Script to analyze customer reviews for sentiment on various aspects and save the results in `Aspect_Sentiment_Scores.csv`.
- **`app.py`**: Flask backend server script to serve the sentiment data as a JSON endpoint (`/sentiment_data`).
- **`index.html`**: Frontend HTML dashboard file that fetches data from the Flask server and displays interactive visualizations.
- **`Aspect_Sentiment_Scores.csv`**: CSV file containing the sentiment scores for different aspects.

## Setup Instructions

### Prerequisites

- Python 3.x
- Required Python Libraries: 
  - Flask
  - pandas
  - nltk
  - textblob

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Install the Required Libraries**:

   ```bash
   pip install Flask pandas nltk textblob
   ```

3. **Download NLTK Data**:

   Open a Python shell and run:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')
   ```

4. **Run the Sentiment Analysis**:

   Run the `Aspect_based_sentiment_analysis.py` script to generate the `Aspect_Sentiment_Scores.csv` file.

   ```bash
   python Aspect_based_sentiment_analysis.py
   ```

5. **Start the Flask Server**:

   Run the Flask server using the `app.py` script:

   ```bash
   python app.py
   ```

6. **Open the Dashboard**:

   Open the `index.html` file in a web browser and ensure that the Flask server is running to view the interactive dashboard.

## How to Use

1. **Upload or Input Customer Reviews**: Update the `Sample_Customer_Reviews.csv` file with new customer reviews.
2. **Run Analysis**: Execute the `Aspect_based_sentiment_analysis.py` script to process the reviews and generate sentiment scores.
3. **Visualize Results**: Open the `index.html` file in a browser to see the sentiment analysis results in a dashboard format.

## License

:)

## Acknowledgments

- This project uses [TextBlob](https://textblob.readthedocs.io/en/dev/) for sentiment analysis.
- Special thanks to [Plotly](https://plotly.com/) for providing excellent visualization tools.
