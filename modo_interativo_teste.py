def eh_maior_de_idade():
    idade = int(input('Digite uma idade: '))
    try:
        if idade is not None:
            if idade >= 18:
                print('maior de idade')
            elif idade < 18:
                print('menor de idade')
    except:
        print('Digite apenas números')