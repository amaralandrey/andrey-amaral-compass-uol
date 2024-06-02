#!/bin/bash

cd /home/andrey/andrey-amaral-compass-uol-1/Sprint01/Desafio/Etapa-1/ecommerce

data_execucao=$(date +"%Y%m%d")

data_sistema=$(date +"%Y/%m/%d %H:%M")

mkdir vendas && mkdir vendas/backup 

cp dados_de_vendas.csv vendas/ 

cp vendas/dados_de_vendas.csv vendas/backup/dados_de_vendas-${data_execucao}.csv

cd vendas/backup && mv dados_de_vendas-${data_execucao}.csv backup-dados-${data_execucao}.csv

primeira_venda=$(awk -F',' 'NR==2 {print $5}' backup-dados-${data_execucao}.csv)

ultima_venda=$(awk -F',' 'NR==67 {print $5}' backup-dados-${data_execucao}.csv)

total_itens=$(awk -F',' 'NR>1 {print $2}' backup-dados-${data_execucao}.csv | sort | uniq | wc -l)

echo "Data do sistema operacional: ${data_sistema}" >> relatorio.txt
echo "Data do primeiro registro de venda: ${primeira_venda}" >> relatorio.txt
echo "Data do último registro de venda: ${ultima_venda}" >> relatorio.txt
echo "Quantidade total de itens diferentes vendidos: ${total_itens}" >> relatorio.txt
echo "10 primeiras linhas do arquivo de vendas:" >> relatorio.txt
tail -n +2 backup-dados-${data_execucao}.csv | head -n 10 >> relatorio.txt

zip backup-dados-${data_execucao}.zip backup-dados-${data_execucao}.csv

ls && rm *.csv

cd .. && rm *.csv
