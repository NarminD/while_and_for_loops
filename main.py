#while loops

counter = 0                                                      
print("Let's use a while loop to count from 0 to 10!")

while counter <= 10:                                               
  print('Say ', counter)                         
  counter += 1                                                    

print("We stopped counting as we reached the number", counter)


#for loops 
print("Now let's use a for loop to improve our vocabulary!")
adj = ["red", "memorable", "beautiful"]
fruits = ["flower", "dress", "notebook"]

for x in adj:
  for y in fruits:
    print(x, y)

print("That's all for now. Great work!")