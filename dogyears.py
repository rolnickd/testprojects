

while True:
  dog_age = 0
  years_old = input("How many years old is your dog?\n")
  
  try:
    years_old_int = int(years_old)

    while years_old_int > 0:
          
      if years_old_int == 1:
        dog_age += 15
        years_old_int -= 1
      
      elif years_old_int == 2:
        dog_age += 9
        years_old_int -= 1
      
      else:
        dog_age += 5
        years_old_int -= 1

    print(f"Your dog is {dog_age} years old in dog years!\n")
    again = input("Do you want to calculate again? Y or N ")
    if again.lower() == "n":
      break
    else:
      continue
    
  except:
    print("Please input an integer\n")

exit = input("Press enter to exit")