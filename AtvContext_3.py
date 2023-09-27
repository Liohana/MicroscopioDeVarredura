""""
Esse programa tem como objetivo receber informações para utilização de um microscopia de varredura.
"""

#definir variáveis:
microscopio = "MEV"
celula = "A1"
resolucao = 1 #nm
iluminacao = 5 #keV
tamanho_largura = 100 #nm
tamanho_altura = 10 #nm
tamanho_espessura = 1 #nm
ambiente = "Vacuo"
preparo = "Platina"
contraste = "DE"

#informações necessárias:
microscopioInf = input('Tipo específico de microscópio de varredura que será utilizado: ')
print('Houve alteração na variável inserida?')
print(microscopio!=microscopioInf)

celulaInf = input('Tipo de célula a ser escaneada: ')
print('Houve alteração na variável inserida?')
print(celula!=celulaInf)

resolucaoInf = input('Resolução da imagem desejada: ')
print('Houve alteração na variável inserida?')
print(resolucao!=resolucaoInf)

iluminacaoInf = input('Faixa de iluminação necessária: ')
print('Houve alteração na variável inserida?')
print(iluminacao!=iluminacaoInf)

tamanho_larguraInf = input('Largura da amostra: ')
print('Houve alteração na variável inserida?')
print(tamanho_largura!=tamanho_larguraInf)

tamanho_alturaInf = input('Altura da amostra: ')
print('Houve alteração na variável inserida?')
print(tamanho_altura!=tamanho_alturaInf)

tamanho_espessuraInf = input('Espessura da amostra: ')
print('Houve alteração na variável inserida?')
print(tamanho_espessura!=tamanho_espessuraInf)

ambienteInf = input('Condições de vácuo ou atmosfera controlada necessárias para a análise da amostra: ')
print('Houve alteração na variável inserida?')
print(ambiente!=ambienteInf)

preparoInf = input('Método de preparação de amostra necessário: ')
print('Houve alteração na variável inserida?')
print(preparo!=preparoInf)

contrasteInf = input('Tipo de contraste é mais relevante para a sua análise: ')
print('Houve alteração na variável inserida?')
print(contraste!=contrasteInf)

#Informações digitadas:

print("As informações de configurações setadas pelo usuário são:")
print("Resolução da imagem: ", microscopioInf)
print("Tipo de célula a ser escaneada: ", celulaInf)
print('Resolução da imagem desejada: ', resolucaoInf)
print('Faixa de iluminação necessária: ', iluminacaoInf)
print('Largura da amostra: ', tamanho_larguraInf)
print('Altura da amostra: ', tamanho_alturaInf)
print('Espessura da amostra: ', tamanho_espessuraInf)
print('Condições de vácuo ou atmosfera controlada necessárias para a análise da amostra: ', ambienteInf)
print('Método de preparação de amostra necessário: ', preparoInf)
print('Tipo de contraste é mais relevante para a sua análise: ', contrasteInf)

#Calibração no sentido horizontal:

ultimaLetra = "a"

calibração_horizontal1 = input("Digite a última letra do seu nome")
print("A informção foi corretamente digitada:", (ultimaLetra == calibração_horizontal1), calibração_horizontal1)
calibração_horizontal2 = input("Digite a última letra do seu nome")
print("A informção foi corretamente digitada:", (ultimaLetra == calibração_horizontal2), calibração_horizontal2)
calibração_horizontal3 = input("Digite a última letra do seu nome")
print("A informção foi corretamente digitada:", (ultimaLetra == calibração_horizontal3), calibração_horizontal3)
calibração_horizontal4 = input("Digite a última letra do seu nome")
print("A informção foi corretamente digitada:", (ultimaLetra == calibração_horizontal4), calibração_horizontal4)
calibração_horizontal5 = input("Digite a última letra do seu nome")
print("A informção foi corretamente digitada:", (ultimaLetra == calibração_horizontal5), calibração_horizontal5)
calibração_horizontal6 = input("Digite a última letra do seu nome")
print("A informção foi corretamente digitada:", (ultimaLetra == calibração_horizontal6), calibração_horizontal6)
calibração_horizontal7 = input("Digite a última letra do seu nome")
print("A informção foi corretamente digitada:", (ultimaLetra == calibração_horizontal7), calibração_horizontal7)
calibração_horizontal8 = input("Digite a última letra do seu nome")
print("A informção foi corretamente digitada:", (ultimaLetra == calibração_horizontal8), calibração_horizontal8)
calibração_horizontal9 = input("Digite a última letra do seu nome")
print("A informção foi corretamente digitada:", (ultimaLetra == calibração_horizontal9), calibração_horizontal9)
calibração_horizontal10 = input("Digite a última letra do seu nome")
print("A informção foi corretamente digitada:", (ultimaLetra == calibração_horizontal10), calibração_horizontal10)

primeiraLetra = "l"

calibração_horizontal11 = input("Digite a primeira letra do seu nome")
print("A informção foi corretamente digitada:", (primeiraLetra == calibração_horizontal11), calibração_horizontal11)
calibração_horizontal12 = input("Digite a primeira letra do seu nome")
print("A informção foi corretamente digitada:", (primeiraLetra == calibração_horizontal12), calibração_horizontal12)
calibração_horizontal13 = input("Digite a primeira letra do seu nome")
print("A informção foi corretamente digitada:", (primeiraLetra == calibração_horizontal13), calibração_horizontal13)
calibração_horizontal14 = input("Digite a primeira letra do seu nome")
print("A informção foi corretamente digitada:", (primeiraLetra == calibração_horizontal14), calibração_horizontal14)
calibração_horizontal15 = input("Digite a primeira letra do seu nome")
print("A informção foi corretamente digitada:", (primeiraLetra == calibração_horizontal15), calibração_horizontal15)
calibração_horizontal16 = input("Digite a primeira letra do seu nome")
print("A informção foi corretamente digitada:", (primeiraLetra == calibração_horizontal16), calibração_horizontal16)
calibração_horizontal17 = input("Digite a primeira letra do seu nome")
print("A informção foi corretamente digitada:", (primeiraLetra == calibração_horizontal17), calibração_horizontal17)
calibração_horizontal18 = input("Digite a primeira letra do seu nome")
print("A informção foi corretamente digitada:", (primeiraLetra == calibração_horizontal18), calibração_horizontal18)
calibração_horizontal19 = input("Digite a primeira letra do seu nome")
print("A informção foi corretamente digitada:", (primeiraLetra == calibração_horizontal19), calibração_horizontal19)
calibração_horizontal20 = input("Digite a primeira letra do seu nome")
print("A informção foi corretamente digitada:", (primeiraLetra == calibração_horizontal20), calibração_horizontal20)


#Calibração no sentido vertical 

penultimaLetra = "n"

calibração_vertical1 = input("Digite a penúltima letra do seu nome")
print("A informção foi corretamente digitada:", (penultimaLetra == calibração_vertical1), calibração_vertical1)
calibração_vertical2 = input("Digite a penúltima letra do seu nome")
print("A informção foi corretamente digitada:", (penultimaLetra == calibração_vertical2), calibração_vertical2)
calibração_vertical3 = input("Digite a penúltima letra do seu nome")
print("A informção foi corretamente digitada:", (penultimaLetra == calibração_vertical3), calibração_vertical3)
calibração_vertical4 = input("Digite a penúltima letra do seu nome")
print("A informção foi corretamente digitada:", (penultimaLetra == calibração_vertical4), calibração_vertical4)
calibração_vertical5 = input("Digite a penúltima letra do seu nome")
print("A informção foi corretamente digitada:", (penultimaLetra == calibração_vertical5), calibração_vertical5)
calibração_vertical6 = input("Digite a penúltima letra do seu nome")
print("A informção foi corretamente digitada:", (penultimaLetra == calibração_vertical6), calibração_vertical6)
calibração_vertical7 = input("Digite a penúltima letra do seu nome")
print("A informção foi corretamente digitada:", (penultimaLetra == calibração_vertical7), calibração_vertical7)
calibração_vertical8 = input("Digite a penúltima letra do seu nome")
print("A informção foi corretamente digitada:", (penultimaLetra == calibração_vertical8), calibração_vertical8)
calibração_vertical9 = input("Digite a penúltima letra do seu nome")
print("A informção foi corretamente digitada:", (penultimaLetra == calibração_vertical9), calibração_vertical9)
calibração_vertical10 = input("Digite a penúltima letra do seu nome")
print("A informção foi corretamente digitada:", (penultimaLetra == calibração_vertical10), calibração_vertical10)

segundaLetra = "i"

calibração_vertical11 = input("Digite a segunda letra do seu nome")
print("A informção foi corretamente digitada:", (segundaLetra == calibração_vertical11), calibração_vertical11)
calibração_vertical12 = input("Digite a segunda letra do seu nome")
print("A informção foi corretamente digitada:", (segundaLetra == calibração_vertical12), calibração_vertical12)
calibração_vertical13 = input("Digite a segunda letra do seu nome")
print("A informção foi corretamente digitada:", (segundaLetra == calibração_vertical13), calibração_vertical13)
calibração_vertical14 = input("Digite a segunda letra do seu nome")
print("A informção foi corretamente digitada:", (segundaLetra == calibração_vertical14), calibração_vertical14)
calibração_vertical15 = input("Digite a segunda letra do seu nome")
print("A informção foi corretamente digitada:", (segundaLetra == calibração_vertical15), calibração_vertical15)
calibração_vertical16 = input("Digite a segunda letra do seu nome")
print("A informção foi corretamente digitada:", (segundaLetra == calibração_vertical16), calibração_vertical16)
calibração_vertical17 = input("Digite a segunda letra do seu nome")
print("A informção foi corretamente digitada:", (segundaLetra == calibração_vertical17), calibração_vertical17)
calibração_vertical18 = input("Digite a segunda letra do seu nome")
print("A informção foi corretamente digitada:", (segundaLetra == calibração_vertical18), calibração_vertical18)
calibração_vertical19 = input("Digite a segunda letra do seu nome")
print("A informção foi corretamente digitada:", (segundaLetra == calibração_vertical19), calibração_vertical19)
calibração_vertical20 = input("Digite a segunda letra do seu nome")
print("A informção foi corretamente digitada:", (segundaLetra == calibração_vertical20), calibração_vertical20)

print('Fim da calibração do sistema.')
