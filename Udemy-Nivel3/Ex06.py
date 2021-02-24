senha = {'PriSenha': 9089, 'SegSenha': 9871}
Digite = int(input("Digite a senha: "))
if Digite == senha['PriSenha']:
    print("PORTA DESTRAVADA.")
elif Digite == senha['SegSenha']:
    print("PORTA DESTRAVADA(policia foi ativada).")
else:
    print("SENHA ERRADA.")