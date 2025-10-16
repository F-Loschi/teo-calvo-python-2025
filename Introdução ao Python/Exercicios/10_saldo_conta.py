#%%
saldo_total = 0

saldo = input("Entre com o saldo \n")

while saldo != '':
    saldo_total += float(saldo)
    saldo = input("Entre com o saldo\n")

print(f"Saldo total: R${saldo_total}")
#%%
saldo_total = 0

saldo = input("Entre com o saldo \n")

while True:
    saldo = input("Entre com o saldo\n")
    if saldo == '':
        break
    saldo_total += float(saldo)

print(f"Saldo total: R${saldo_total}")
# %%
