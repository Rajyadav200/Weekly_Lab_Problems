# This python script takes input radius of circle and computes its Area
# Initialize while loop

while True:

  # Taking User input 
  radius = input("Enter the raduis of a circle: ")

  # Assining constant value
  pi = 3.14159

  if ( radius != 'q'):
    # This formule to compute area of circle
    
    Area_of_circle = ( pi*(float(radius.split()[0]))**2)

    print("Radius:", radius)
    print("Area:" , Area_of_circle,"square units")

  else :
    print("Program End ")
    break

