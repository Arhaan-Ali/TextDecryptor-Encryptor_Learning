import random
import  string
chars = " " +  string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
random.seed(42)
key = chars.copy()
random.shuffle(key)
response = input("Do you want to encrypt text or decrypt it or exit from the program ? : ").upper()
while response !="EXIT" :
  if response == "ENCRYPT":
    plain_text = input("Please input text to encrypt : ")
    cyphered_text = ""
    for letters in plain_text:
      index = chars.index(letters)
      cyphered_text += key[index]
    print(f"Encrypted Message : {cyphered_text}")
  elif response.upper() == "DECRYPT":
    cyphered_text = input("Please input text to decrypt : ")
    plain_text = ""
    for letters in cyphered_text:
      index = key.index(letters)
      plain_text += chars[index]
    print(f"Decrypted Message : {plain_text}")
  else:
    print("please choose a correct option.")
  response = input("Do you want to encrypt text or decrypt it or exit from the program ? : ").upper()
print("Program Exited")

