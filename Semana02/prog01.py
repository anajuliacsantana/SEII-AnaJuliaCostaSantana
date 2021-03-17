#Métodos são funcões que pertencem a um objeto
#Método - replace
#Trocando caracteres da string, precisamos de 2 argumentos
#a string que será alterada e o novo caracter, 
#e ela retorna uma nova mensagem, para trocar na própria mensagem
#basta ter a variável atua susbtituída
message = 'Hello World'
new_message = message.replace('World','Universe') 
print(new_message)