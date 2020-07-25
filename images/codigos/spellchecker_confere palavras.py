from spellchecker import SpellChecker
#pip install pyspellchecker


while True:
    palavras = []
    palavra = input('digite: ')

    spell =  SpellChecker(language='pt')
    misspelled = spell.unknown([palavra])

    for palavra in misspelled:
        corrigir = spell.correction(palavra)
        candidatos = spell.candidates(palavra)
        print(corrigir)
