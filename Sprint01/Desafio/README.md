
# Desafio

### Etapas
0. Preparação.
- Foi baixado o arquivo dados_de_vendas.csv e criado o diretório ecommerce. 
- O arquivo csv foi movido para dentro do diretório ecommerce. 

1. Criar arquivo executável. 
- O script usa o comando cd para indicar onde o processamento deve ocorrer, no caso, escolhi realizar as operações dentro do diretório ecommerce em todas as etapas.
- São usadas variáveis para guardar a data de execução do script e a data do sistema, que contém a hora e o minuto da execução.
- São criados os diretórios com o comando mkdir.
- As operações de movimentação e cópia de arquivos são realizadas posteriormente.
- São realizadas operações nos dados do arquivo de backup, como a obtenção da primeira e última venda, assim como o cálculo do total de itens vendidos. 
- O relatório é criado.
- O arquivos .csv são compactados em um arquivo .zip e os arquivos .csv são removidos do diretório atual e do diretório anterior

2. Agendar a execução do processamento.
- Para agendar a execução da tarefa, foi utilizado o Crontab. 
- A instrução de agendamento utilizada foi: "27 15 * * 1-4 /bin/bash /home/andrey/andrey-amaral-compass-uol-1/Sprint01/Desafio/Etapa-3/ecommerce/processamento_de_vendas.sh'. 

![Print da instrução registrada no Crontab](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint01/Desafio/Etapa-2/desafio-etapa2.png)

3. Criar novo relatório. 
- Foram criadas três novas versões do arquivo dados_de_vendas.csv.
- Foi criado um script que cria no diretório vendas o relatorio_final.txt e adiciona a ele os dados dos relatórios txt que estiverem no diretório backup.
- Para que os relatórios não se sobrepusessem durante as execuções, o script foi alterado para incluir a data de execução no nome de cada relatório.
