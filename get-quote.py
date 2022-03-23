import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last=15
  rnd1=random.randint(0,last)
  rnd2=random.randint(0,last)
  quote1=quotes[rnd1]
  quote2=quotes[rnd2]
  print(quote1.strip()+'\n'+quote2.strip())

if __name__== "__main__":
  primary()
