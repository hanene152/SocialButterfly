# reporting/report_generator.py

import matplotlib.pyplot as plt
import pandas as pd

def generate_report(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(f"{filename}.csv", index=False)

def plot_sentiment(data, title, filename):
    df = pd.DataFrame(data)
    plt.figure(figsize=(10, 5))
    plt.hist(df['sentiment'], bins=20, edgecolor='k')
    plt.title(title)
    plt.xlabel('Sentiment')
    plt.ylabel('Frequency')
    plt.savefig(f"{filename}.png")
