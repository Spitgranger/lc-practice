# This is a O(n) solution the idea would be the following:
# As we know we cannot sell before we buy, the buy pointer can
# be initialized to the first element of the prices array. Now,
# we iterate through the prices array and constantly calculate potential profit
# and updating the return variable. If at any point the price is lower than the buy price,
# we update our buy pointer to the current price.
def max_profit(prices):
    profit = 0
    buy = 0
    for i in range(len(prices)):
        profit = max(profit, prices[i] - prices[buy])
        if prices[i] < prices[buy]:
            buy = i
    return profit

print(max_profit([7,1,5,3,6,4]))
print(max_profit([7,6,4,3,1]))