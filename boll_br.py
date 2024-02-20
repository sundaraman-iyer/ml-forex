import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt

# Replace 'your_data.csv' with your actual file path
df = pd.read_csv('output-copy.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Calculate Bollinger Bands
df.ta.bbands(close="Close", length=20, std=2, append=True)

# Plot the closing prices and Bollinger Bands
plt.figure(figsize=(10, 6))
plt.plot(df['Close'], label='Close Price', color='black')
plt.plot(df['BBM_20_2.0'], label='SMA_20', linestyle='--', color='blue')  # Correct column name for pandas_ta is 'BBM_20_2.0'
plt.plot(df['BBU_20_2.0'], label='Upper Band', linestyle='--', color='red')
plt.plot(df['BBL_20_2.0'], label='Lower Band', linestyle='--', color='green')
plt.legend()
plt.show()
