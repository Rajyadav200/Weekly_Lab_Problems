# This python script takes mass as input and computes the Energy in Joules
# Initialize while loop 

while True:
  
  # takinking user input

  mass = (input("Enter the value of mass: "))

  # assinging constant value

  speed_of_light = "300000000 meters per second"

# Condition 
  if mass != 'q':
     if int(mass) > 0:

      # Formula to compute Energy with typecasting 

      Energy = int(mass) * int(speed_of_light.split()[0])**2

      # Output printing on console 

      print("Energy:", Energy ,"Joules")
      
# Loop termination candition

  else :
    print("Program end")
    break

