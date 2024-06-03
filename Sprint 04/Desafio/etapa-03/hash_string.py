import hashlib
 
while True:

    entrada = input("Digite algo (para encerrar, digite 'sair'): \n")
    
    if entrada.lower() == "sair":
        break
    
    hash_entrada = hashlib.sha1(entrada.encode())
    
    hex_entrada = hash_entrada.hexdigest()
    
    print(f"Hash do texto digitado: {hex_entrada} \n")
