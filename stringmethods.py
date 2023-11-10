sentence = "this is a sentence"
print(sentence.upper())

sentence = "this is a sentence"
sentence = sentence.upper()
print(sentence)

sentence = "this IS a sentence"
print(sentence.lower())

sentence = "this is a sentence"
print(sentence.capitalize())

sentence = "this IS a 99484 sentence"
print(sentence.isdigit())

sentence = "99484"
print(sentence.isdigit())

sentence = "99484 7343983"
print(sentence.isdigit())

sentence = "A 99484 7343983"
print(sentence.isalnum())

sentence = "A994847343983"
print(sentence.isalnum())

sentence = "A 99484 7343983"
print(sentence.startswith("A948"))

sentence = "A 99484 7343983"
print(sentence.startswith("A 9948"))

sentence = "A 99484 7343983"
print(sentence.startswith("A948"))

sentence = "A 99484 7343983"
print(sentence.endswith("3983"))

sentence = "A 99484 7343983"
print(sentence.startswith("84 734", 5))