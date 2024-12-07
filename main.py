import random as r
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD" : "se usa cuando se quiere referir de forma sarcastica a algo",
            "AFK" : "Significa away from keyboard,y se utiliza cuando alguien ya no esta presente",
            "GG": "",
            "SIMP" :"Una persona SIMPatica, es la que e da un mejor trato con el genero femenino dandole y uno peor al masculino esta persona siendo hombre"
            }


print (meme_dict.keys())
word = input("Escribe una palabra que no entiendas o escribe sorprendeme: ").upper()

if word in meme_dict.keys():
    print("el significado es:", meme_dict[word])
elif word == "SORPRENDEME":
    wodr = r.choice (list(meme_dict.keys()))
    print("La palabra es:",wordr, "y su significado es:",word)
else:
    print("Esta palabra aun no se ha agregado al diccionario")
