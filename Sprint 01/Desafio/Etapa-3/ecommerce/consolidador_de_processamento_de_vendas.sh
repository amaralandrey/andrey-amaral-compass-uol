#!/bin/bash

relatorio_final="relatorio_final.txt"

cd /home/andrey/andrey-amaral-compass-uol-1/Sprint01/Desafio/Etapa-3/ecommerce/vendas/backup

for relatorio in *.txt; do
    cat "$relatorio" >> "../$relatorio_final"
    echo "" >> "../$relatorio_final"
done
