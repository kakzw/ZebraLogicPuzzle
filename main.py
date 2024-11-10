import itertools

numOfBoys = 4

# Define possible values for each attribute
shirts = ["Black", "Blue", "Green", "Red"]
names = ["Daniel", "Joshua", "Nicholas", "Ryan"]
movies = ["Action", "Comedy", "Horror", "Thriller"]
snacks = ["Chips", "Cookies", "Crackers", "Popcorn"]
ages = [11, 12, 13, 14]

# Generate all permutations for each attribute
possibleCombinations = list(itertools.permutations(range(numOfBoys)))

# Function to check if a given arrangement satisfies all the clues
def is_valid_solution(namePos, agePos, shirtPos, moviePos, snackPos):
  # Joshua is at one of the ends
  if names.index("Joshua") not in (namePos[0], namePos[-1]):
    return False
  
  # The boy in the black shirt is somewhere to the left of the youngest boy
  blackIndex = shirtPos.index(shirts.index("Black"))
  youngestIndex = agePos.index(ages.index(min(ages)))
  if blackIndex >= youngestIndex:
    return False
    
  # Joshua likes horror movies
  joshuaIndex = namePos.index(names.index("Joshua"))
  if moviePos[joshuaIndex] != movies.index("Horror"):
    return False
    
  # 14-year-old boy is at the third position
  if agePos[2] != ages.index(14):
    return False
  
  # boy in the Red shirt is somewhere between the 13-year-old and action movie, in that order
  redIndex = shirtPos.index(shirts.index("Red"))
  index13 = agePos.index(ages.index(13))
  actionIndex = moviePos.index(movies.index("Action"))
  if not (index13 < redIndex < actionIndex):
    return False
  
  # Daniel likes thriller movies
  danielIndex = namePos.index(names.index("Daniel"))
  if moviePos[danielIndex] != movies.index("Thriller"):
    return False
    
  # boy who eats cookies is at one of the ends
  if snacks.index("Cookies") not in (snackPos[0], snackPos[-1]):
    return False
  
  # boy in the black shirt is left of thrillier movie
  blackIndex = shirtPos.index(shirts.index("Black"))
  thrillerIndex = moviePos.index(movies.index("Thriller"))
  if blackIndex + 1 != thrillerIndex:
    return False
    
  # boy who eat crackers is right of comedy
  comedyIndex = moviePos.index(movies.index("Comedy"))
  crackersIndex = snackPos.index(snacks.index("Crackers"))
  if comedyIndex + 1 != crackersIndex:
    return False

  # boy in the Red shirt is somewhere between the popcorn and Nicholas, in that order
  redIndex = shirtPos.index(shirts.index("Red"))
  popcornIndex = snackPos.index(snacks.index("Popcorn"))
  nicholasIndex = namePos.index(names.index("Nicholas"))
  if not (popcornIndex < redIndex < nicholasIndex):
    return False
    
  # boy who likes thriller movies is at one of the ends
  if movies.index("Thriller") not in (moviePos[0], moviePos[-1]):
    return False
  
  # Nicholas is somewhere between Joshua and Daniel, in that order
  joshuaIndex = namePos.index(names.index("Joshua"))
  nicholasIndex = namePos.index(names.index("Nicholas"))
  danielIndex = namePos.index(names.index("Daniel"))
  if not (joshuaIndex < nicholasIndex < danielIndex):
    return False
  
  # boy in the first position wears a green shirt
  if shirtPos[0] != shirts.index("Green"):
    return False
  
  # if all clues are satisfied, return true
  return True

# Check each possible arrangement to find the first valid solution
for shirtPos in possibleCombinations:
  for namePos in possibleCombinations:
    for moviePos in possibleCombinations:
      for snackPos in possibleCombinations:
        for agePos in possibleCombinations:
          if is_valid_solution(namePos, agePos, shirtPos, moviePos, snackPos):
            # Print the solution
            print("Solution:")
            for i in range(numOfBoys):
              print(f"Boy {i + 1}: Shirt={shirts[shirtPos[i]]}, Name={names[namePos[i]]}, Movie={movies[moviePos[i]]}, Snack={snacks[snackPos[i]]}, Age={ages[agePos[i]]}")
            exit()