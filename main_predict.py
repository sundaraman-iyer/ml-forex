
from cci import analyze_cci
import matplotlib.pyplot as plt
from boll_br import analyze_bbands
from sma import analyze_sma_signals
from termcolor import colored


def predict(file_name):

    # calling cci.py
    cci = analyze_cci(file_name)
    if cci:
        print("CCI Analyzed - Signal is Buy")
    else:
        print("CCI Analyzed - Signal is Sell")
    
    # calling boll_br.py
    bbands = analyze_bbands(file_name)
    if bbands:
        print("Bollenger's Brand Analyzed - Signal is Sell")
    else:
        print("Bollenger's Brand Analyzed - Signal is Buy")
    
    #calling sma.py
    sma = analyze_sma_signals(file_name)
    if sma:
        print("SMA Analyzed - Signal is Buy")
    else:
        print("SMA Analyzed - Signal is Sell")

    # final verdict

    if cci and bbands and sma:
        print(colored("Buy the Currency","green"))

    else:
        print(colored("Sell the Currency","yellow"))

if __name__ == '__main__':
    file_name = 'output-copy.csv'
    predict(file_name)