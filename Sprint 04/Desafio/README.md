## Desafio

Nesta sprint, o desafio proposto teve como objetivo a prática de containers utilizando Docker e Python. Ele era formado por três etapas. 

### Etapa 01

Na etapa 01, era preciso construir uma imagem para a execução de um script em Python.  
A imagem que escrevi segue as instruções a seguir:  

    FROM python:3.10  
    
    WORKDIR /app  
    
    COPY carguru.py /app/  
    
    CMD ["python", "carguru.py"]  

Para construir a imagem, utilizei o comando:

    docker build .

Como não dei nome ao Dockerfile, o nome da minha imagem ficou como "__sha256:17efab932f3c0d97988c4146264893dd26a4f445c4eb4__".  

Para executar a imagem, utilizei o comando: 

    docker run sha256:17efab932f3c0d97988c4146264893dd26a4f445c4eb4

A execução da imagem foi realizada com êxito.   

### Etapa 02

A etapa 02 consistia em responder à pergunta "é possível reutilizar containers?" e apresentar o comando para reiniciar um container parado.

Sim, é possível reutilizar um container, ou seja, utilizar um ambiente já instanciado para uma nova finalidade, embora cada execução do Docker gere um container diferente forma automatica. A reutilização pode ser um instrumento para economizar recursos do sistema e garantir a consistência do mesmo ambiente para situações diferentes.  
Para reiniciar um container utilizamos o comando __start__ ou o __restart__. O comando start é utilizado para iniciar containers que temos certeza que estão parados, do contrário não geram resultado. Já o comando restart pode ser utilizado em qualquer situação do container.  

### Etapa 03

Por último, a etapa 03 nos pedia para:

- Criar um script em Python.

        import hashlib
        
        while True:
        
            entrada = input("Digite algo (para encerrar, digite 'sair'): \n")
            if entrada.lower() == "sair":
                break
            
            hash_entrada = hashlib.sha1(entrada.encode())
            
            hex_entrada = hash_entrada.hexdigest()
            
            print(f"Hash do texto digitado: {hex_entrada} \n")
   
            
- Criar a imagem mascarar-dados para executar o script.

A imagem criada foi a seguinte:  

        FROM python:3.10
        
        WORKDIR /app
        
        COPY hash_string.py /app/ 
        
        CMD ["python", "hash_string.py"]

A construção dela foi feita com o comando:  

    docker build -t mascarar-imagens .
    
  
- Iniciar o container a partir da imagem e inserir algumas palavras no programa.  

A execução da imagem foi feita com o comando: 

    docker run -it mascarar-dados

    Palavra: Andrey  
    Hash: 9dc3bfc2ddc8e4f4ff5afbbf6f8b138671b13e9d  
    
    Palavra: Amaral  
    Hash: f9fa0a3cef3b4cb48eb6ddc3af97aebc4d88fcbc  
    
    Palavra: Miranda  
    Hash: b5e016461e6854e4e71c5dcbaf0bf906803336cb  
    
    Palavra: Belém do Pará  
    Hash: 51968612527711568a8addeba208909969cea872  
    
    Palavra: Compass/UOL  
    Hash: 5c6dfc08124196816cee4c63312d62c39e0286ba  
    


