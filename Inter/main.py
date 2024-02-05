import csv
import os

year = input(" Ano: ")
diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_script, '../Arquivos Relatorios/extrato' + year + 'Inter.csv')

with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
    file = csv.reader(csvfile, delimiter=';', quotechar='|', )
    category = [['Pix enviado ', 0, 0, [["", 0, 0]]], ['Pix recebido', 0, 0, [["", 0, 0]]], ['Crédito Evento B3', 0, 0, [["", 0, 0, 0]]], ['Pagamento efetuado', 0, 0, [ ["", 0] ]], ['Compra no débito', 0, 0, [ ["", 0] ]] ]
    for row in file:
      if category[0][0] == row[1]:
        category[0][1] += float(row[3].replace('.','').replace(',','.')[1:])
        category[0][2] += 1
        for i in range(0, len(category[0][3])):
          if category[0][3][i][0] == row[2]:
            category[0][3][i][1] += float(row[3].replace('.','').replace(',','.')[1:])
            category[0][3][i][2] += 1
            break
        else:
          category[0][3].append([row[2], float(row[3].replace('.','').replace(',','.')[1:]), 1])
      if category[1][0] == row[1]:
        category[1][1] += float(row[3].replace('.','').replace(',','.'))
        category[1][2] += 1
        for i in range(0, len(category[1][3])):
          if category[1][3][i][0] == row[2]:
            category[1][3][i][1] += float(row[3].replace('.','').replace(',','.'))
            category[1][3][i][2] += 1
            break
        else:
          category[1][3].append([row[2], float(row[3].replace('.','').replace(',','.')), 1])
      if category[2][0] == row[1]:
        category[2][1] += float(row[3].replace('.','').replace(',','.'))
        category[2][2] += 1
        item = row[2].split()
        for i in range(0, len(category[2][3])):
          if item[5] == category[2][3][i][0]:
            category[2][3][i][1] += float(row[3].replace('.','').replace(',','.'))
            category[2][3][i][2] += 1
            category[2][3][i][3] += int(item[4])
            break
        else:
          category[2][3].append([item[5], float(row[3].replace('.','').replace(',','.')), 1, int(item[4])])
      if category[3][0] == row[1]:
        category[3][1] += float(row[3].replace('.','').replace(',','.')[1:])
        category[3][2] += 1
        for i in range(0, len(category[3][3])):
          if category[3][3][i][0] == row[2]:
            category[3][3][i][1] += float(row[3].replace('.','').replace(',','.')[1:])
            break
        else:
          category[3][3].append([row[2], float(row[3].replace('.','').replace(',','.')[1:])])
      if category[4][0] == row[1]:
        category[4][1] += float(row[3].replace('.','').replace(',','.')[1:])
        category[4][2] += 1
        for i in range(0, len(category[4][3])):
          if category[4][3][i][0] == row[2]:
            category[4][3][i][1] += float(row[3].replace('.','').replace(',','.')[1:])
            break
        else:
          category[4][3].append([row[2], float(row[3].replace('.','').replace(',','.')[1:])])  
    print("\n")
    print("\tTransações totais: " + str(category[0][2]+ category[1][2] + category[2][2] + category[3][2] + category[4][2]).zfill(4))
    print(str(category[0][2]).zfill(4) + " - " + category[0][0][:-1] + ": R$" + f"{round(category[0][1], 2):.2f}")
    print(str(category[1][2]).zfill(4) + " - " + category[1][0] + ": R$" + f"{round(category[1][1], 2):.2f}")
    print(str(category[2][2]).zfill(4) + " - " + category[2][0] + ": R$" + f"{round(category[2][1], 2):.2f}")
    print(str(category[3][2]).zfill(4) + " - " + category[3][0] + ": R$" + f"{round(category[3][1], 2):.2f}")
    print(str(category[4][2]).zfill(4) + " - " + category[4][0] + ": R$" + f"{round(category[4][1], 2):.2f}")
    print("\n")
    print("\tTransações Pix recebidos")
    for i in range(0, len(category[1][3])):
      if i != 0: 
        print(str(category[1][3][i][2]).zfill(2) + " - " + category[1][3][i][0] + ": R$" + f"{category[1][3][i][1]:.2f}")
    print("\n")
    print("\tTransações Pix enviados")
    for i in range(0, len(category[0][3])):
      if i != 0: 
        print(str(category[0][3][i][2]).zfill(2) + " - " + category[0][3][i][0] + ": R$" + f"{category[0][3][i][1]:.2f}")
    print("\n")
    print("\tDividendos recebidos")
    for i in range(0, len(category[2][3])):
      if i != 0:
        print(str(category[2][3][i][2]).zfill(2) + " - " + category[2][3][i][0] + ": R$" + f"{category[2][3][i][1]:.2f}".zfill(6) + "  x" + str(category[2][3][i][3]).zfill(4) + "  -> R$" + f"{(category[2][3][i][1] / category[2][3][i][3]):.2f}")
    print("\n")