
# ! Varianta 1 - folosid un 'for loop' clasic si filtrarea numerelor pare printr-un 'if statement':
sum1 = 0
for num in range(2020,3031):
	if num % 2 == 0:
		sum1 += num
print(sum1)

# ! Varianta 2 - folosid un 'for loop' clasic si filtrarea prin 'pas' la functia range 
sum2 = 0
for num in range(2020,3031, 2):
    sum2 += num
print(sum2)

# ! Varianta 3 - folosind 'list comprehension' si filtrare prin if statement
sum3 = sum([num for num in range(2020,3031) if num % 2 == 0])
print(sum3)

# ! Varianta 4 - folosind 'list comprehension' si filtrare prin pas la functia range
sum4 = sum([num for num in range(2020,3031, 2)])
print(sum4)