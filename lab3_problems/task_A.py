# This Python script takes user input as a string and converts that string from upper to lower case and vice versa for only alphanumeric characters.
# Start of the loop


while True :

  # user input 
  str1 = input("\nEnter a string: ")
  
  # Input string
  print(str1)

  # condition check if user wants to quite the program
  if ( str1 != 'q'):

   # Iterate over each character in the string
    for i in range(len(str1)):

      # If the character is upperrcase, convert it to lowercase
      if('A' <= str1[i] <= 'Z'):
        print(chr(ord(str1[i])+32), end = "")

      # If the character is lowercase, convert it to uppercase
      elif('a' <= str1[i] <= 'z'):
        print(chr(ord(str1[i])-32), end = "")

      # If the character is non-alphanumeric, print it as is
      else :
         print(str1[i], end = "")


  # If user wants to quit, end the program 
  else :
    print("Program end 😵😵")
    break
