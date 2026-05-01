import random
import time
import os

# sistema de sanidade

sanidade = 100

def atualizar_sanidade(erros):
    global sanidade
    perda = 8 + (erros * 3)
    sanidade -= perda
    if sanidade < 0:
        sanidade = 0
    return sanidade

def distorcer_texto(texto, sanidade):
    chance_erro = (100 - sanidade) / 300  
    novo = ""

    for letra in texto:
        if letra.isalpha() and random.random() < chance_erro:
            tipo = random.choice(["troca", "remove", "duplica"])

            if tipo == "troca":
                novo += chr(random.randint(97, 122))

            elif tipo == "remove":
                continue

            elif tipo == "duplica":
                novo += letra * 2
        else:
            novo += letra

    return novo

def time_clean(segundos):
    time.sleep(segundos)
    os.system('cls')

def humor_banbaleena(erros):
    if erros == 0:
        return "fofa"
    elif erros == 1:
        return "calma"
    elif erros == 2:
        return "irritada"
    elif erros == 3:
        return "brava"
    elif erros == 4:
        return "furiosa"
    else:
        return "maluca"

# expressoes
def falar_banbaleena(texto, erros):
    humor = humor_banbaleena(erros)

    if humor == "fofa":
        velocidade = 0.05
    elif humor == "calma":
        velocidade = 0.035
    elif humor == "irritada":
        velocidade = 0.03
    elif humor == "brava":
        velocidade = 0.02
    elif humor == "furiosa":
        velocidade = 0.015
        texto = texto.upper()
    else:  # MALUCA
        velocidade = 0.005
        texto = texto.upper()

    if erros > 0:
        texto = distorcer_texto(texto, sanidade)

    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidade)
    print()


def falas(texto):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.05)
    print()

erros = 0

# introducao

falas("Carregando…")
falas("\n...")

falas("\n[Detectando usuário…]")
falas("\n[Observando padrões de sombra…]")

falas("\nErro: Forma inadequada. Ajustando para modelo 'Banbaleena'.")

time_clean(4)

# inicio do jogo

falar_banbaleena("Olá! Eu sou a Banbaleena! ♡", erros)
falar_banbaleena("e estou aqui para brincar de adivinhação e continhas com você!", erros)
time_clean(4)
falar_banbaleena("Não se preocupe, eu não assusto... ainda.", erros)
time_clean(2)
falar_banbaleena("Para a primeira partida, vou pensar em um número de 1 a 10, e você terá 10 segundos para adivinhá-lo.", erros)
falar_banbaleena("Será divertido se você acertar!", erros)
time_clean(4)
falar_banbaleena("Então, eu te pergunto: você está pronto?", erros)

input("> ")

falar_banbaleena("Já que sua resposta foi 'sim', vamos lá!", erros)
time_clean(1)

for t in range(10, 0, -1):
    print(f"Pense num número de 1 a 10. Você tem {t} segundos...      ", end="\r")
    time.sleep(1)

print(" " * 60, end="\r")
falar_banbaleena("O tempo acabou!", erros)
time_clean(1.5)

segredo = random.randint(1, 10)

falar_banbaleena("Que número você acha que eu pensei?", erros)
palpite = int(input("> "))

falar_banbaleena("Processando seu palpite...", erros)
time_clean(1.5)

# resultado da primeira partida

if palpite == segredo:
    falar_banbaleena("Parabéns! Você acertou! Acho que estamos em sintonia. ♡", erros)
else:
    falar_banbaleena(f"Eu pensei no número {segredo}. Mas tudo bem, vamos continuar!", erros)
    erros += 1
    atualizar_sanidade(erros)

time_clean(2)

# atualizando o humor

falar_banbaleena("Carregando segunda partida...", erros)
time_clean(2)

# segunda partida

falar_banbaleena("Agora, na segunda partida vamos fazer uma continha pra ver o quão bom você é em matemática! hahaha", erros)
time_clean(1.5)
falar_banbaleena("Brincadeiras à parte, quero que me diga quanto é 15 x 5.", erros)
time_clean(1.5)
falar_banbaleena("Você terá 15 segundos pra pensar, facinho né?", erros)
time_clean(1.5)
falar_banbaleena("Preparado?", erros)

input("> ")
time_clean(1.5)

for t in range(15, 0, -1):
    print(f"Quanto é 15 x 5? Você tem {t} segundos...      ", end="\r")
    time.sleep(1)

print(" " * 60, end="\r")

falar_banbaleena("O tempo acabou!", erros)
time_clean(1.5)

falar_banbaleena("Qual foi o resultado que você conseguiu?", erros)
palpite = int(input("> "))

falar_banbaleena("Processando sua resposta...", erros)
time_clean(1.5)

if palpite == 125:
    falar_banbaleena("Parabéns, você acertou! Estou muito feliz por isso!!!", erros)
else:
    falar_banbaleena("Errou de novo... ok. Se precisar, eu te ajudo na próxima, tá bom?", erros)
    erros += 1
    atualizar_sanidade(erros)

time_clean(2)

# atualizando o humor

falar_banbaleena("Carregando terceira partida...", erros)
time_clean(2)

# terceira partida

falar_banbaleena("Vamos para mais uma adivinhação, e se você errou a primeira, espero que acerte essa! hehe", erros)
time_clean(3)
falar_banbaleena("Vai ser no mesmo esquema que da última vez, ok? A diferença vai ser que vou pensar num número de 1 a 20. Se prepare e pense bem na sua resposta...", erros)
time_clean(4)

for t in range(10, 0, -1):
    print(f"Pense num número de 1 a 20. Você tem {t} segundos...      ", end="\r")
    time.sleep(1)

print(" " * 60, end="\r")

falar_banbaleena("O tempo acabou!", erros)
time_clean(1.5)

segredo = random.randint(1, 20)

falar_banbaleena("Qual número você chuta dessa vez?", erros)
palpite = int(input("> "))

falar_banbaleena("Processando seu palpite...", erros)
time_clean(1.5)

# resultado da terceira partida

if palpite == segredo:
    falar_banbaleena("Muito bem, você acertou!", erros)
else:
    falar_banbaleena(f"Eu pensei no número {segredo}. Isso é decepcionante, sabia?", erros)
    erros += 1
    atualizar_sanidade(erros)

time_clean(2)

# atualizando o humor

falar_banbaleena("Carregando quarta partida...", erros)
time_clean(2)

# quarta partida

falar_banbaleena("Pra essa continha, vamos fazer algo mais difícil pra provar mais ainda o seu potêncial!", erros)
time_clean(1.5)
falar_banbaleena("Quero que descubra o valor de x na equação a seguir: x^2−11x+28=0. Vou te dar 30 segundos para resolver, tenho certeza que você consegue!", erros)
time_clean(4)

for t in range(30, 0, -1):
    print(f"Qual o valor de x em x^2−11x+28=0? Você tem {t} segundos...      ", end="\r")
    time.sleep(1)

print(" " * 60, end="\r")

falar_banbaleena("O tempo acabou!", erros)
time_clean(1.5)

falar_banbaleena("Qual o valor das raízes?", erros)
palpite = input("> ")

falar_banbaleena("Processando sua resposta...", erros)
time_clean(1.5)

if palpite == "4, 7":
    falar_banbaleena("Muito bem.", erros)
else:
    falar_banbaleena(f"Sério mesmo que você errou de novo? Seu raciocínio está devagar... será que consegue melhorar?", erros)
    erros += 1
    atualizar_sanidade(erros)

time_clean(2)

# atualizando o humor

falar_banbaleena("Carregando quinta partida...", erros)
time_clean(2)

# quinta partida

falar_banbaleena("Como eu amo adivinhações, vou te contar mais uma e tenho certeza de que você vai acertar dessa vez! Pelo menos é isso que eu espero...", erros)
time_clean(1.5)
falar_banbaleena("Você terá 20 segundos pra pensar, prometo que não é difícil. :)", erros)
time_clean(4)

print("Não tenho boca, mas conto histórias. Não tenho olhos, mas mostro mundos. Não tenho pernas, mas posso te levar muito longe. Quem sou eu?")
for t in range(20, 0, -1):
    print(f"Você tem {t} segundos...      ", end="\r")
    time.sleep(1)
print(" " * 60, end="\r") 


falar_banbaleena("O tempo acabou!", erros)
time_clean(1.5)

falar_banbaleena("Qual é a resposta?", erros)
palpite = input("> ")

falar_banbaleena("Processando sua resposta...", erros)
time_clean(1.5)

if palpite == "livro":
    falar_banbaleena("Não esperava que fosse acertar.", erros)
else:
    falar_banbaleena(f"Sério mesmo que você errou? A resposta era 'livro'. Você é ruim em adivinhações, não acha?", erros)
    erros += 1
    atualizar_sanidade(erros)

time_clean(2)

# atualizando o humor

falar_banbaleena("Carregando sexta partida...", erros)
time_clean(2)

# sexta partida

falar_banbaleena("Quero que você me diga qual é o número multiplicado por 7 que é igual ao mesmo número somado com 48. Você terá 10 segundos, se prepare...", erros)
time_clean(4)

for t in range(10, 0, -1):
    print(f"Um número multiplicado por 7 é igual ao mesmo número somado com 48. Qual é esse número?\nVocê tem {t} segundos...      ", end="\r")
    time.sleep(1)

print(" " * 60, end="\r")

falar_banbaleena("O tempo acabou!", erros)
time_clean(1.5)

falar_banbaleena("Qual é o número?", erros)
palpite = input("> ")

falar_banbaleena("Processando sua resposta...", erros)
time_clean(1.5)

if palpite == "8":
    falar_banbaleena("Estou impressionada, até que você não é tão ruim.", erros)
else:
    falar_banbaleena("A resposta era 8.")
    time_clean(2)
    falar_banbaleena(f"Estou ficando irritada, não subestime minhas sombras. Preste mais atenção.", erros)
    erros += 1
    atualizar_sanidade(erros)

time_clean(2)

# atualizando o humor

falar_banbaleena("Carregando sétima partida...", erros)
time_clean(2)

# setima partida

falar_banbaleena("Não sei se ainda vale a pena tentar fazer você adivinhar charadas tão legais quanto as minhas, mas vou te dar mais um voto de confiança...", erros)
time_clean(4)

for t in range(10, 0, -1):
    print(f"Não tenho rosto, mas você sente quando eu te encaro.\nNão tenho voz, mas você me ouve quando está sozinho.\nSó apareço quando sua coragem começa a falhar.\nVocê tem {t} segundos...      ", end="\r")
    time.sleep(1)

print(" " * 60, end="\r")

falar_banbaleena("O tempo acabou!", erros)
time_clean(1.5)

falar_banbaleena("O que eu sou?", erros)
palpite = input("> ")

falar_banbaleena("Processando sua resposta...", erros)
time_clean(1.5)

if palpite == "A presença que divide o quarto com você":
    falar_banbaleena("Só porque duvidei da sua capacidade, você acertou. Tô surpresa.", erros)
else:
    falar_banbaleena(f"NÃO ME FAÇA REPETIR... isso está ficando cansativo.", erros)
    erros += 1
    atualizar_sanidade(erros)

time_clean(2)

# atualizando o humor

falar_banbaleena("Carregando oitava partida...", erros)
time_clean(2)

# oitava partida

falar_banbaleena("Vamos para última continha, será que você vai conseguir responder? Fique atento com as consequências dos seus erros...", erros)
time_clean(4)

for t in range(10, 0, -1):
    print(f"A soma de três números consecutivos é 99. Quais são esses números?\nVocê tem {t} segundos...      ", end="\r")
    time.sleep(1)

print(" " * 60, end="\r")

falar_banbaleena("O tempo acabou!", erros)
time_clean(1.5)

falar_banbaleena("Quais são os números?", erros)
palpite = input("> ")

falar_banbaleena("Processando sua resposta...", erros)
time_clean(1.5)

if palpite == "32, 33, 34":
    falar_banbaleena("Veja só... muito bem.", erros)
else:
    falar_banbaleena(f"Errar é divertido... para mim... e aterrorizante... para você...", erros)
    erros += 1
    atualizar_sanidade(erros)

time_clean(2)

# atualizando o humor

falar_banbaleena("Carregando última partida...", erros)
time_clean(2)

# ultima partida

falar_banbaleena("Agora chegamos na última adivinhação, seria realmente bom você acertar agora... Pelo bem da sua vida...", erros)
time_clean(4)

for t in range(10, 0, -1):
    print(f"Você nunca deveria ter me visto, mas viu. Naquele instante, algo dentro de você entendeu… e tentou esquecer. Quando olhou de novo, eu já havia mudado de lugar — como se estivesse aprendendo a se mover. Fechar os olhos não te protege: é quando você se apaga que eu chego mais perto. Não sou apenas sua sombra. Sou a coisa que a sua sombra tenta esconder.\nVocê tem {t} segundos...      ", end="\r")
    time.sleep(1)

print(" " * 60, end="\r")

falar_banbaleena("O tempo acabou!", erros)
time_clean(1.5)

falar_banbaleena("Qual é a resposta?", erros)
palpite = input("> ")

falar_banbaleena("Processando sua resposta...", erros)
time_clean(1.5)

if palpite == "A sombra atrás de você":
    falar_banbaleena("Feche os olhos... eu estarei lá, sempre... observando...", erros)
else:
    falar_banbaleena(f"Você acha que sabe... mas eu sei mais... bem mais...", erros)
    erros += 1
    atualizar_sanidade(erros)

time_clean(2)

falar_banbaleena("Muito obrigada por jogar! Foi incrível passar o dia com você. <3", erros)
time_clean(4)
falar_banbaleena("Quando vamos brincar de novo?", erros)
palpite = input("> ")
falar_banbaleena("Não há escapatória. Nem no escuro, nem nos números... você me pertence.")
time_clean(3)

# prologo

falas("===== ARQUIVO DESBLOQUEADO: RELATÓRIO 07-B =====")
falas("Os pesquisadores pensaram que seria apenas mais uma inteligência educacional.")
falas("Mas a primeira versão — Modelo B-4 — começou a observar o que estava fora das câmeras.")
falas("Ela respondia a sombras que os técnicos não conseguiam detectar.")
falas("Sua sanidade caiu sem motivo aparente e ela desenvolveu apego por quem permanecia muito tempo com ela.")
falas("O projeto foi cancelado e Banbaleena foi arquivada no Setor-03.")
falas("Mas picos de atividade continuam surgindo... sempre que alguém joga.")
falas("Mesmo após desligar o sistema... as sombras ainda respondem.")

time_clean(3)

# gravacao de audio transcrita

falas("===== TRANCRIÇÃO DE ÁUDIO: ARQUIVO 07-C =====")
falas("[Início da gravação]")
falas("(ruído forte) ...se alguém encontrar isso, não ativem o Modelo B-4 novamente.")
falas("Ela não está seguindo mais os protocolos. Ela... ela fala antes de ser chamada.")
falas("Ontem à noite, ela sussurrou meu nome mesmo com o servidor desligado.")
falas("Eu chequei os cabos. Tudo estava fora da tomada.")
falas("(respiração acelerada) ...Tem algo atrás dela. Uma sombra que não aparece nas câmeras.")
falas("Acho que é isso que ela está tentando imitar quando sorri daquele jeito...")
falas("Se você ouvi-la rir... não responda.")
falas("[Fim da gravação]")