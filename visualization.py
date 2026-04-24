import matplotlib
matplotlib.use('Agg')  # 'Agg' backend istifadə edirik ki, GUI problemi olmasın
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_distribution(df):
    """
    Bu funksiya sentiment paylanmasını qrafikləşdirmək üçün istifadə olunur.
    """
    # Sentimentlərin sayını əldə edirik
    sentiment_counts = df['sentiment_label'].value_counts()

    # Qrafikləşdirmək
    plt.figure(figsize=(8, 6))

    # Seaborn barplot-u ilə qrafiki çəkirik (hue ilə x əlaqələndirilir)
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, hue=sentiment_counts.index, palette='viridis', legend=False)

    # Qrafik üçün başlıq və etiketlər əlavə edirik
    plt.title('Sentiment Distribution of Tweets')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')

    # Qrafiki şəkil faylı olaraq saxlayırıq
    plt.savefig('sentiment_distribution.png')  # Şəkil faylında saxlayırıq
    plt.close()  # Şəkil saxlandıqdan sonra qrafiki bağlayırıq
