# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = somaC = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor da matriz [{l},{c}]: '))
        
for l in range(0,3):
    somaC += matriz[l][2]
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c]%2 == 0:
            soma += matriz[l][c]
    print()

print(f'A soma de todos os valores pares é: {soma}')
print(f'A soma dos valores da terceira coluna é: {somaC}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')