num_apples = 10
num_banana = 5
print("We have " + str(num_apples) + " apples")

# use format()
print("We have {1} apples and {0} banana".format(num_apples, num_banana))
print("We have {apples} apples and {bananas} banana".format(
  apples=num_apples, 
  bananas=num_banana
  ))

# f-strings
print(f"We have {num_apples} apples and {num_banana} banana")

n = 10 / 3
print(n)
print("Number is: {:10.2f}".format(n))
print("Number is: {:5.2f}".format(n))
print("Number is: {:.4f}".format(n))