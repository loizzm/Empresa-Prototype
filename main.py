from Dev import Dev
from Data import Data
from PontoFlex import PontoFlex
from Eng import Eng
from Estagiario import Estagiario
from Gerente import Gerente
from Empresa import Empresa

data= Data(17,7,2001,8,0,0)
data4= Data(17,7,2001,17,0,0)
data2= Data(17,7,2001,12,0,0)
data3= Data(17,7,2001,13,0,0)
lucas=Dev("lucas","154.449.996-50",data,"553198363-7417","Rua itapura 207, Saudade")
lucas.Registra_ponto(data)
lucas.Registra_ponto(data2)
lucas.Registra_ponto(data3)
lucas.Registra_ponto(data4)
amanda= Eng("amanda","154.568.696-32",data,"553198363-7417","Rua Dante 60, São Lucas")
luiz=Estagiario("Luiz","154.568.696-32",data,"553198363-7417","Rua Dante 60, São Lucas")
amanda.Registra_ponto(data)
amanda.Registra_ponto(data4)
angelica= Gerente("angelica","154.568.696-32",data,"553198363-7417","Rua Dante 60, São Lucas")
angelica.add_Funcionario(amanda)
angelica.add_Funcionario(lucas)
print(amanda.calc_salario())
print(lucas.calc_salario())
angelica.calc_Salario()
angelica.calc_Salario()
print(angelica.salario)
Empresa=Empresa.instance()
Empresa1=Empresa.instance()
Empresa.cadastra_Funcionario(angelica)
Empresa.cadastra_Funcionario(amanda)
print(Empresa)










