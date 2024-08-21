# 1 - Pessoa Fisica / 2 - Pessoa Juridica / 3 - Sair 
# 1 - Cadastrar Pessoa Fisica / 2 - Listar pessoa física / 3 - Sair 
# 1 - Cadastrar Pessoa Juridica / 2 - Listar pessoa Juridica / 3 - Sair 

from datetime import date, datetime
from pessoa import Endereco, PessoaFisica, PessoaJuridica


def main():
    
    lista_pf = []
    lista_pj = []
    
    while True:
        
        opcao = int(input("Escolha uma opcao:\n[1] Pessoa física [2] Pessoa Jurídica [3] Sair\n"))
        
        if opcao == 1:
            while True:
                opcao_PF = int(input("Escolha uma opcao:\n[1] Cadastrar [2] Listar [3] Remover CPF [4] Atualizar cadastro [5] Voltar ao menu anterior\n"))
                #Cadastrar uma pessoa física
                if opcao_PF == 1:
                    novaPF = PessoaFisica()
                    nova_end_PF = Endereco()
                    
                    novaPF.nome= input("Digite o Nome da pessoa física:\n")
                    novaPF.cpf= input("Digite o CPF da pessoa física:\n")
                    novaPF.rendimento= float(input("Digite o rendimento mensal da pessoa física (DIGITE APENAS NUMEROS):\n"))
                    
                    data_nascimento = input("Digite a data de nascimento (dd/NN/aaaa):\n") # Solicita a data de nascimento
                    novaPF.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novaPF.dataNascimento).days // 365
                    
                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")
                        continue # Retorna ao inicio do loop
                    
                    # Cadastro de endereco
                    nova_end_PF.logradouro = input("Digite o logradouro:\n")
                    nova_end_PF.numero = input("Digite o numero:\n")
                    end_comercial = input("Este endereco é comercial? [S] [N]\n") # Solicitar se o endereco é comercial
                    nova_end_PF.endereco_Comercial = end_comercial.strip().upper() == 'S' # Define maiusculo
                    
                    
                    novaPF.endereco = nova_end_PF
                    
                    lista_pf.append(novaPF)
                    
                    print("Cadastro realizado com sucesso")


                # Listar pessoa física
                elif opcao_PF == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome:\n{cada_pf.nome}")
                            print(f"CPF:\n{cada_pf.cpf}")
                            print(f"Endereco\n{cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}")
                            print(f"Data Nascimento\n{cada_pf.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago\n{cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print(f"Digite 0 para sair")
                            input()
                            
                    else:
                        print('Lista vazia')
                        
                # Sair do menu
                elif opcao_PF == 3:
                    removerCPF = input("Digite o CPF que deseja ser removido\n")
                    pessoa_encontrada = False
                    
                    for cada_pf in lista_pf:
                        if cada_pf.cpf == removerCPF:
                            lista_pf.remove(cada_pf) 
                            pessoa_encontrada = True
                            print("Pessoa física removida!")
                        
                    if not pessoa_encontrada:
                        print("Nenhuma pessoa encontrada")
                           
                    
                elif opcao_PF == 4:
                    atualizarCadastrof = input("Digite qual valor voce deseja alterar\n[0] Nome\n[1] Renda mensal\n[2] Logradouro\n[3] Numero\n[4] Endereco comercial\n[5] Data nascimento\n")
                    
                    if atualizarCadastrof == '0':
                        for cada_pf in lista_pf: 
                            novoNome = input("Digite o novo Nome:\n")
                            novaPF.nome = novoNome
                                                      
                    if atualizarCadastrof == '1':
                        for cada_pf in lista_pf: 
                            novoRenda = input("Digite a novo Renda mensal:\n")
                            novaPF.rendimento = novoRenda
                            
                    if atualizarCadastrof == '2':
                        for cada_pf in lista_pf: 
                            novoLogradouro = input("Digite o novo Logradouro:\n")
                            nova_end_PF.logradouro = novoLogradouro
                            
                    if atualizarCadastrof == '3':
                        for cada_pf in lista_pf: 
                            novoNumero = input("Digite o novo Numero:\n")
                            nova_end_PF.numero = novoNumero
                            
                    if atualizarCadastrof == '4':
                        for cada_pf in lista_pf: 
                            novoEnderecoComercial = input("Digite o novo Endereco Comercial [S] [N]:\n")
                            nova_end_PF.endereco_Comercial = novoEnderecoComercial 
                            
                    if atualizarCadastrof == '5':
                        for cada_pf in lista_pf: 
                            dataNascimento = input("Digite a nova data nascimento (dd/NN/aaaa):\n")
                            novaPF.dataNascimento = dataNascimento 
                
                
                # Sair do menu
                elif opcao_PF == 5:
                    print("Voltando ao menu anterior")
                    break
                
                else:
                    print("Opcao inválida, por favor digite uma das opcoes indicadas:\n")
               
               
               
        elif opcao == 2:
            while True:
                opcao_PJ = int(input("Escolha uma opcao:\n[1] Cadastrar [2] Listar [3] Remover CNPJ [4] Atualizar cadastro [5] Voltar ao menu anterior\n"))
                #Cadastrar uma pessoa Juridica
                if opcao_PJ == 1:
                    novaPJ = PessoaJuridica()
                    nova_end_PJ = Endereco()
                    
                    novaPJ.nome= input("Digite o Nome fantasia da pessoa Jurídica:\n")
                    novaPJ.cnpj= input("Digite o CNPJ da pessoa Jurídica:\n")
                    novaPJ.rendimento= float(input("Digite o rendimento mensal da pessoa Jurídica (DIGITE APENAS NUMEROS):\n"))
                    
                    
                    # Cadastro de endereco
                    nova_end_PJ.logradouro = input("Digite o logradouro:\n")
                    nova_end_PJ.numero = input("Digite o numero:\n")
                    end_comercial = input("Este endereco é comercial? [S] [N]\n") # Solicitar se o endereco é comercial
                    nova_end_PJ.endereco_Comercial = end_comercial.strip().upper() == 'S' # Define maiusculo
                    
                    
                    novaPJ.endereco = nova_end_PJ
                    
                    lista_pj.append(novaPJ)
                    
                    print("Cadastro realizado com sucesso")


                # Listar pessoa juridica
                elif opcao_PJ == 2:
                    if lista_pj:
                        for cada_pj in lista_pj:
                            print(f"Nome fantasia:\n{cada_pj.nome}")
                            print(f"CNPJ:\n{cada_pj.cnpj}")
                            print(f"Endereco\n{cada_pj.endereco.logradouro}, {cada_pj.endereco.numero}")
                            print(f"Imposto a ser pago\n{cada_pj.calcular_imposto(cada_pj.rendimento)}")
                            print(f"Digite 0 para sair")
                            input()
                            
                    else:
                        print('Lista vazia')
                        
                # Sair do menu
                elif opcao_PJ == 3:
                    removerCNPJ = input("Digite o CNPJ que deseja ser removido\n")
                    pessoa_encontradaJ = False
                    
                    for cada_pj in lista_pj:
                        if cada_pj.cnpj == removerCNPJ:
                            lista_pj.remove(cada_pj) 
                            pessoa_encontradaJ = True
                            print("Pessoa jurídica removida!")
                        
                    if not pessoa_encontradaJ:
                        print("Nenhuma pessoa encontrada")
                
                elif opcao_PJ == 4:
                    atualizarCadastro = input("Digite qual valor voce deseja alterar\n[0] Nome fantasia\n[1] Renda mensal\n[2] Logradouro\n[3] Numero\n[4] Endereco comercial\n")
                    
                    if atualizarCadastro == '0':
                        for cada_pj in lista_pj: 
                            novoNome = input("Digite o novo Nome fantasia:\n")
                            novaPJ.nome = novoNome
                                            
                    if atualizarCadastro == '1':
                        for cada_pj in lista_pj: 
                            novoRenda = input("Digite a novo Renda mensal:\n")
                            novaPJ.rendimento = novoRenda
                            
                    if atualizarCadastro == '2':
                        for cada_pj in lista_pj: 
                            novoLogradouro = input("Digite o novo Logradouro:\n")
                            nova_end_PJ.logradouro = novoLogradouro
                            
                    if atualizarCadastro == '3':
                        for cada_pj in lista_pj: 
                            novoNumero = input("Digite o novo Numero:\n")
                            nova_end_PJ.numero = novoNumero
                            
                    if atualizarCadastro == '4':
                        for cada_pj in lista_pj: 
                            novoEnderecoComercial = input("Digite o novo Endereco Comercial [S] [N]:\n")
                            nova_end_PJ.endereco_Comercial = novoEnderecoComercial 
                
                
                elif opcao_PJ == 5:
                    print("Voltando ao menu anterior")
                    break
                
                else:
                    print("Opcao inválida, por favor digite uma das opcoes indicadas:\n")            
        
        
        elif opcao == 3:
            print('Obrigado por utilizar nosso sistema')
            break
        
        
        else:
            print('Opcao invalida, por favor digite uma das opcoes listadas!')
            
            
if __name__ == '__main__':
    main() # Chama a funcao main