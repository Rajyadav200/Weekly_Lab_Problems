
# This python script takes input temperature in celsies and convert Farenheit
# Initialize while loop

while True:

  # Taking User input 
  temperature_in_celsies = input("enter the temperature: ")

  if (temperature_in_celsies != 'q'):
    # Here is the calculating temperature in Farenheit 


    temperature_in_farenheit = (((9/5)*int(temperature_in_celsies.split()[0])) + 32 )

    print("Celsius: ", temperature_in_celsies)

    print("-"*20)

    print("Farenheit:", temperature_in_farenheit)
  else :
    print("Program end")
    break
