# def conta_maluca (n):
#     if n == 0:
#         return 0
#     else:
#         return n + conta_maluca(n - 1)

# resultado = conta_maluca(5)
# print(resultado)

def conta_maluca(n1, n2):
    resultado = (n1*3) + (n2+13)
    print(f"O resultado é: {resultado}")

conta_maluca(5, 10)
    