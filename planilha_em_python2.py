import openpyxl

#Carregando arquivo
book = openpyxl.load_workbook('Planilha de Compras.xlsx')

#selecionando uma página
frutas_page = book['Frutas']

#
for rows in frutas_page.iter_rows(min_row=2, max_row=5):
    for cell in rows:
        print(cell.value)
