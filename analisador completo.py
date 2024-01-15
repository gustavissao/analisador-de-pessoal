somaidade = 0
médiaidade = 0
maioridadem = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
    print(F'----- {p}° pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadem:
        maioridadem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
médiaidade = somaidade / 4
print(f'A media de idade do grupo é de {médiaidade:.1f} anos')
print(f'a idade do mais velho tem {maioridadem} anos e se chama {nomevelho}')
print(f'o numero de mulheres com menos de 20 são, {totmulher} mulheres')