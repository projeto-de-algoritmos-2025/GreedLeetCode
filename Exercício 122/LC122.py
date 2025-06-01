class Solution:
  def maxProfit(self, prices: list[int]) -> int:
    if not prices or len(prices) < 2:
      return 0

    max_profit_total = 0

    for i in range(1, len(prices)):
      if prices[i] > prices[i-1]:  # intervalo de oportunidade de lucro"
        profit_this_interval = prices[i] - prices[i-1]
        max_profit_total += profit_this_interval

    return max_profit_total