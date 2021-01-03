def encrypt(text,s):
  result=""
  for i in range(len(text)):
    char=text[i]
    if(char.isupper()):
      result += chr((ord(char)+ s - 65) % 26 + 65)
    else:
      result += chr((ord(char) + s - 97) % 26 + 97)
  return result

def decrypt(text,s):
  result=""
  for i in range(len(text)):
    char=text[i]
    if(char.isupper()):
      result += chr((ord(char)- s - 65) % 26 + 65)
    else:
      result += chr((ord(char) - s - 97) % 26 + 97)
  return result

text=input("Enter the  text ")
shift=int(input("Enter the shift No "))
print("ENCRYPTION..............")
print("Plain text: "+ text)
print("Shift no :"+ str(shift))
cipher=encrypt(text,shift)
print("Cipher Text: "+ cipher )
print("DECRYPTION.........")
print("Cipher Text : "+ cipher)
print("Original Text : "+ decrypt(cipher,shift))

#hello
