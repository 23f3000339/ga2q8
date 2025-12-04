# Healthcare Analysis Script
# Student Email: 23f3000339@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt

def generate_report():
    # Data Setup
    data = {
        'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
        'Score': [3.53, 3.29, 5.74, 5.05]
    }
    df = pd.DataFrame(data)
    
    # Calculate Average
    avg_score = df['Score'].mean()
    print(f"Calculated Average: {avg_score}")
    
    # Generate Plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['Quarter'], df['Score'], marker='o')
    plt.title(f'Performance Trend (Avg: {avg_score})')
    plt.axhline(y=4.5, color='r', linestyle='--', label='Target')
    plt.savefig('trend_chart.png')

if __name__ == "__main__":
    generate_report()
