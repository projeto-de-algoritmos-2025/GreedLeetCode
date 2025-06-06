# 122. Best Time to Buy and Sell Stock II

O arquivo [LC122.py](./LC122.py) apresenta a resolução do exercício número 122 sobre greedy algorithms da plataforma LeetCode.

A resolução foi aceita pela plataforma, conforme a **Figura 1** abaixo:

<center>

![Resolução 122.py](../assets/122.png)

**Figura 1** - Resolução da questão 122.

</center>

## Explicação da solução

1. O algortimo inicializa o lucro_maximo_total como 0.

2. Itera pela matriz prices começando do segundo dia (1) até o último dia.

3. Para cada dia atual (i), compare seu preço prices[i] com o preço do dia anterior (i-1).

    3.1. O par de dias (dia i-1, dia i) forma um "intervalo de oportunidade".

4. Se prices[i] > prices[i-1]: 

    4.1. Há um lucro potencial neste intervalo: lucro_do_intervalo = prices[i] - prices[i-1].
    4.2. Agenda esta transação e adicione lucro_do_intervalo ao lucro_maximo_total.

**Saída:** Após iterar por todos os intervalos diários possíveis, retorna o lucro_maximo_total.