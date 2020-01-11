import hamming

manipulador = open('binario.txt', 'r')
escrever = open('hamming.txt', 'w')

# codigo ainda sera melhorado para ler o numero de linhas
i = 0
hamming_txt = []
while i < 12: # 12 é o numero de linhas do arquivo de binários.
    binario = manipulador.readline()
    new_binario = []
    print(binario)
    for value in binario:
        if value != '\n':
            new_binario.append(value)
    print(new_binario)
    convertido = hamming.hamming(new_binario, 0)
    hamming_txt.append(convertido)
    print(convertido)
    print('-----------------------------------')
    i += 1
manipulador.close()
escrever.writelines(str(hamming_txt))

escrever.close()

'''@programador_who - aulas particulares de programacao '''
