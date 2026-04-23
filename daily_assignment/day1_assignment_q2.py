# Q-2. Count how many times "a" appears in a string using enumerate.
string = "coca-cola"
count=0
for idx,char in enumerate(string):
    if char=='a':
        count+=1
print(count)