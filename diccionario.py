None
meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "XD": "carita riendo",
    "FLASHEAR":"imaginarse o esperar algo imposible",
    "GG":"expresión rápida al terminar una partida."
    }

word = input("Escribe una palabra que no entiendas (¡con minusculas!): ").upper()
if word in meme_dict.keys():
    print(word,meme_dict[word])
else:
    print("ni idea buscalo en otro lado")
    # ¿Qué hacer si no se encuentra la palabra?
 
