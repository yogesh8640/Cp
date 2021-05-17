def rev(n):
  count = 0
  while True:
    k = str(n)
    if k == k[::-1]:
      break
    else:
      m = int(k[::-1])
      n += m
      count += 1
  print("iterations=",+count)
  return n

print(rev(264))
print(rev(265))

