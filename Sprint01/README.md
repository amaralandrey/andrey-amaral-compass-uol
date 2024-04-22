
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
- A instrução de agendamento utilizada foi: "27 15 * * 1-4 /bin/bash /home/andrey/andrey-amaral-compass-uol-1/Sprint01/Desafio/Etapa-3/ecommerce/processamento_de_vendas.sh". 

![Print da instrução registrada no Crontab](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint01/Desafio/Etapa-2/desafio-etapa2.png)

3. Criar novo relatório. 
- Foram criadas três novas versões do arquivo dados_de_vendas.csv.
- Foi criado um script que cria no diretório vendas o relatorio_final.txt e adiciona a ele os dados dos relatórios txt que estiverem no diretório backup.
- Para que os relatórios não se sobrepusessem durante as execuções, o script foi alterado para incluir a data de execução no nome de cada relatório.

# Exercícios
## Nesta sprint não foram repassados exercícios para serem executados, além do desafio.

# Evidências
## Nesa seção, apresento as evidências produzidas durante a realização das atividades da sprint.

### Arquivos csv
Além dos dados de vendas fornecidos inicialmente, adicionei também ao diretório Evidências as três alterações completas que foram requeridas para a execução agendada do script de processamento de vendas. 

### Atividades com o Github
Nos foi requerida a realização de atividades utilizando o Github.

- Etapa 01 - Criar um repositório privado e adicionar colaboradores.

![Repositorio criado](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint01/Evidencias/etapa1.1.png)

![Colaboradores adicionados](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint01/Evidencias/etapa1.2.png)

- Etapa 02 - Escolher um editor de código e integrar ao Github.
O editor que escolhi foi o VSCode.

![Instalando plugging no editor](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint01/Evidencias/etapa2.1.png)

![Clonando o repositorio para o ambiente de integracao](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint01/Evidencias/etapa2.2.png)

- Etapa 03 - Criar um README e escrever apresentação e resumos.
O Markdown foi criado e está como o README do repositório que foi criado.

- Etapa 04 - Realizar commit e push.
Foram realizados durante a sprint.

# Certificados
## Nesta seção, apresento as últimas telas dos dois cursos que deveriam ser assistidos na sprint 01. Não foram realizados cursos externos.

![Tela do curso de linux](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint01/Certificados/conclusao-curso-linux.png)

![Tela do curso de Git/Github](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint01/Certificados/conclusao-curso-git.png)
