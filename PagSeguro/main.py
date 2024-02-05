import csv
import os

year = input(" Ano: ")
diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_script, '../Arquivos Relatorios/extrato' + year + 'PagSeguro.csv')

with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
    file = csv.reader(csvfile, delimiter=';', quotechar='|', )
    category = [['Vendas', 0, 0], ['Pix enviado', 0, 0, [ ["", 0, 0, 0] ]], ['Cartão da Conta', 0, 0], ['Pagamento de conta', 0, 0], ['QR Code Pix enviado', 0, 0], ['Rendimento da conta', 0, 0], ['Recarga de celular', 0, 0], ['Estorno Pix enviado', 0, 0, [ ['', 0, 0] ]]]
    for row in file:
      if row[2] == category[0][0]:
        category[0][1] += float(row[4].replace(',', '.'))
        category[0][2] += 1
      elif row[2] == category[1][0]:
        category[1][1] += float(row[4].replace(',', '.')[1:])
        category[1][2] += 1
        for i in range(len(category[1][3])):
          if category[1][3][i][0] == row[3]:
            category[1][3][i][1] += float(row[4].replace(',', '.')[1:])
            category[1][3][i][2] += 1
            break
        else:
          category[1][3].append([row[3], float(row[4].replace(',', '.')[1:]), 1])
      elif row[2] == category[2][0]:
        category[2][1] += float(row[4].replace(',', '.')[1:])
        category[2][2] += 1
      elif row[2] == category[3][0]:
        category[3][1] += float(row[4].replace(',', '.')[1:])
        category[3][2] += 1
      elif row[2] == category[4][0]:
        category[4][1] += float(row[4].replace(',', '.')[1:])
        category[4][2] += 1
      elif row[2] == category[5][0]:
        category[5][1] += float(row[4].replace(',', '.'))
        category[5][2] += 1
      elif row[2] == category[6][0]:
        category[6][1] += float(row[4].replace(',', '.')[1:])
        category[6][2] += 1
      elif row[2] == category[7][0]:
        category[7][1] += float(row[4].replace(',', '.'))
        category[7][2] += 1
        for i in range(len(category[1][3])):
          if category[1][3][i][0] == row[3]:
            category[1][3][i][1] -= float(row[4].replace(',', '.'))
        for i in range(len(category[7][3])):
          if category[7][3][i][0] == row[3]:
            category[7][3][i][1] += float(row[4].replace(',', '.'))
            category[7][3][i][2] += 1
            break
        else:
          category[7][3].append([row[3], float(row[4].replace(',', '.')), 1])
    print("\n")
    print("\tTransações totais: " + str(category[0][2]+ category[1][2] + category[2][2] + category[3][2] + category[4][2] + category[5][2] + category[6][2]).zfill(4))
    print(str(category[0][2]).zfill(4) + " - " + category[0][0] + ": R$" + str(round(category[0][1], 2)))
    print(str(category[1][2]).zfill(4) + " - " + category[1][0] + ": R$" + str(round(category[1][1], 2)))
    print(str(category[2][2]).zfill(4) + " - " + category[2][0] + ": R$" + str(round(category[2][1], 2)))
    print(str(category[3][2]).zfill(4) + " - " + category[3][0] + ": R$" + str(round(category[3][1], 2)))
    print(str(category[4][2]).zfill(4) + " - " + category[4][0] + ": R$" + str(round(category[4][1], 2)))
    print(str(category[5][2]).zfill(4) + " - " + category[5][0] + ": R$" + str(round(category[5][1], 2)))
    print(str(category[6][2]).zfill(4) + " - " + category[6][0] + ": R$" + str(round(category[6][1], 2)))
    print(str(category[7][2]).zfill(4) + " - " + category[7][0] + ": R$" + str(round(category[7][1], 2)))
    print("\n")
    print("\tPix Enviados totais em R$: ")
    for i in range(len(category[1][3])):
      if i != 0:
        print(str(category[1][3][i][2]).zfill(2) + " - " + category[1][3][i][0] + ": " + str(round(category[1][3][i][1], 2)))
    print("\n")
    print("\tEstornos de Pix Enviados totais em R$: ")
    for i in range(len(category[7][3])):
      if i != 0:
        print(str(category[7][3][i][2]).zfill(2) + " - " + category[7][3][i][0] + ": " + str(round(category[7][3][i][1], 2)))
    print("\n")
    
