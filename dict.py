dict={
    "fan":"pankha",
    "water":"pani",
    "watch":"ghadi"
}
print('Options are',dict.keys())
a=input("Enter the word : ")
print("The meaning of the given word is",dict.get(a))