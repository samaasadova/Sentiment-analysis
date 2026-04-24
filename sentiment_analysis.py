from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sqlite3
import pandas as pd

# Sentiment təhlili funksiyası
def analyze_sentiment(df):
    """
    Bu funksiya datasetdəki hər tweetin sentimentini analiz edir və müsbət, mənfi, ya neytral olaraq təyin edir.
    """
    analyzer = SentimentIntensityAnalyzer()
    df['sentiment'] = df['text'].apply(lambda tweet: analyzer.polarity_scores(tweet)['compound'])
    df['sentiment_label'] = df['sentiment'].apply(lambda score: 'Positive' if score > 0 else ('Negative' if score < 0 else 'Neutral'))
    return df

# SQLite verilənlər bazasında cədvəl yaratma funksiyası
def create_table():
    """
    SQLite verilənlər bazasında cədvəl yaradılır, əgər varsa, heç bir şey etməz.
    """
    conn = sqlite3.connect('sentiment_analysis.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
        tweet_id INTEGER PRIMARY KEY,
        tweet_text TEXT,
        sentiment REAL,
        sentiment_label TEXT
    )
    ''')

    conn.commit()
    conn.close()

# SQLite verilənlər bazasına məlumatları yazmaq
def save_to_sqlite(df):
    """
    Sentiment təhlilini edilmiş məlumatları SQLite verilənlər bazasına yazır.
    """
    conn = sqlite3.connect('sentiment_analysis.db')
    cursor = conn.cursor()

    for index, row in df.iterrows():
        cursor.execute("INSERT INTO tweets (tweet_text, sentiment, sentiment_label) VALUES (?, ?, ?)",
                       (row['text'], row['sentiment'], row['sentiment_label']))

    conn.commit()
    conn.close()

# Sentiment təhlilindən alınan məlumatları CSV faylında saxlayır
def save_to_csv(df, processed_data_path):
    """
    Bu funksiya sentiment təhlilini edilmiş məlumatları CSV faylında saxlayır.
    """
    df.to_csv(processed_data_path, index=False)

# SQLite verilənlər bazasından məlumatları çəkmək
def fetch_data_from_sqlite():
    """
    SQLite verilənlər bazasından məlumatları çəkir və DataFrame şəklində qaytarır.
    """
    conn = sqlite3.connect('sentiment_analysis.db')
    query = "SELECT tweet_text, sentiment, sentiment_label FROM tweets"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
