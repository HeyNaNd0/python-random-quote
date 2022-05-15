import random

def logic():
  d = open("quotes.txt","a")
  d.write("Always have bail money.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0,last)
  print(quotes[rnd]+ "\n" + quotes[rnd-1],end="")

if __name__ == "__main__":
  logic()
