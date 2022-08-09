import random

# @_devsmi_
sentences = "selamün aleyküm.".split(".")

print(("-" * 30) + "\n sahte alıntı oluşturucu \n" + ("-" * 30))

n = int(input("cümle sayısı"))
quote = []

for i in range(n):
    quote.append(random.choice(sentences))
    print("alıntı: : {}.".format(".".join(quote)))
