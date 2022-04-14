soma=0
ct=0
qtdalunos = int (input())
if qtdalunos == 0:
    print ('NÃO HOUVE PROCESSAMENTO')
    
while ct < qtdalunos:
    media= float (input())
    soma += media
    ct += 1
    if media >= 6.0:
        print ('PARABÉNS VOCÊ ESTÁ APROVADO')
    totalmedia = soma / qtdalunos
if qtdalunos >0:
    print(totalmedia)