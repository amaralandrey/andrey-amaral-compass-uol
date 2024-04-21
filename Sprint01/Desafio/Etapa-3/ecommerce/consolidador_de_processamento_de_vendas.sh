#!/bin/bash

# Define o nome do arquivo final
relatorio_final="relatorio_final.txt"

cd /home/andrey/andrey-amaral-compass-uol-1/Sprint01/Desafio/Etapa-3/ecommerce/vendas/backup

# Percorre todos os arquivos de relatório e os une no arquivo final
for relatorio in *.txt; do
    cat "$relatorio" >> "../$relatorio_final"
    echo "" >> "../$relatorio_final"
done

