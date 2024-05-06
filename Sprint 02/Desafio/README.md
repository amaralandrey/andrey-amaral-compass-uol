# Desafio

## Etapa 01

### Breve explicação sobre a normalização feita.  

A primeira forma normal (1FN) determina que os atributos da relação devem estar em sua forma atômica, ou seja, não podem ser compostos ou multivalorados. A base de dados Concessionaria já atende a 1FN, pois não tem atributos multivalorados ou compostos.  

Já a segunda forma normal (2FN) pressupõe que uma relação está na 2FN se ela está na 1FN e contém apenas dados sobre uma e somente uma entidade. A base de dados Concessionaria contém dados de mais de uma entidade, o que gera dependencias parciais (por exemplo, nome do cliente depender também do ID do cliente, não apenas do ID da locação) que devem ser eliminadas com a criação de relações separadas para cada entidade. Por isso, foram criadas as relações Cliente, Vendedor, Locação, Carro e Combustível.  
A relação tb_locacao recebe como chave estrangeira as chaves primárias de tb_cliente, tb_vendedor e tb_carro. A relação tb_carro recebe como chave estrangeira a chave primária de tb_combustível.  

Cardinalidade:  
- tb_cliente (1, N)  
- tb_vendedor (1, N)  
- tb_locacao (N, N)  
- tb_carro (1, N)  
- tb_combustivel (1, N)  

Por fim, a terceira forma normal (3FN) determina que a relação esteja na 2FN e que as dependências transitivas sejam eliminadas. Uma dependência transitiva ocorre quando um atributo em uma relação é determinado por outro atributo que não é uma chave primária. Nas relações criadas, todas as entidades dependem unicamente de suas respectivas chaves primárias, logo o esquema, após a transformação da 2FN, também está na 3FN.  

DER da base de dados concessionária após a normalização  
![Texto Alternativo](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2002/Desafio/etapa-1/der-concessionaria-normalizada.jpg)

As queries para a criação da base normalizada está na pasta etapa-1 em TXT e SQLITE.  

## Etapa 02

### Breve explicação do modelo dimensional criado.  

O modelo dimensional criado usa as relações cliente, vendedor, carro e combustível como as dimensões do modelo e a relação locação como o fato.  

O modelo utilizado foi o snowflake, pois em razão da dimensão carro receber uma chave estrangeira da dimensão combustível não consegui usar o modelo estrela.  

Desenho do modelo dimensiional   
![Texto Alternativo](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2002/Desafio/etapa-2/modelo-dimensional-concessionaria.jpg)

As queries para a criação da base dimensional está na pasta etapa-2 em TXT e SQLITE.  


