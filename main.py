# Caesar Cypher by Larry-Larriee -------------------------------------------

''' 
What Is Caesar Cipher?

In Caesar Cipher, letters in the alphabet are shifted a certain number of 
times. People can decode or encode this string using a "key" Note: You can
shift the alphabet either left OR right. 
'''

# Variables ----------------------------------------------------------------

from larryTools import alphabet
from larryTools import help_me
from larryTools import specialChar
import os 
import asyncio
from discord.ext import commands

TOKEN = os.environ["TOKEN"]
bot = commands.Bot(command_prefix=["caesar ", "Caesar "])

# Functions ----------------------------------------------------------------

# Discord.py automatically adds a help function & this is to remove it
bot.remove_command("help")

# New implemented help command
@bot.command(name = "help")
async def help(ctx):
  await ctx.author.send(help_me)
  await ctx.send(f"""Hello <@{ctx.author.id}>! Please check your DMs for more info :D""")

@bot.command(aliases = ["encode", "Encode"])
async def encode_string(ctx, *string, key=0):

  # Use given input and interpret it so algorithm can digest
  # key should be the last element in the list. 
  try:
    key = int(string[-1])
  except ValueError:
    await ctx.reply("Invalid Key :(")
    return
    
  # string to encode (discord.py automatically puts in tuple)
  string = [i for i in string]
  string.remove(str(key))
  string = " ".join(string)

  # lambda is a one-liner function :)
  lowerString = lambda x: x.lower() 
  fixedString = lowerString(string)

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
    
      # To account for spaces and special characters in the string
      elif char in specialChar:
        encodeCharR += char
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

      # To account for spaces and special characters in the string
      elif char in specialChar:
        encodeCharL += char
        break

  await ctx.send(f"**Orginal Text (For Encode):** {string}\n")
  await asyncio.sleep(1)
  await ctx.send(f"**Left Shift:** {encodeCharL}\n**Right Shift:** {encodeCharR}")

@bot.command(aliases = ["Decode", "decode"])
async def decodeString(ctx, *string, key=0):

  # Use given input and interpret it so algorithm can digest
  # key should be the last element in the list. 
  try:
    key = int(string[-1])
  except ValueError:
    await ctx.reply("Invalid Key :(")
    return
  
  # string to encode (discord.py automatically puts in tuple)
  string = [i for i in string]
  string.remove(str(key))
  string = " ".join(string)
  
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
      
      # To account for spaces and special characters in the string
      elif char in specialChar:
        decodeCharL += char
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

      # To account for spaces and special characters in the string
      elif char in specialChar:
        decodeCharL += char
        break
  
  await ctx.send(f"**Orginal Text (For Decode):** {string}\n")
  await asyncio.sleep(1)
  await ctx.send(f"**Left Shift:** {decodeCharL}\n**Right Shift:** {decodeCharR}")
  
# MainSetup ----------------------------------------------------------------

#print(encodeString("hello world", 5))
#print(decodeString("mjqqt btwqi", 5))
#print(decodeString("czggj rjmgy", 5))

bot.run(TOKEN)