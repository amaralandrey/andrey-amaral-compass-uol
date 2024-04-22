
# Desafio

### Etapas
0. Preparação.
- Foi baixado o arquivo dados_de_vendas.csv e criado o diretório ecommerce. 
- O arquivo csv foi movido para dentro do diretório ecommerce. 

1. Criar arquivo executável. 
- O script usa o comando cd para indicar onde o processamento deve ocorrer, no caso, escolhi realizar as operações dentro do diretório ecommerce em todas as etapas.  
**cd /home/andrey/andrey-amaral-compass-uol-1/Sprint01/Desafio/Etapa-1/ecommerce**

- São usadas variáveis para guardar a data de execução do script e a data do sistema, que contém a hora e o minuto da execução.  
**data_execucao=$(date +"%Y%m%d")**
**data_sistema=$(date +"%Y/%m/%d %H:%M")**

- São criados os diretórios com o comando mkdir.  
**mkdir vendas && mkdir vendas/backup**
  
- As operações de movimentação e cópia de arquivos são realizadas posteriormente.  
**cp dados_de_vendas.csv vendas/**  
**cp vendas/dados_de_vendas.csv vendas/backup/dados_de_vendas-${data_execucao}.csv**  
**cd vendas/backup && mv dados_de_vendas-${data_execucao}.csv backup-dados-${data_execucao}.csv**  

- São realizadas operações nos dados do arquivo de backup, como a obtenção da primeira e última venda, assim como o cálculo do total de itens vendidos.  
**primeira_venda=$(awk -F',' 'NR==2 {print $5}' backup-dados-${data_execucao}.csv)**  
**ultima_venda=$(awk -F',' 'NR==67 {print $5}' backup-dados-${data_execucao}.csv)**  
**total_itens=$(awk -F',' 'NR>1 {print $2}' backup-dados-${data_execucao}.csv | sort | uniq | wc -l)**  

- O relatório é criado.
**echo "Data do sistema operacional: ${data_sistema}" >> relatorio.txt**  
**echo "Data do primeiro registro de venda: ${primeira_venda}" >> relatorio.txt**  
**echo "Data do último registro de venda: ${ultima_venda}" >> relatorio.txt**  
**echo "Quantidade total de itens diferentes vendidos: ${total_itens}" >> relatorio.txt**  
**echo "10 primeiras linhas do arquivo de vendas:" >> relatorio.txt**  
**tail -n +2 backup-dados-${data_execucao}.csv | head -n 10 >> relatorio.txt**  
  
- O arquivos .csv são compactados em um arquivo .zip e os arquivos .csv são removidos do diretório atual e do diretório anterior. Foi preciso usar o comando ls junto com o rm, pois sem ele o rm não encontrava os arquivos csv.
**zip backup-dados-${data_execucao}.zip backup-dados-${data_execucao}.csv**  
__ls && rm *.csv__  
__cd .. && rm *.csv__  

2. Agendar a execução do processamento.
- Para agendar a execução da tarefa, foi utilizado o Crontab. 
- A instrução de agendamento utilizada foi: "**27 15 * * 1-4 /bin/bash /home/andrey/andrey-amaral-compass-uol-1/Sprint01/Desafio/Etapa-3/ecommerce/processamento_de_vendas.sh**". 

![Print da instrução registrada no Crontab](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint01/Desafio/Etapa-2/desafio-etapa2.png)

3. Criar novo relatório. 
- Foram criadas três novas versões do arquivo dados_de_vendas.csv.
- Foi criado um script que cria no diretório vendas o relatorio_final.txt e adiciona a ele os dados dos relatórios txt que estiverem no diretório backup.
- Para que os relatórios não se sobrepusessem durante as execuções, o script foi alterado para incluir a data de execução no nome de cada relatório.
  __for relatorio in *.txt; do
    cat "$relatorio" >> "../$relatorio_final"
    echo "" >> "../$relatorio_final"
done__
