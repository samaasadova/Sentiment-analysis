import pandas as pd

def load_data(file_path):
    """
    Bu funksiya CSV faylını oxuyur və pandas DataFrame olaraq qaytarır.
    """
    df = pd.read_csv(file_path)
    return df

