# This Python script takes user input as a string and modifies the string for a slow speed subtitle.
# It adds "..." after each word except the last one.

# Start of the loop

while True:

  # user input
  str1 = input("\nEnter the subtitle of a lecture: ")
  

  # check if user want to exist the program .
  if ( str1 != 'q'):
    
    # Split the string into words and Iterate over each word in the string
    for i in range(len(str1.split())):

      string_len = len(str1.split())

      # If the word is not the last one, add "..." after it
      if ( i != ( string_len -1 )) :

        slow_speed_subtitle = (str1.split()[i] + "...")
        print(slow_speed_subtitle , end = "" )

      # If the word is the last one, print it as is
      else :
        print(str1.split()[i], end = "")

  # this is for If user wants to quit.
  else :
    print("Program end 😁😁")
    break
