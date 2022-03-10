import random as r
wordlist = []
special_char = ['!', '@', '#', '$', '%', '&']
with open('wikipedia.txt', 'r') as file: 
    data = file.readlines()
    
    #create a for loop to convert a paragraph into a list of strings for each line 
    #example: ['this', 'is', 'one', 'line']
    for line in data:
        words = line.split()

        #check the length of words then print the word list 
        for item in words: 
            if len(item) > 5: 
                wordlist.append(item.capitalize())

word = r.choice(wordlist)
schar = r.choice(special_char)
num = str(r.randint(10,99))

password = word + schar + num 
print(password)
