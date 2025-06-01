import math

class Solution:
  def putMarbles(self, weights: list[int], k: int) -> int:
    n = len(weights)

    if k == 1 or k == n:
      return 0
    
    cut_costs = []
    for i in range(n - 1):
      cut_costs.append(weights[i] + weights[i+1])
    
    cut_costs.sort()
    
    min_score_additional_cost = 0
    num_cuts_to_make = k - 1
    
    for i in range(num_cuts_to_make):
      min_score_additional_cost += cut_costs[i]
      
    max_score_additional_cost = 0
    for i in range(num_cuts_to_make):
      max_score_additional_cost += cut_costs[len(cut_costs) - 1 - i]
    
    return max_score_additional_cost - min_score_additional_cost