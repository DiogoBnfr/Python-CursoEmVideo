# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”
# Primeira forma:
n = str(input('Qual o nome da sua cidade?')).strip()
print('Sua cidade começa com "Santo"? {}'.format("Santo" in n.title()))

# Segunda forma:
cid = str(input('Qual o nome da sua cidade?')).strip()
print(cid[:5].title() == "Santo")
