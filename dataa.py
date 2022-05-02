# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# from random import random
# # Raw Package
# import numpy as np
# import pandas as pd
#
# #Data Source
# import yfinance as yf
#
# #Data viz
# import plotly.graph_objs as go
#
#
# # def print_hi(name):
# #     # Use a breakpoint in the code line below to debug your script.
# #     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# #     print("''''Nice''''")  # Press Ctrl+F8 to toggle the breakpoint.
# #
# #
# # def sortAB(ltArgs):
# #     for i in range(len(ltArgs)-1, 0, -1):
# #         for j in range(i):
# #             if ltArgs[j] > ltArgs[j+1]:
# #                 sw = ltArgs[j]
# #                 ltArgs[j] = ltArgs[j+1]
# #                 ltArgs[j+1] = sw
# #
# #     return ltArgs
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     # Interval required 5 minutes
#     # dataUBER = yf.download(tickers='UBER', period='5d', interval='5m')
#     # dataFB = yf.download(tickers='FB', period='5d', interval='5m')
#     # data_BTC_USD = yf.download(tickers='BTC-USD', period='22h', interval='15m')
#     data_ADA_USD = yf.download(tickers='ADA-USD', period='max', interval='1wk')
#
#     # Print data
#     # print(dataFB)
#     # print(dataUBER)
#     # print(data_BTC_USD)
#     print(data_ADA_USD)
