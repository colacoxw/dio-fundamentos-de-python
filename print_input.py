nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

# sep vai set utilido para separar os itens dentro do print, removendo o " " e deixando oque você inserir
# end é o final da linha, ou seja, se em end você tiver um ..., no final do print terá um ... 

print(nome,idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="#")
print(nome, idade, sep="#", end="...\n")