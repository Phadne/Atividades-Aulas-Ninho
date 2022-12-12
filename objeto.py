class Pokemon:
    def __init__(self,name,hp,atack,speed,category,type):
        self.name= name
        self.hp= hp
        self.atack= atack
        self.speed= speed
        self.category= category
        self.type= type

def imprimir(self):
print(f"""My pokemon:
"Name": {self.name}
"HP": {self.hp}
"Atack":{self.atack}
"Speed":{self.speed}
"Category":{self.category}
"Type":{self.type} \n""")       

def batalhar (p1,p2):

    p1local= Pokemon()       

pokemon1 = Pokemon("Jigglypuff","30", "20", "Ballon", "Fairy")

# print(f"""My pokemon:
# "Name": {pokemon1.name}
# "HP": {pokemon1.hp}
# "Atack":{pokemon1.atack}
# "Speed":{pokemon1.speed}
# "Category":{pokemon1.category}
# "Type":{pokemon1.type} \n""")


pokemon2 = Pokemon("Psyduck", "40","40", "Duck","Water")




print(pokemon1.name)
print(pokemon2.name)
if pokemon1.atack > pokemon2.atack:
    pokemon1 = print()
