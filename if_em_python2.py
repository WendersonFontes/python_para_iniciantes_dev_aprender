devo_levantar = False
esta_muito_frio = True
esta_muito_quente = True

if devo_levantar:
    print('Levantar e preparar o café!')
if esta_muito_frio:  # Mudamos de elif para if
    print('Ficar quietinho na cama!')
if esta_muito_quente:  # Mudamos de elif para if
    print('Aumentar o ventilador!')
if not devo_levantar and not esta_muito_frio and not esta_muito_quente:
    print('Dormir mais um tanto!')