from load_fruits_list import get_fruits_list


guess = input("What fruit name do you know? ")
guess = guess.lower()

# fruits_list = [
#     "apple", "banana", "pineapple", "grape", "coconut", 
#     "cherry", "watermelon", "palm", "mango"
# ]
fruits_list = get_fruits_list()

if guess in fruits_list:
    print("You're correct")
else:
    print(f"{guess.title()} is not known as a fruit.")
