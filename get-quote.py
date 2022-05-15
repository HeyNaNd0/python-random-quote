import random

def logic():
  print("Keep it logically awesome.")


f = open("quotes.txt")
quotes = f.readlines()
f.close()
last = 13
rnd = random.randint(0,last)
print(quotes[rnd]+"\n"+ quotes[rnd-1])

if __name__ == "__main__":
  logic()
