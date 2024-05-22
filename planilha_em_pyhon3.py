import openpyxl

#Carregando arquivo
book = openpyxl.load_workbook('Planilha de Compras.xlsx')

#selecionando uma página
frutas_page = book['Frutas']

#
for rows in frutas_page.iter_rows(min_row=2, max_row=5):
    print(f'{rows[0].value}, {rows[1].value}, {rows[2].value}') # ou assim: print(rows[0].value, rows[1].value, rows[2].value) --> menos organizado mas é outra forma que funciona
