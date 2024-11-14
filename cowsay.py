import sys
from heifer_generator import HeiferGenerator as hg

def list_cows(cows):
  cow_list = []
  for cow in cows:
    cow_list.append(cow.name)
  return cow_list
def find_cow(name, cows):
    for cow in cows:
      if cow.name == name:
        return cow
    return None

if __name__ == "__main__":
  cows = hg.get_cows()
  separator = " "
  if sys.argv[1] == "-l":
    print("Cows available: "+ separator.join(list_cows(cows)))
  elif sys.argv[1] == "-n":
    if sys.argv[2] in hg.cow_names or sys.argv[2] in hg.dragon_names:
      summoned = find_cow(sys.argv[2], cows)
      message = separator.join(sys.argv[3:])
      print(message)
      print(summoned.image)
      if summoned.name == "dragon":
        print("This dragon can breathe fire.")
      elif summoned.name == "ice-dragon":
        print("This dragon cannot breathe fire.")
    else:
      print(f"Could not find {sys.argv[2]} cow!")
  else:
    message = separator.join(sys.argv[1:])
    print(message)
    print(hg.cows[0].image)
    

