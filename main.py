import os
from data_processing import load_data
from sentiment_analysis import analyze_sentiment, save_to_sqlite, save_to_csv
from visualization import plot_sentiment_distribution

# Datasetin yeri
file_path = "data/raw_data/tweets.csv"
processed_data_path = "data/processed_data/sentiment_analysis_results.csv"

# Dataseti yükləyirik
df = load_data(file_path)

# Sentiment təhlilini tətbiq edirik
df = analyze_sentiment(df)

# processed_data qovluğunu yaradın, əgər yoxdursa
if not os.path.exists('data/processed_data'):
    os.makedirs('data/processed_data')

# Yalnız lazımlı sütunları seçirik (tweet_text, sentiment, sentiment_label)
df_to_save = df[['text', 'sentiment', 'sentiment_label']]

# DataFrame-i CSV faylında saxlayırıq
save_to_csv(df_to_save, processed_data_path)

# Məlumatları SQLite verilənlər bazasına yazırıq
save_to_sqlite(df)

# Qrafikləşdirməni işə salırıq
plot_sentiment_distribution(df)

# SQLite verilənlər bazasından məlumatları çəkmək (əgər lazım olsa)
# fetched_df = fetch_data_from_sqlite()
# print(fetched_df.head())
