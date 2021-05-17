NCARDS = 52 #Number of cards
NSUITS = 4   #Number of suits
val = "23456789TJQKA"
suits = "cdhs"
MAX = 500
def value(n):
  return val.index(val[n//NSUITS])

def war(deck1, deck2):
  inwar = False         
  war_queue = list()   
  steps = 0             
  
  while len(deck1) != 0 and len(deck2) != 0 and steps <= MAX:
    steps += 1
    x = deck1.pop()
    y = deck2.pop()
    war_queue.extend([x, y])
    
    if inwar:
      inwar = False
    else:
      if value(x) > value(y):
        deck1.extend(war_queue)
        war_queue.clear()
      elif value(x) < value(y):
        deck2.extend(war_queue)
        war_queue.clear()
      else:
        inwar = True
  

  if len(deck1) != 0 and len(deck2) == 0:
    print("deck1 wins in", steps, "steps")
  elif len(deck1) == 0 and len(deck2) != 0:
    print("deck2 wins in", steps, "steps")
  else:
    print("Game tied after", steps)
  
        
def rank_card(value, suit):
  try:
    i = val.index(value) 
    j = suits.index(suit) 
    return i*NSUITS + j
    
  except ValueError:
    print("\nBad input\n value : {value}\n suit : {suit}")
    return


print("Enter how many times you want to run: ")
T = int(input())
  
while T != 0:
    T -= 1
    

    decks = [[], []]
    
    for i in range(0, len(decks)):
      print("Deck", i+1, end=' ')
      temp_deck = input().strip().split()
      

      for card in temp_deck:
        rank = rank_card(card[0], card[1])
        if rank != None:
          decks[i].append(rank)
        else:
          print("Re-enter val of deck", i+1)
          i -= 1
          break

    war(decks[0], decks[1])
