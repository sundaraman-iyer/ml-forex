import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt

def analyze_bbands(file_name, length=20, std=2, threshold=0.9):
    # Read CSV data
    df = pd.read_csv(file_name)

    # Calculate Bollinger Bands
    df.ta.bbands(close="Close", length=length, std=std, append=True)

    # Calculate Bollinger Band percentage distances
    df['distance_upper'] = (df['Close'] - df['BBU_20_2.0']) / df['BBU_20_2.0']
    df['distance_lower'] = (df['Close'] - df['BBL_20_2.0']) / df['BBL_20_2.0']

    upper_threshold = 0.95  # Sell signal when close is near upper band
    lower_threshold = -0.95  # Buy signal when close is near lower band

    # Calculate percentage distance from the upper band
    df['distance_upper'] = (df['Close'] - df['BBU_20_2.0']) / df['BBU_20_2.0']

    # Create a new column for signals
    df['BB_Signal'] = 0

    # Set sell signals based on upper band distance
    df.loc[df['distance_upper'] > upper_threshold, 'BB_Signal'] = 1

    # Set buy signals based on lower band distance
    df.loc[df['distance_lower'] < lower_threshold, 'BB_Signal'] = -1

    # Plot closing price, Bollinger Bands, and highlight sell signals
    plt.figure(figsize=(10, 6))
    plt.plot(df['Close'], label='Close Price', color='black')
    plt.plot(df['BBM_20_2.0'], label='SMA_20', linestyle='--', color='blue')
    plt.plot(df['BBU_20_2.0'], label='Upper Band', linestyle='--', color='red')
    plt.plot(df['BBL_20_2.0'], label='Lower Band', linestyle='--', color='green')
    
    # Title of grapgh
    plt.title('Buy/Sell Signals based on Bollinger\'s Band  Strategy')
    plt.xlabel('Date')
    
    plt.legend()
    plt.show()

    # Print potential buy and sell signals
    if 1 in df['BB_Signal'].values:
        # print("Potential Sell Signal Detected")
        return False
    else:
        # print("Potential Buy Signal Detected")
        return True

if __name__ == '__main__':
    analyze_bbands('output-copy.csv', length=20, std=2)














































































# #working condition of bollinger's brand

# import pandas as pd
# import pandas_ta as ta
# import matplotlib.pyplot as plt

# # Replace 'your_data.csv' with your actual file path
# df = pd.read_csv('output-copy.csv')

# # Display the first few rows of the DataFrame
# print(df.head())

# # Calculate Bollinger Bands
# df.ta.bbands(close="Close", length=20, std=2, append=True)

# # Plot the closing prices and Bollinger Bands
# plt.figure(figsize=(10, 6))
# plt.plot(df['Close'], label='Close Price', color='black')
# plt.plot(df['BBM_20_2.0'], label='SMA_20', linestyle='--', color='blue')  # Correct column name for pandas_ta is 'BBM_20_2.0'
# plt.plot(df['BBU_20_2.0'], label='Upper Band', linestyle='--', color='red')
# plt.plot(df['BBL_20_2.0'], label='Lower Band', linestyle='--', color='green')
# plt.legend()
# plt.show()
