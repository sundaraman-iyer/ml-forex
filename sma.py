import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def analyze_sma_signals(file_name, close_column='Close', sma_periods=[20, 50]):

  # Read data from CSV
  df = pd.read_csv(file_name)

  # Function to calculate SMA
  def calculate_sma(data, column, period):
    return data[column].rolling(window=period).mean()

  # Calculate SMAs
  df['SMA1'] = calculate_sma(df, close_column, sma_periods[0])
  df['SMA2'] = calculate_sma(df, close_column, sma_periods[1])

  # Determine Buy/Sell signals
  df['Signal'] = 0
  df.loc[df['SMA1'] > df['SMA2'], 'Signal'] = 1  # Golden Cross (Buy)
  df.loc[df['SMA1'] < df['SMA2'], 'Signal'] = -1  # Death Cross (Sell)

  # Plotting
  plt.figure(figsize=(10, 6))

  # Line plot for Closing Price and SMAs
  plt.plot(df['Date'], df[close_column], label='Closing Price', color='blue')
  plt.plot(df['Date'], df['SMA1'], label=f'SMA-{sma_periods[0]}', color='orange')
  plt.plot(df['Date'], df['SMA2'], label=f'SMA-{sma_periods[1]}', color='green')

  # Scatter plot for Buy/Sell signals
  buy_signals = df[df['Signal'] == 1]['Date'].tolist()
  sell_signals = df[df['Signal'] == -1]['Date'].tolist()
  plt.scatter(buy_signals, df.loc[df['Signal'] == 1, close_column], label='Buy Signal', marker='^', color='green')
  plt.scatter(sell_signals, df.loc[df['Signal'] == -1, close_column], label='Sell Signal', marker='v', color='red')

  # Title and labels
  plt.title('Buy/Sell Signals based on SMA Strategy')
  plt.xlabel('Date')
  plt.ylabel(f'{close_column}')

  # Set the y-axis tick labels to display in dollar format (assuming 'Close*' refers to price)
  if close_column[-1] == "*":
    plt.gca().yaxis.set_major_formatter('${x:,.0f}')

  # Legend
  plt.legend()

  # Show the plot
  plt.show()

  # final logic for prediction     

  if 1 in df['Signal'].values:
    # print("Potential Buy Signal Detected")
    return True
  else:
    # print("Potential Sell Signal Detected")
    return False


if __name__ == '__main__':
    analyze_sma_signals('output-copy.csv') 











































































# # working condition of sma.py

# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker

# # Read data from CSV file
# df = pd.read_csv('output_data.csv')  # Replace 'your_file_path.csv' with the actual path to your CSV file

# # Function to calculate Simple Moving Average (SMA)
# def calculate_sma(data, column, period):
#     return data[column].rolling(window=period).mean()

# # Calculate SMAs for the specified periods
# sma_period_1 = 20
# sma_period_2 = 50

# # Calculate SMAs and add them to the DataFrame
# df['SMA1'] = calculate_sma(df, 'Close*', sma_period_1)
# df['SMA2'] = calculate_sma(df, 'Close*', sma_period_2)

# # Determine Buy/Sell signals based on Golden Cross and Death Cross
# df['Signal'] = 0  # 0 represents no signal

# # Golden Cross (Buy Signal)
# df.loc[df['SMA1'] > df['SMA2'], 'Signal'] = 1

# # Death Cross (Sell Signal)
# df.loc[df['SMA1'] < df['SMA2'], 'Signal'] = -1

# # Plotting
# plt.figure(figsize=(10, 6))

# # Line plot for Closing Price and SMAs
# plt.plot(df['Date'], df['Close*'], label='Closing Price', color='blue')
# plt.plot(df['Date'], df['SMA1'], label=f'SMA-{sma_period_1}', color='orange')
# plt.plot(df['Date'], df['SMA2'], label=f'SMA-{sma_period_2}', color='green')

# # Scatter plot for Buy/Sell signals
# buy_signals = df[df['Signal'] == 1]['Date'].tolist()
# sell_signals = df[df['Signal'] == -1]['Date'].tolist()
# plt.scatter(buy_signals, df.loc[df['Signal'] == 1, 'Close*'], label='Buy Signal', marker='^', color='green')
# plt.scatter(sell_signals, df.loc[df['Signal'] == -1, 'Close*'], label='Sell Signal', marker='v', color='red')

# # Title and labels
# plt.title('Buy/Sell Signals based on SMA Strategy')
# plt.xlabel('Date')
# plt.ylabel('Closing Price (in $)')

# # Set the y-axis tick labels to display in dollar format
# plt.gca().yaxis.set_major_formatter('${x:,.0f}')

# # Legend
# plt.legend()

# # Show the plot
# plt.show()
