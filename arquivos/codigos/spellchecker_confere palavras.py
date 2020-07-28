from spellchecker import SpellChecker
#pip install pyspellchecker


while True:
    palavra = input('digite:')

    spell =  SpellChecker(language='pt')
    misspelled = spell.unknown(palavra.split())
    for palavra_final in misspelled:
        corrigir = spell.correction(palavra_final)
        candidatos = spell.candidates(palavra_final)
        correcao = f"você escreveu {corrigir} errado?"
        print(correcao)
