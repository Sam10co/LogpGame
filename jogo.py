import pygame

pygame.init()

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)

largura_tela = 1000
altura_tela = 700
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo de Moralidade")

fonte = pygame.font.SysFont("Arial", 24)

def desenhar_texto(tela, texto, posicao, cor=PRETO):
    linhas = texto.split("\n")
    y_offset = 0
    for linha in linhas:
        renderizada = fonte.render(linha, True, cor)
        tela.blit(renderizada, (posicao[0], posicao[1] + y_offset))
        y_offset += 30

def tocar_musica(caminho):
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

def desenhar_botao(tela, texto, posicao, largura, altura, cor_botao, cor_texto):
    pygame.draw.rect(tela, cor_botao, (posicao[0], posicao[1], largura, altura))
    desenhar_texto(tela, texto, (posicao[0] + 10, posicao[1] + 10), cor_texto)

def opcoes_interacao(mouse_pos, opcoes, moralidade):
    for i, opcao in enumerate(opcoes):
        if 50 <= mouse_pos[0] <= 450 and (200 + i * 100) <= mouse_pos[1] <= (250 + i * 100):
            moralidade += opcao["impacto"]
            return opcao["proximo_capitulo"], moralidade
    return None, moralidade

def jogo():
    moralidade = 0
    rodando = True
    capitulo_atual = 1
    pode_clicar = True
    musica_tocando = False  # Variável para controlar a música

    while rodando:
        tela.fill(BRANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONUP:
                pode_clicar = True

        if capitulo_atual == 1:
            if not musica_tocando:
                tocar_musica("ventolitoral.mp3")
                musica_tocando = True

            desenhar_texto(tela, "Capítulo 1: O Chamado Divino", (50, 50))
            desenhar_texto(tela,"Áureo, o cupido, é convocado para uma missão importante.", (50, 100))
            desenhar_texto(tela,"Você se encontra no reino celeste, diante de duas entidades:", (50, 130))
            

            opcoes = [
                {"texto": "Ouvir a mensagem da entidade celestial", "impacto": 10, "proximo_capitulo": 2},
                {"texto": "Ouvir a mensagem da entidade sombria", "impacto": -10, "proximo_capitulo": 2}
            ]

            for i, opcao in enumerate(opcoes):
                desenhar_botao(tela, opcao["texto"], (50, 200 + i * 100), 400, 50, CINZA, PRETO)

            if evento.type == pygame.MOUSEBUTTONDOWN and pode_clicar:
                mouse_pos = pygame.mouse.get_pos()
                proximo_capitulo, moralidade = opcoes_interacao(mouse_pos, opcoes, moralidade)
                if proximo_capitulo:
                    capitulo_atual = proximo_capitulo
                    pode_clicar = False
                    musica_tocando = False

        elif capitulo_atual == 2:
            if musica_tocando == False:
                tocar_musica("hittheroad.mp3")
                musica_tocando = True

            desenhar_texto(tela, "Capítulo 2: As Primeiras Tentações", (50, 50))
            desenhar_texto(tela,"Helena fala sobre seu relacionamento com Diogo.", (50, 100))
            desenhar_texto(tela,"Ela parece confusa e vulnerável.", (50, 130))

            opcoes = [
                {"texto": "Ajudar Helena a se concentrar em sua arte", "impacto": 5, "proximo_capitulo": 3},
                {"texto": "Explorar suas inseguranças", "impacto": -5, "proximo_capitulo": 3}
            ]

            for i, opcao in enumerate(opcoes):
                desenhar_botao(tela, opcao["texto"], (50, 200 + i * 100), 400, 50, CINZA, PRETO)

            if evento.type == pygame.MOUSEBUTTONDOWN and pode_clicar:
                mouse_pos = pygame.mouse.get_pos()
                proximo_capitulo, moralidade = opcoes_interacao(mouse_pos, opcoes, moralidade)
                if proximo_capitulo:
                    capitulo_atual = proximo_capitulo
                    pode_clicar = False
                    musica_tocando = False

        elif capitulo_atual == 3:
            if not musica_tocando:
                tocar_musica("letmedown.mp3")
                musica_tocando = True

            desenhar_texto(tela, "Capítulo 3: O Conflito Interno", (50, 50))
            desenhar_texto(tela,"Helena se sente ainda mais insegura.", (50, 100))
            desenhar_texto(tela,"Ela pergunta se Diogo ainda a ama.", (50, 130))

            opcoes = [
                {"texto": "Aconselhar Helena a buscar uma reconciliação com Diogo", "impacto": 10, "proximo_capitulo": 4},
                {"texto": "Incentivar Helena a seguir em frente", "impacto": -10, "proximo_capitulo": 4}
            ]

            for i, opcao in enumerate(opcoes):
                desenhar_botao(tela, opcao["texto"], (50, 200 + i * 100), 400, 50, CINZA, PRETO)

            if evento.type == pygame.MOUSEBUTTONDOWN and pode_clicar:
                mouse_pos = pygame.mouse.get_pos()
                proximo_capitulo, moralidade = opcoes_interacao(mouse_pos, opcoes, moralidade)
                if proximo_capitulo:
                    capitulo_atual = proximo_capitulo
                    pode_clicar = False
                    musica_tocando = False

        elif capitulo_atual == 4:
            if not musica_tocando:
                tocar_musica("faroestecaboclo.mp3")
                musica_tocando = True

            desenhar_texto(tela, "Capítulo 4: O Peso das Escolhas", (50, 50))
            desenhar_texto(tela,"Helena e Diogo estão em um ponto de ruptura.", (50, 100))
            desenhar_texto(tela,"Você deve decidir o que fazer a seguir.", (50, 130))

            opcoes = [
                {"texto": "Aceitar missão do Céu para restaurar o relacionamento", "impacto": 10, "proximo_capitulo": 5},
                {"texto": "Aceitar missão do Inferno para destruí-los", "impacto": -10, "proximo_capitulo": 5},
                {"texto": "Seguir uma nova entidade", "impacto": 0, "proximo_capitulo": 5}
            ]

            for i, opcao in enumerate(opcoes):
                desenhar_botao(tela, opcao["texto"], (50, 200 + i * 100), 400, 50, CINZA, PRETO)

            if evento.type == pygame.MOUSEBUTTONDOWN and pode_clicar:
                mouse_pos = pygame.mouse.get_pos()
                proximo_capitulo, moralidade = opcoes_interacao(mouse_pos, opcoes, moralidade)
                if proximo_capitulo:
                    capitulo_atual = proximo_capitulo
                    pode_clicar = False
                    musica_tocando = False

        elif capitulo_atual == 5:
            if not musica_tocando:
                tocar_musica("Birds.mp3")
                musica_tocando = True

            desenhar_texto(tela, "Capítulo 5: O Destino de Todos", (50, 50))
            desenhar_texto(tela,"Helena e Diogo se encontram para discutir o futuro.", (50, 100))
            desenhar_texto(tela,"Ambos estão incertos sobre o que fazer.", (50, 130))

            opcoes = [
                {"texto": "Unir Helena e Diogo de uma vez por todas", "impacto": 10, "proximo_capitulo": 6},
                {"texto": "Separá-los definitivamente", "impacto": -10, "proximo_capitulo": 6},
                {"texto": "Deixar o destino decidir por si", "impacto": 0, "proximo_capitulo": 6}
            ]

            for i, opcao in enumerate(opcoes):
                desenhar_botao(tela, opcao["texto"], (50, 200 + i * 100), 400, 50, CINZA, PRETO)

            if evento.type == pygame.MOUSEBUTTONDOWN and pode_clicar:
                mouse_pos = pygame.mouse.get_pos()
                proximo_capitulo, moralidade = opcoes_interacao(mouse_pos, opcoes, moralidade)
                if proximo_capitulo:
                    capitulo_atual = proximo_capitulo
                    pode_clicar = False
                    musica_tocando = False

        elif capitulo_atual == 6:
            if not musica_tocando:
                tocar_musica("moinho.mp3")
                musica_tocando = True

            if moralidade > 0:
                desenhar_texto(tela, "Final Celestial", (50, 50))
                desenhar_texto(tela,"Você seguiu o caminho do Céu. Helena e Diogo se reconciliam e vivem em paz.", (50, 100))
            elif moralidade < 0:
                desenhar_texto(tela, "Final Infernal", (50, 50))
                desenhar_texto(tela,"Você seguiu o caminho do Inferno. Helena e Diogo se separam e vivem em sofrimento.", (50, 100))
            else:
                desenhar_texto(tela, "Final Neutro", (50, 50))
                desenhar_texto(tela,"Você seguiu o caminho da neutralidade. Helena e Diogo seguem suas vidas separadamente.", (50, 100))

            desenhar_texto(tela, "Obrigado por jogar!", (50, 200))

        desenhar_texto(tela, f"Moralidade: {moralidade}", (50, 500))
        pygame.display.update()

jogo()
pygame.quit()

