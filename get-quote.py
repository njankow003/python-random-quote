import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last=16
  rnd1=random.randint(0,last)
  rnd2=random.randint(0,last)
  print(quotes[rnd1]+'\n'+quotes[rnd2])

if __name__== "__main__":
  primary()
