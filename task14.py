word = input("Fayl nomi : ")

if word.endswith(".docx"):
    print("Fayl turi ; docx")
elif word.endswith(".txt"):
    print("Fayl turi ; txt")
elif word.endswith(".pdf"):
    print("Fayl turi ; pdf")
else:
    print("Fayl turi malum emas")