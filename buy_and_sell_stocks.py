# program to return maximum profit (Buy and sell stocks),given a list of prices on weekdays.......

def max_profit(prices):
    profit = 0
    min_profit = float('inf')
    for i in range(0,len(prices)):
        min_profit = min(min_profit, prices[i])
        max_profit = max(max_profit,prices[i]-min_profit)
        

    return max_profit