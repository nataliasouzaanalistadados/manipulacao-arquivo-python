
# #Script para inserir novos dados no arquivo
# cpf = input('CPF: ')
# nome = input('Nome: ')
# idade = input('Idade: ')
# Sexo = input('Sexo: ')
# endereco = input('Endereço: ') 
# #del cadastro[indice] Para deletar a informação
# #break
# cadastro_novo = f'{cpf},{nome},{idade},{Sexo},{endereco}\n'


# with open('cadastro_novo.csv','a') as arquivo:
#     arquivo.writelines(cadastro_novo)

# arquivo.close()


# #Realizando uma consulta

# with open('cadastro_novo.csv','r') as arquivo:
#     cadastro_novo = arquivo.readlines()


# filtro_cpf = str(input('Insira o cpf de consulta: '))

# for registro in cadastro_novo:
#     if filtro_cpf in registro.split(',')[0]:
#         print('CPF: ', registro.split(',')[0])
#         print('Nome: ', registro.split(',')[1])
#         print('Idade: ', registro.split(',')[2])
#         print('Sexo: ', registro.split(',')[3])
#         print('Endereço: ', registro.split(',')[4])

# arquivo.close()


#Realizando uma exclusão


filtro_cpf = str(input('Insira o cpf para exclusão: '))
with open('cadastro_novo.csv','r') as arquivo:
    cadastro_novo = arquivo.readlines()


for indice in range(len(cadastro_novo)): 
    if filtro_cpf in cadastro_novo[indice].split(','):
        registro = cadastro_novo[indice].split(',')
        print('CPF: ', registro[0])
        print('Nome: ', registro[1])
        print('Idade: ', registro[2])
        print('Sexo: ', registro[3])
        print('Endereço: ', registro[4])

        if input('Deseja excluir o registro? S/N ').upper()=='S':
            cadastro_novo.pop(indice)  

            with open('cadastro_novo.csv','w') as arquivo:
                arquivo.write("".join(cadastro_novo))
            break
        else:
            print('Cancelado pelo usuário')
    


arquivo.close()

