# import requests
# import mysql.connector
# import pandas as pd

# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]

def sol(arr):
    original_len = len(arr)
    index = 0
    while index < len(arr):
        if arr[index] == 0:
            # shift to right
            arr[-1] = 0
            end_ptr = original_len - 1
            while end_ptr > index:
                arr[end_ptr], arr[end_ptr - 1] = arr[end_ptr - 1], arr[end_ptr]
                end_ptr -= 1
            # print(arr)
            index += 1
        index += 1
    return arr


print(sol([1, 0, 1, 0, 1, 7]))

# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock
# with one condition: You have to hold the stock for minimum 5 days.
# Return the maximum profit you can get from this transaction. If you cannot get any profit, return 0.

# Input: prices = [7,1,5,3,6,4,8,9,10,6,2]
# Output: 9
# Explanation: Buy on day 2 (price = 1), after holding it for 6 days sell it on day 9 (price = 10), profit = 10-1 = 9


def stocks_profit(stocks):
    if len(stocks) <= 6:
        return 0
    m_profit = 0
    cur_profit = 0
    for index in range(len(stocks)-6):
        profit_array = stocks[index+6:]
        max_profit = max(profit_array)
        if max_profit > stocks[index]:
            cur_profit = max_profit - stocks[index]
        if cur_profit > m_profit:
            m_profit = cur_profit
    return m_profit

# print(stocks_profit([7,1,5,3,6,89,1]))
# 3+9
