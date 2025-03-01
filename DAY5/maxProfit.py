# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

def maxProfit(price):
    maxProfit=0
    for i in range(1,len(price)-1):
        if(price[i+1]>price[i]):
            maxProfit+=price[i+1]-price[i]
    return maxProfit

price=[7,1,5,3,6,4]
res=maxProfit(price)
print(res)

