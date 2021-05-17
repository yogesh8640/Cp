#python 3.7.1
 
# To check whether number is jolly or not

print("Press Enter to exit")
print("Enter total number of values and values to check")
while True:
  try:
    n, *numbers = map(int, input().split())
  except ValueError:
    break
  
  abs_diff = list() 
  
  for i in range(n-1):
    abs_diff.append(abs(numbers[i] - numbers[i+1]))
    
  abs_diff.sort()
  
  for i in range(len(abs_diff)):
    if i+1 == abs_diff[i]:
      flag = True
    else:
      flag = False
      print("Not Jolly")
      break
      
  if flag:
    print("Jolly")