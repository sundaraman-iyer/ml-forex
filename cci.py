import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt

def analyze_cci(filepath, length=20, threshold=100):

  # Read CSV data
  df = pd.read_csv(filepath, parse_dates=['Date'], dayfirst=True)

  # Calculate CCI
  df['CCI'] = df.ta.cci(close="Close", length=length, append=True)

  # Plot CCI and close price
  plt.figure(figsize=(10, 6))
  plt.plot(df['Date'], df['Close'], label='Close Price', color='black')
  plt.plot(df['Date'], df['CCI'], label='CCI', color='blue')
  plt.axhline(threshold, color='red', linestyle='--', linewidth=0.8, label='CCI +{}'.format(threshold))
  plt.axhline(-threshold, color='green', linestyle='--', linewidth=0.8, label='CCI -{}'.format(threshold))
  
  # Title of grapgh
  plt.title('Buy/Sell Signals based on CCI Strategy')
  plt.xlabel('Date')
  
  
  plt.legend()
  plt.show()

  # Calculate and print buy/sell signals
  df['CCI_Signal'] = 0
  df.loc[df['CCI'] > threshold, 'CCI_Signal'] = 1
  df.loc[df['CCI'] < -threshold, 'CCI_Signal'] = -1

  if 1 in df['CCI_Signal'].values:
    # print("Potential Sell Signal Detected")
    return False
  else:
    # print("Potential Buy Signal Detected")
    return True

if __name__ == '__main__':
  analyze_cci('output-copy.csv')



























# working condition of cci.py

# import pandas as pd
# import pandas_ta as ta
# import matplotlib.pyplot as plt

# # Replace 'output-copy.csv' with your actual file path
# df = pd.read_csv('output-copy.csv', parse_dates=['Date'], dayfirst=True)

# # Calculate Commodity Channel Index (CCI)
# df['CCI'] = df.ta.cci(close="Close", length=20, append=True)

# # Plot the closing prices and CCI
# plt.figure(figsize=(10, 6))
# plt.plot(df['Date'], df['Close'], label='Close Price', color='black')
# plt.plot(df['Date'], df['CCI'], label='CCI', color='blue')

# # Add a horizontal line at +100 and -100 for reference
# plt.axhline(100, color='red', linestyle='--', linewidth=0.8, label='CCI +100')
# plt.axhline(-100, color='green', linestyle='--', linewidth=0.8, label='CCI -100')

# plt.legend()
# plt.show()

# # Check if CCI is greater than +100 or less than -100
# cci_threshold = 100
# df['CCI_Signal'] = 0  # Initialize a new column for signals

# # Set signals based on CCI threshold
# df.loc[df['CCI'] > cci_threshold, 'CCI_Signal'] = 1  # Sell Signal
# df.loc[df['CCI'] < -cci_threshold, 'CCI_Signal'] = -1  # Buy Signal

# # Print the signals
# if 1 in df['CCI_Signal'].values:
#     print("Potential Sell Signal Detected")
# else:
#     print("Potential Buy Signal Detected")

# # Display the DataFrame with CCI signals
# print(df[['Date', 'CCI', 'CCI_Signal']])
