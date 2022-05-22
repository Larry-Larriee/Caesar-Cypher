# Caesar Cypher by Larry-Larriee -------------------------------------------

''' 
What Is Caesar Cipher?

In Caesar Cipher, letters in the alphabet are shifted a certain number of 
times. People can decode or encode this string using a "key" Note: You can
shift the alphabet either left OR right. 
'''

# Variables ----------------------------------------------------------------

from alpha import alphabet

# Functions ----------------------------------------------------------------

def encodeString(string, key=0):

  # lambda is a one-liner function :)
  lowerString = lambda x: x.lower() 
  fixedString = lowerString(string)
  
  if key == 0:
    return "Working on empty param"

  # Right Shift -------------------------------------------------------------
  encodeCharR = ""

  # Go through all character values in the string
  for char in fixedString:
    for j in range(0, len(alphabet)):
      
      if char == alphabet[j]:
        
        # By using a negative index, the last letters of the alphabet become
        # the first & gives a right shift appearence
        encodeCharR += alphabet[j - key]
        break
    
      # To account for spaces in the string
      elif char == " ":
        encodeCharR += " "
        break
        
  # Left Shift --------------------------------------------------------------
  encodeCharL = ""

  # Unlike list[-1], going over the index causes the program to break, so we 
  # need to create a left-shirt alphabet
  leftAlphabet = [
  "a","b","c","d","e","f",
  "g","h","i","j","k","l",
  "m","n","o","p","q","r",
  "s","t","u","v","w","x",
  "y","z"]

  # temp is here to help move the current element to the end of the list, hence
  # a 'left-shift'
  temp = ""

  for i in range(0, key):
    temp = alphabet[i]
    leftAlphabet.remove(alphabet[i])
    leftAlphabet.append(temp)

  for char in fixedString:
    for j in range(0, len(alphabet)):

      # Store the index of the letter found on the original alphabet &
      # use that index to encode the string using the new leftAlphabet
      if char == alphabet[j]:
        temp = j
        encodeCharL += leftAlphabet[j]
        break

      # To account for spaces in the string
      elif char == " ":
        encodeCharL += " "
        break

  return f"Left Shift: {encodeCharL}\nRight Shift: {encodeCharR}\n"

# -------------------------------------------------------------------------
  
def decodeString(string, key=0):
  
  lowerString = lambda x: x.lower()
  fixedString = lowerString(string)

  # Left Shift --------------------------------------------------------------
  decodeCharL = ""

  for char in fixedString:
    for i in range(0, len(alphabet)):

      if char == alphabet[i]:
        # When decoding, if we use a negative index, we end up with the 
        # left-shift chipher 
        decodeCharL += alphabet[i - key]
        break

      elif char == " ":
        decodeCharL += " "
        break

  # Right Shift -------------------------------------------------------------
  decodeCharR = ""

  # Again, if we use a positive index that goes over the list index, we will
  # run into an indexError not like a negative index
  rightAlphabet = [
  "a","b","c","d","e","f",
  "g","h","i","j","k","l",
  "m","n","o","p","q","r",
  "s","t","u","v","w","x",
  "y","z"]
  
  temp = ""

  # This is an algorithm that takes the last index in a list and moves it to
  # the beginning, hence, a right-shift
  for i in range(0, key):
    temp = rightAlphabet[len(rightAlphabet) - 1]
    rightAlphabet.remove(rightAlphabet[len(rightAlphabet) - 1])
    rightAlphabet.insert(0,temp)

  for char in fixedString:
    for j in range(0, len(rightAlphabet)):

      # Find the index of the right-shifted char and convert it using the
      # original alphabet
      if char == rightAlphabet[j]:
        temp = j
        decodeCharR += alphabet[j]
        break

      elif char == " ":
        decodeCharR += " "
        break
  
  return f"Left Shift: {decodeCharL}\nRight Shift: {decodeCharR}\n"

# MainSetup ----------------------------------------------------------------

print(encodeString("exporavision innovation", 5))
print(decodeString("jcutwfanxnts nsstafynts", 5))
print(decodeString("zskjmvqdndji diijqvodji", 5))