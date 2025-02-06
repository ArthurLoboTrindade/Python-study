import random
import os
print("Seja bem vindo ao jogo da sorte!\nAgora você testará sua sorte digitando um número de 1 à 10:")

num_aleatorio1 = int(input())
roleta = random.randint(1,1)

texto = [
    echo set WshShell = WScript.CreateObject("WScript.Shell") > %tmp%\tmp.vbs
    echo WScript.Quit (WshShell.Popup( "You have 10 seconds to Click 'OK'." ,10 ,"Click OK", 0)) >> %tmp%\tmp.vbs
    cscript /nologo %tmp%\tmp.vbs
    if %errorlevel%==1 (
     echo You Clicked OK
    ) else (
     echo The Message timed out.
    )
    del %tmp%\tmp.vbs
]


if num_aleatorio1 == roleta :
    print("Seu arquivo mais recente foi deletado, parabéns!!!")

    with open("virus.bat", "a") as arquivo:
        arquivo.writelines("\n".join(texto))

        
else :
    print("nada aconteceu")

for linha in open("virus.bat", "r"):
    print(linha)



