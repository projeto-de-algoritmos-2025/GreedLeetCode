class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
         # Ordena os intervalos pelo valor de fim
        intervals.sort(key=lambda x: x[1])
        
        removals = 0
        # Guarda o final do primeiro intervalo (após a ordenação)
        end = intervals[0][1]
        
        # Percorre os intervalos a partir do segundo
        for i in range(1, len(intervals)):
            #Testa se o início do intervalo atual é menor que o final do último intervalo.
            #Se for menor, ele é removido.
            if intervals[i][0] < end:
                removals += 1
            else:
                # Atualiza o final para o final do intervalo atual, pois não há sobreposição.
                end = intervals[i][1]
        
        return removals
      
