import csv
import os

#year = input(" Ano: ")
diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_script, '../Arquivos Relatorios/extrato2023' + 'B3.csv')

fiis = [[["", 0, 0, 0, 0]]]

with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
  file = csv.reader(csvfile, delimiter=',', quotechar='"', )
  for row in file:
    if row[0] == "Credito":
      if row[2] == "Transferência - Liquidação":
        token = row[3].split()[0]
        for i in range(len(fiis[0])):
          if fiis[0][i][0] == token:
            fiis[0][i][1] += int(row[5])
            fiis[0][i][2] += float(row[7][4:-1].replace('.','').replace(',','.'))
            fiis[0][i][3] += 1
            break
        else:
          fiis[0].append([token, int(row[5]), float(row[7].replace('.','').replace(',','.')[4:-1]), 1, 0])

with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
  file = csv.reader(csvfile, delimiter=',', quotechar='"', ) 
  for row in file:
    if row[0] == "Debito":
      if row[2] == "Transferência - Liquidação":
        token = row[3].split()[0]
        for i in range(len(fiis[0])):
          if fiis[0][i][0] == token:
            fiis[0][i][1] -= int(row[5])
            fiis[0][i][2] -= float(row[7][4:-1].replace('.','').replace(',','.'))
            fiis[0][i][4] += 1
            break
print("\nATIVOS   QUANTIDADE   PREÇO MÉDIO   TOTAL       ENTRADAS   SAIDAS")
for i in range(len(fiis[0])):
  if i != 0:
    if fiis[0][i][1] != 0:
      print(fiis[0][i][0] + "   " + str(fiis[0][i][1]).zfill(3) + "          " + "R$" + f"{(fiis[0][i][2] / fiis[0][i][1]):.2f}".zfill(6) + "      " + "R$" + f"{fiis[0][i][2]:.2f}".zfill(7) + "   " + str(fiis[0][i][3]).zfill(2) + "         " + str(fiis[0][i][4]).zfill(2))
print("\nAtivos vendido")
acc = 0.0
for i in range(len(fiis[0])):
  if i != 0:
    if fiis[0][i][1] == 0:
      if (fiis[0][i][2] * -1) >= 0:
        print(fiis[0][i][0] + "   LUCRO     " + "R$" + f"{(fiis[0][i][2] * -1):.2f}".zfill(6))
        acc -= fiis[0][i][2]
      else:
        print(fiis[0][i][0] + "   PREJUIZO  " + "R$" + f"{fiis[0][i][2]:.2f}".zfill(6))
        acc += fiis[0][i][2]
print("   PREJUIZO DE VENDAS " + "R$" + f"{acc:.2f}")
