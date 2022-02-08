#Kata 4 Ejercicio 1
text = """Interesting facts about the Moon. The Moon is Earth's 
only satellite. There are several interesting facts about the Moon 
and how it affects life here on Earth. On average, the Moon moves 
4cm away from the Earth every year. This yearly drift is not 
significant enough to cause immediate effects on Earth. The 
highest daylight temperature of the Moon is 127 C."""

text_partes=text.split('.')
print(text_partes)

#Kata 4 Ejercicio 1
pista = ["average", "temperature", "distance"]

# Ciclo for para recorrer la cadena
for sentence in text_partes:
    for pista in pista:
        if pista in sentence:
            print(sentence)
            break

# Ciclo for para recorrer la cadena
for sentence in text_partes:
    for pista in pista:
        if pista in sentence:
            print(sentence)
            break