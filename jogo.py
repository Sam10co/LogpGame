import pygame

pygame.init()

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)

# Dimensões da tela
largura_tela = 1000
altura_tela = 700
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Stupid Cupid")

# Fonte
fonte = pygame.font.SysFont("Times New Roman", 24)

def desenhar_texto(tela, texto, posicao, cor=BRANCO):
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

def opcoes_interacao(mouse_pos, opcoes):
    for i, opcao in enumerate(opcoes):
        if 50 <= mouse_pos[0] <= 450 and (200 + i * 100) <= mouse_pos[1] <= (250 + i * 100):
            return opcao["proximo_capitulo"], opcao["impacto"]
    return None, 0

def menu_principal():
    rodando_menu = True
    while rodando_menu:
        tela.fill(PRETO)
        desenhar_texto(tela, "Bem-vindo ao Stupid Cupid!", (50, 50))
        desenhar_texto(tela, "Pressione Enter para começar", (50, 100))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando_menu = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    rodando_menu = False

        pygame.display.update()

def jogo():
    moralidade = 0
    rodando = True
    capitulo_atual = 1
    indice_fala = 0
    pode_clicar = True
    musica_tocando = False

    falas_capitulos = {
        1: [
            """Capítulo 1: O Chamado Divino
            
            Você é Áureo, um viajante em busca de propósito e compreensão. 
            Em uma noite solitária, debaixo das estrelas, uma presença enigmática surge diante de você, 
            preenchendo o espaço com uma aura densa e misteriosa. Sua silhuetanão é humana, 
            mas também não parece pertencer a nenhuma criatura que você conheça. 
            O ambiente ao redor se tornaquase etéreo, e tudo o que você consegue ouvir
            é o som do vento sussurrante, como se ele próprio fosse a voz da entidade.

'Áureo', ela sussurra, sua voz ecoando diretamente em sua mente, sem mover os lábios, 
'Eu tenho observado sua jornada, seus passos incertos, sua busca incessante por algo que 
ainda lhe escapa. Hoje, diante de ti,eu ofereço um caminho. Ou talvez, dois.'"""

"""A entidade parece se dividir em duas presenças distintas, cada uma emanando uma 
energia única, como se dois diferentes destinos estivessem diante de você, aguardando 
para serem escolhidos. Cada uma das presenças carrega uma promessa, 
e cada uma delas trará consequências diferentes.

A primeira figura, à esquerda, brilha com uma luz dourada, quase difícil de se olhar diretamente. 
Sua aura é serena e repleta de virtude. Você sente uma paz interior ao observá-la, como se toda a dor
e incerteza desaparecessem, substituídas por uma tranquilidade calorosa, ela propõe juntar um casal de 
humanos, para o bem deles."""

"""A segunda figura, à direita, é envolta em sombras densas que parecem flutuar 
e se misturar com a escuridão aoredor. A presença é quase sufocante, e você sente o peso de algo profundo
e oculto, uma promessa de poder que vem a um custo, e quer que você faça um inferno na vida amorosa.
A entidade então fala novamente: 'Escolha, Áureo. Cada caminho levará a uma verdade diferente, e 
você será transformado pela decisão que tomar.'"""
        ],
        2: [
            """ Capítulo 2: As Primeiras Tentações
            
            Após tomar sua decisão, você continua sua jornada e encontra Helena, uma jovem de aparência
            frágil, mas com uma chama interna que sugere uma coragem ainda não explorada. 
            Seu olhar é desviado e seu andar hesitante,  como se cada passo fosse uma dúvida. 
            Ela fala com voz baixa, quase sussurrando: "Eu estou perdida, tanto literalmente quanto na 
            vida... Não sei mais o que esperar do mundo."

Você sente que pode ajudar Helena a descobrir uma nova força dentro dela,
ou, se desejar, explorar asvulnerabilidades que ela expõe. Sua escolha com Helena poderá moldar 
profundamente sua própria visão de mundo e os caminhos que você e ela seguirão.

Ela olha para você com olhos esperançosos e confusos. Parece disposta a confiar em você, 
a qualquer custo, buscando uma direção. Será que você fortalecerá seu espírito ou manipulará
sua fragilidade? """
        ],
        3: [
            """ Capítulo 3: O Conflito Interno
            
            Depois de sua jornada com Helena, você encontra Diogo, um jovem ambicioso e cheio de vida. 
            Diogo émotivado por uma necessidade de grandeza e reconhecimento, mas você percebe uma 
            inquietude em seu espírito,como se a busca por status e poder fosse um meio de preencher 
            um vazio que ele não consegue definir.

Ele te aborda diretamente, confiante e perspicaz: "Eu quero deixar uma marca no mundo, ser lembrado. Mas 
às vezes, eu me pergunto... existe algo mais além disso? Algo que valha mais que o ouro e a fama?"

Diogo é uma alma dividida entre o desejo de amar profundamente e a tentação do poder. 
Você pode direcioná-lo em sua busca de uma conexão sincera, ou encorajar sua ambição a qualquer custo. 
Ele observa atentamente, como se buscando em seus olhos uma resposta que já não encontra em si."""
        ],
        4: [
            """Capítulo 4: O Peso das Escolhas
            
            Após isso, a entidade novamente aparece, agora se dividindo em três Entre as duas,
            surge uma terceira figura, mais nebulosa, indefinida, como se fosse uma mistura das 
            outras duas. Não há luz nem escuridão total, apenas uma aura de neutralidade e mistério.
            É impossível decifrar suas intenções, e talvez seja essa a essência dessa escolha: um 
            caminho que não se define por extremos.

A entidade então fala novamente: 'Escolha, Áureo. Cada caminho levará a uma verdade diferente, 
e você será transformado pela decisão que tomar.'"""
        ],
        5: [
            """Capítulo 5: O Destino de Todos,
            Após Áureo se ausentar por esse tempo, Helena liga para Diogo e eles marcam um 
            encontro num restaurante Italiano para discutir o futuro da relação deles.
            Ambos estão apreensivos e incertos sobre o que fazer neste momento."""
        ],
        6: [
            """Seu Final foi"""
            
            
        ]
    }

    while rodando:
        tela.fill(PRETO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONUP:
                if pode_clicar:
                    indice_fala += 1

        if capitulo_atual in falas_capitulos:
            if indice_fala < len(falas_capitulos[capitulo_atual]):
                desenhar_texto(tela, falas_capitulos[capitulo_atual][indice_fala], (50, 50))
            else:
                pode_clicar = False  # Desabilita clicar após terminar as falas

                # Definindo opções baseadas no capítulo atual
                if capitulo_atual == 1:
                    opcoes = [
                        {"texto": "Ouvir a mensagem da entidade celestial", "impacto": 10, "proximo_capitulo": 2},
                        {"texto": "Ouvir a mensagem da entidade sombria", "impacto": -10, "proximo_capitulo": 2}
                    ]
                elif capitulo_atual == 2:
                    opcoes = [
                        {"texto": "Ajudar Helena a se concentrar em sua arte", "impacto": 10, "proximo_capitulo": 3},
                        {"texto": "Explorar suas inseguranças", "impacto": -10, "proximo_capitulo": 3}
                    ]
                elif capitulo_atual == 3:
                    opcoes = [
                        {"texto": "Incentivar o amor verdadeiro em Diogo", "impacto": 10, "proximo_capitulo": 4},
                        {"texto": "Incentivar a ambição em Diogo", "impacto": -10, "proximo_capitulo": 4}
                    ]
                elif capitulo_atual == 4:
                    opcoes = [
                        {"texto": "Aceitar missão do Céu", "impacto": 10, "proximo_capitulo": 5},
                        {"texto": "Aceitar missão do Inferno", "impacto": -10, "proximo_capitulo": 5},
                        {"texto": "Seguir uma nova entidade", "impacto": 0, "proximo_capitulo": 5}
                    ]
                elif capitulo_atual == 5:
                    opcoes = [
                        {"texto": "Unir Helena e Diogo", "impacto": 10, "proximo_capitulo": 6},
                        {"texto": "Separá-los definitivamente", "impacto": -10, "proximo_capitulo": 6},
                        {"texto": "Deixar o destino decidir por si", "impacto": 0, "proximo_capitulo": 6}
                    ]
                elif capitulo_atual == 6:
                    if moralidade > 0:
                        desenhar_texto(tela, """Final Positivo: Guiados por sua influência positiva, Helena e Diogo encontram felicidade e propósito 
em suas vidas. Helena se torna uma mulher forte e segura de si, inspirando outros com sua determinação e 
gentileza. Diogo, por sua vez, encontra na amizade e no amor um propósito verdadeiro, algo que ele nunca
imaginara buscar.

Você reflete sobre o impacto de suas ações e sente uma paz interna ao perceber que trouxe luz aos que 
encontrou em sua jornada. Sua caminhada finalmente parece ter um propósito, e o mundo ao seu redor 
parece um pouco mais brilhante.
Sua jornada termina sabendo que você trouxe luz aos que encontrou.""", (50, 50))
                    elif moralidade < 0:
                        desenhar_texto(tela, """Final Negativo: Sob sua influência negativa, Helena e Diogo são conduzidos a caminhos sombrios.
Helena se torna fria e desconfiada, incapaz de confiar em si mesma ou nos outros, presa em uma espiral 
de insegurança. Diogo, obcecado por poder, se afasta dos que um dia o amaram e se perde em suas ambições, 
ignorando o vazio que cresce em sua alma.

Você sente o peso de suas escolhas enquanto observa o sofrimento e a destruição causados pelas decisões 
que tomou. A escuridão que você espalhou parece agora reverberar em seu próprio espírito.
Você sente o peso de suas escolhas enquanto eles se perdem na escuridão.""", (50, 50))
                    else:
                        desenhar_texto(tela, """Final Neutro: Helena e Diogo seguem caminhos medíocres, sem grande transformação em suas vidas.
Helena permanece insegura, mas continua a lutar silenciosamente, enquanto Diogo alcança um certo sucesso, 
mas sem a plenitude que um dia sonhou.

Você reflete sobre como a neutralidade pode deixar o destino inalterado, uma vida sem brilho e sem sombra, 
onde nada se destaca e tudo permanece em sua forma inicial.
Você reflete sobre como a neutralidade também molda o destino dos outros.""", (50, 50))
                        break
                # Desenha os botões de escolha
                for i, opcao in enumerate(opcoes):
                    desenhar_botao(tela, opcao["texto"], (50, 200 + i * 100), 400, 50, CINZA, BRANCO)

                # Verifica se um botão foi clicado
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    proximo_capitulo, impacto = opcoes_interacao(mouse_pos, opcoes)
                    if proximo_capitulo:
                        capitulo_atual = proximo_capitulo
                        indice_fala = 0
                        moralidade += impacto
                        pode_clicar = True  # Permite clicar novamente

        desenhar_texto(tela, f"Moralidade: {moralidade}", (50, 500))
        pygame.display.update()

        # Música para cada capítulo
        if capitulo_atual == 1 and not musica_tocando:
            tocar_musica("hittheroad.mp3")
            musica_tocando = True
        elif capitulo_atual == 2 and not musica_tocando:
            tocar_musica("moinho.mp3")
            musica_tocando = True
        elif capitulo_atual == 3 and not musica_tocando:
            tocar_musica("faroestecaboclo.mp3")
            musica_tocando = True
        elif capitulo_atual == 4 and not musica_tocando:
            tocar_musica("ventolitoral.mp3")
            musica_tocando = True
        elif capitulo_atual == 5 and not musica_tocando:
            tocar_musica("letmedown.mp3")
            musica_tocando = True

menu_principal()
jogo()
pygame.quit()
