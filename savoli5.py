my_list=["Salom aleykum", "millioner", "welcom","telefon"]
with open("fille.txt","w") as file:
    for i in my_list:
        file.write(i +"\n")
    print("operation successfully")