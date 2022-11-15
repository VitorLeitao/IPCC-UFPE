soma = 1
for c in range(2, 1001):
    fact1 = 1
    for i in range(1,c+1): 
        fact1 = fact1 * i 
    soma += fact1

print(soma % 9)
      



