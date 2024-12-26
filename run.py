import graphics as gf
from functions import menu, sobre_o_jogo, estrutura, retangulo_vida_c3, retangulo_vida_nave, estrutura_pause, mostra_menu, jogo, fim_de_jogo

win = gf.GraphWin('C3 Invaders', 700, 800, autoflush=False)
itensMenu = menu() 
itensSobre = sobre_o_jogo()
itensJogo = estrutura()
barrasVida = retangulo_vida_c3()
barrasVidaNave = retangulo_vida_nave()
pause = estrutura_pause()
    

loopDoGame = False
while loopDoGame == False:
    mostra_menu(win, itensMenu, itensSobre, itensJogo, barrasVida, barrasVidaNave)
    
    runGame= jogo(win, barrasVida, barrasVidaNave, pause)
    
    final = fim_de_jogo(runGame)
    
    for item in itensJogo:
        item.undraw()
    for item in barrasVida:
        item.undraw()
    for item in barrasVidaNave:
        item.undraw()
    for item in final:
        item.draw(win)
        
    fimMsm= False
    continuou= False
    
    while fimMsm == False and continuou == False:
        clickFinal = win.getMouse()
        
        if 250 < clickFinal.getX() < 330: #     Clicou em continuar
            if 520 < clickFinal.getY() < 560:
                for elem in final:
                    elem.undraw()
                continuou=True

        elif 360 < clickFinal.getX() < 440: #     Clicou em sair
            if 520 < clickFinal.getY() < 560:
                fimMsm=True
                
    if fimMsm == True:
        loopDoGame = True
    if continuou == True:
        continue

win.close()

'''

O código não está devidamente limpo e organizado conforme o ideal, e por isso, talvez sua leitura não esteja amigável.

Entretanto, o objetivo da atividade era exercitar a solução de problemas e a lógica, e com isso, o sistema foi desenvolvido sem preocupações nesse quesito.

'''