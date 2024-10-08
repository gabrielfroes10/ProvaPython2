def calcular_temperaturas_media(cidades):
    medias = []
    for cidade, temperaturas in cidades:
        media = sum(temperaturas) / len(temperaturas)  
        medias.append((cidade, media))  
    return medias


lista_cidades = [
    ("Cidade A", [20, 22, 21, 19, 23, 20, 21]),
    ("Cidade B", [30, 32, 31, 29, 30, 31, 32]),
    ("Cidade C", [15, 16, 14, 15, 16, 15, 14]),
]

resultado = calcular_temperaturas_media(lista_cidades)
print("Temperaturas médias por cidade:", resultado)
