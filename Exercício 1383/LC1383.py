class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10**9 + 7
        
        # Cria uma lista engineers que une as listas (eficiência, velocidade)
        engineers = list(zip(efficiency, speed))
        # Ordena em ordem decrescente de eficiência
        engineers.sort(reverse=True, key=lambda x: x[0])
        
        speed_heap = []  # min-heap para guardar as velocidades selecionadas
        speed_sum = 0
        max_perf = 0
        
        # Percorre a lista de engenheiros: o atual define a eficiência mínima do time
        for curr_eff, curr_speed in engineers:
            # Adiciona a velocidade do engenheiro atual ao heap
            heapq.heappush(speed_heap, curr_speed)
            speed_sum += curr_speed
            
            # Se o time exceder o limite de k engenheiros, remove o de menor velocidade
            if len(speed_heap) > k:
                removed_speed = heapq.heappop(speed_heap)
                speed_sum -= removed_speed
            
            # Calcula o desempenho com o somatório atualizado de velocidades e a eficiência mínima atual
            curr_perf = speed_sum * curr_eff
            max_perf = max(max_perf, curr_perf)
        
        return max_perf % mod
        
