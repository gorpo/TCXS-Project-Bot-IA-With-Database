
from spellchecker import SpellChecker


mensagem = 'voce esta em cacsa'

spell = SpellChecker(language='pt')
misspelled = spell.unknown(mensagem.split())  #msg['reply_to_message']['text'].split()
palavra_errada = list(misspelled)[0]  #retorna a palavra que estava errada na frase
todas_palavras = []
separador = ' \n'

for palavra_final in misspelled:
    corrigir = spell.correction(palavra_final)
    candidatos = spell.candidates(palavra_final)
    todas_palavras.append(corrigir)
    mensagem_corrigida = mensagem.replace(palavra_errada,corrigir) #nova frase com replace na palavra errada pela mais provavel.
    print(mensagem_corrigida)
    for candidato in list(candidatos):  #outras alternativas de correção
        alternativas_corrigidas = mensagem.replace(palavra_errada,candidato) #novas frases com replace na palavra errada pelas outras mais provaveis
        print(alternativas_corrigidas)









