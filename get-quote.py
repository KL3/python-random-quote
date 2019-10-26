import random

def primary():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
   
  last = len(quotes) - 1 
  rnd = random.randint(0, last)  
  print(quotes[rnd],end='', flush=True)
  
  #not the best implementation as it's repetitive but okay for start
  last2 = len(quotes) - 1 
  rnd2 = random.randint(0, last2) 
  print(quotes[rnd2],end='', flush=True)
  
  #writing to file
  file = open("quotes.txt", "a+")
  text = input("user input: ")
  file.write("\n" +text)
  file.close()
  

if __name__== "__main__":
  primary()
