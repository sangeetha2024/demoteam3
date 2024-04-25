Tamil=int(input("Tamil :"))
English=int(input("English :"))
Maths=int(input("Maths :"))
Science=int(input("Science :"))
Social=int(input("Social :"))
Tot=Tamil+English+Maths+Science+Social
print(Tot)
if (Tot<100):
    print("Aditional class is required")
else:
    print("You are good")