devo_levantar = False
esta_muito_frio = True
esta_muito_quente = True

if devo_levantar:
    print('Levantar e preparar o café!')
elif esta_muito_frio:
    print('Ficar quietinho na cama!')
elif esta_muito_quente:
    print('Aumentar o ventilador!') # Este bloco será ignorado porque a condição anterior foi verdadeira.
else:
    print('Dormir mais um tanto!')
