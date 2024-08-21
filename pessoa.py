from datetime import date

#CLASSE ENDERECO
class Endereco:
    def __init__(self, logradouro="", numero="", endereco_Comercial=False):
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_Comercial = endereco_Comercial
        
        
#CLASSE PESSOA
class Pessoa:
    def __init__(self, nome="", rendimento=0.0, endereco=None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco
        
    def calcular_imposto(self, rendimento):
        return rendimento
        
        
#CLASSE PESSOA FISICA
class PessoaFisica(Pessoa):
    #inicializar com os atributos que foram herdados e proprios atributos da classe
    def __init__(self, nome="", rendimento=0.0, endereco=None, cpf="", dataNascimento=""):
        
        if endereco is None:
            #Se nenhum endereco for fornecido, cria um objetivo chamado endereco padrao
            endereco = Endereco()
            
        if dataNascimento is None:
            dataNascimento = date.today()
        
        super().__init__(nome, rendimento, endereco)
        #chama o construtor da superclasse Pessoa para inicializar os atributos herdados
        
        
        #Atributos da propria classe
        self.cpf = cpf
        self.dataNascimento = dataNascimento
        
    def calcular_imposto(self, rendimento: float) -> float:
        # Sem imposto para rendimentos até 1500
        if rendimento <= 1500:
            return 0
        
        # 2% de imposto para rendimentos acima de 6000        
        elif 1500 < rendimento <= 3500:
            return (rendimento / 100)* 2
        
        # 3.5% de imposto para rendimentos acima de 6000        
        elif 3500 < rendimento <= 6000:
            return (rendimento / 100) * 3.5
        # 5% de imposto para rendimentos acima de 6000
        else:
            return (rendimento * 0.05)    
        
        
#CLASSE PESSOA JURIDICA
class PessoaJuridica(Pessoa):
    #inicializar com os atributos que foram herdados e proprios atributos da classe
    def __init__(self, nome="", rendimento=0.0, endereco=None, cnpj=""):
        
        if endereco is None:
            #Se nenhum endereco for fornecido, cria um objetivo chamado endereco padrao
            endereco = Endereco()
            
        
        super().__init__(nome, rendimento, endereco)
        #chama o construtor da superclasse Pessoa para inicializar os atributos herdados
        
        
        #Atributos da propria classe
        self.cnpj = cnpj
        
    def calcular_imposto(self, rendimento: float) -> float:
        # Sem imposto para rendimentos até 1500
        if rendimento <= 1500:
            return 0
        
        # 2% de imposto para rendimentos acima de 6000        
        elif 1500 < rendimento <= 3500:
            return (rendimento / 100)* 2
        
        # 3.5% de imposto para rendimentos acima de 6000        
        elif 3500 < rendimento <= 6000:
            return (rendimento / 100) * 3.5
        # 5% de imposto para rendimentos acima de 6000
        else:
            return (rendimento * 0.05)    