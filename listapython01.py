"""
1) Leia a idade de uma pessoa. Se ela for maior ou igual a 18 anos, mostre a mensagem: "Maior de idade"

idade = int(input("Informe a idade: "))
if(idade >= 18):
    print("Maior de idade")
"""
"""
2 ) Leia um número. Se ele for positivo, mostre: "Numero positivo".

numero = int(input("Informe um numero: "))
if(numero > 0):
    print("Numero positivo")
"""
"""
3) Leia a nota de um aluno. Se a nota for maior ou igual a 7, mostre: "Aprovado direto".

nota = float(input("Informe a nota do aluno: "))
if(nota >= 7):
    print("Aprovado direto")
"""
"""
4) Leia um valor. Se ele for igual a zero, mostre: "Valor nulo".

valor = int(input("Informe um valor: "))
if(valor == 0):
    print("Valor nulo")
"""

"""
5) Leia o saldo de uma conta. Se o saldo for maior que 1000, mostre: "Cliente VIP".

saldo = float(input("Informe o saldo da conta: "))
if(saldo > 1000):
    print("Cliente VIP")
"""

"""
6) Leia a idade de uma pessoa. Se for maior ou igual a 18, mostre "Maior de idade", senão mostre "Menor de idade".

idade = int(input("Informe a idade: "))
if(idade >= 18):
    print("Maior de idade")
else:
    print("Menor de idade")
"""

"""
7) Leia um número. Se for positivo, mostre "Positivo", senão mostre "Negativo".

numero = int(input("Informe um numero: "))
if(numero > 0):
    print("Positivo")
else:
    print("Negativo")
"""

"""
8) Leia a nota de um aluno. Se for maior ou igual a 6, mostre "Aprovado", senão "Reprovado".

nota = float(input("Informe a nota do aluno: "))
if(nota >= 6):
    print("Aprovado")
else:
    print("Reprovado")
"""

"""
9) Leia um número. Se for par, mostre "Par", senão mostre "Impar".

numero = int(input("Informe um numero: "))
if(numero % 2 == 0):
    print("Par")
else: 
    print("Impar")
"""

"""
10) Leia o valor de uma compra. Se for maior que 100, mostre "Desconto aplicado", senão "Sem desconto".

valorCompra = float(input("Informe o valor da compra: "))
if(valorCompra > 100):
    print("Desconto aplicado")
else:
    print("Sem desconto")
"""

"""
11) Leia a nota de um aluno e classifique:

>= 9  classificação  "Excelente";
>= 7  classificação  "Bom";
>= 5  classificação  "Regular";
  < 5  classificação  "Ruim".

nota = float(input("Informe a nota do aluno: "))
if(nota >= 9):
    print("Excelente")
elif(nota >= 7):
    print("Bom")
elif(nota >= 5):
    print("Regular")
else:    
    print("Ruim")
"""

"""
12) Leia a idade e classifique:

<= 12 classificação  "Criança";
<= 17 classificação  "Adolescente";
<= 59 classificação  "Adulto";
>= 60 classificação  "Idoso".

idade = int(input("Informe a idade: "))
if(idade <= 12):
    print("Criança")
elif(idade <= 17):
    print("Adolescente")
elif(idade <= 59):
    print("Adulto")
else:
    print("Idoso")
"""

"""
13) Leia um número e classifique:

> 0 classificação  "Positivo";
< 0 classificação  "Negativo";
= 0 classificação  "Zero".

numero = int(input("Informe um numero: "))
if(numero > 0):
    print("Positivo")
elif(numero < 0):
    print("Negativo")
else:
    print("Zero")
"""

"""
14) Leia o valor de um produto e classifique de acordo com a regra a seguir:

>= 100 classificação  "Produto caro";
>=   50 classificação  "Produto intermediario";
  <   50 classificação  "Produto barato".

valor = int(input("Informe o valor do produto: "))
if(valor >= 100):
    print("Produto caro")
elif(valor >= 50):
    print("Produto intermediario")
else:
    print("Produto barato")
"""

"""
15) Leia a temperatura e classifique de acordo com os dados a seguir:

>= 30 classificação  "Muito quente";
>= 20 classificação  "Agradavel";
>= 10 classificação  "Frio";
  < 10 classificação  "Muito frio".

temperatura = float(input("Informe a temperatura: "))
if(temperatura >= 30):
    print("Muito quente")
elif(temperatura >= 20):
    print("Agradavel")
elif(temperatura >= 10):
    print("Frio")
else:
    print("Muito frio")
"""

"""
16) Classificação de triângulo. Leia três valores representando os lados de um triângulo. Verifique:

1) Se é possível formar um triângulo (a soma de dois lados deve ser maior que o terceiro) 

2) Caso seja possível, classifique como:

Equilatero (todos os lados iguais);
Isosceles (dois lados iguais);
Escaleno (todos diferentes).

lado1 = float(input("Informe o valor do lado 1: "))
lado2 = float(input("Informe o valor do lado 2: "))
lado3 = float(input("Informe o valor do lado 3: "))
if((lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)):
    if((lado1 == lado2) and (lado1 == lado3)):
        print("Triangulo equilatero")
    elif((lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3)):
        print("Triangulo isosceles")
    else:
        print("Triangulo escaleno")
"""

"""
17) Sistema de notas com conceito. Leia a nota de um aluno (0 a 10) e classifique:

>= 9  classificação  "Excelente"; 
>= 7  classificação  "Bom";  
>= 5  classificação  "Regular "; 
  < 5  classificação  "Insuficiente".

Além disso:

Se a nota for menor que 0 ou maior que 10, mostre "Nota invalida".

nota = float(input("Informe a nota do aluno: "))
if((nota < 0) or (nota > 10)):
    print("Nota invalida")
elif(nota >= 9):
    print("Excelente")
elif(nota >= 7):
    print("Bom")
elif(nota >= 5):
    print("Regular")
else:
    print("Insuficiente")
"""

"""

18) Cálculo de imposto. Leia o salário de um funcionário e calcule o imposto de acordo com as regras a seguir:

Até 2000 é isento;  
Até 4000 aliquota de 10%;  
Acima de 4000 aliquota de 20%.

Se programa deve Mostrar:

O salário informado;
O valor do imposto;
O salário líquido.
"""

"""
19) Calculadora simples. Leia dois números e uma operação (+, -, *, /).

Realize o cálculo conforme a operação informada.

Regras a serem consideradas:

- Se for divisão, verificar se o divisor é zero;
- Se a operação for inválida, mostrar mensagem de erro.
"""

"""
20) Sistema de acesso. Leia:

- Nome do usuário
- Senha

Considere:
Usuário: admin  
Senha: 1234  

Regras:

- Se usuário e senha estiverem corretos, mostrar mensagem: "Acesso permitido";
- Se apenas usuário estiver correto, mostrar mensagem: "Senha incorreta";
- Caso contrário, mostrar: "Usuario invalido".
"""

"""
21) Desafio final

Até aqui você praticou vários exercícios sobre estruturas de decisão (if, if/else e if/elif/else).

Agora vamos dar um passo a mais. 

A ideia é simples: você não será apenas quem resolve problemas… mas também quem os cria.

--------------------------------------------------------------------------

21.1) Criação dos exercícios

Você deverá elaborar 3 exercícios próprios, sendo:

- 1 exercício utilizando apenas IF;
- 1 exercício utilizando IF e ELSE;
- 1 exercício utilizando IF, ELIF e ELSE.

Cada exercício deve:

Ter um enunciado claro e contextualizado, diferente dos que já foram apresentados e resolvidos;
Fazer sentido no mundo real (exemplo: notas, idade, salário, comissão, valor de venda, custo de km de por litro, custo de viagem, etc.);
Indicar claramente o que deve ser exibido como saída.

"""

"""
21.2) Sua resolução

Antes de trocar com um colega, você deve:

Resolver os 3 exercícios que criou; 
Garantir que seu código funciona corretamente; 
Testar pelo menos uma vez. 
"""

"""
21.3) Troca com colega

Após finalizar:

Troque seus exercícios com um colega;
Resolva os exercícios que ele criou;
Compare a solução dele com a sua interpretação. 

"""