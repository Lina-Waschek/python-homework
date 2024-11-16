s = "We tried list and we tried dicts also we tried Zen"
words = s.split(' ') #split the string into individual words with space as a delimiter
word_count ={} #define an empty dictionary to store the words with word counts

for word in words: #for every word in words
    if word in word_count: #if the word is already in the word_count dictionary
        word_count[word] += 1 #then the counter for this specific word is increased by 1
    else: # if the word is not already in word_count
        word_count[word] = 1 #then the value of the word-count of this specific word is 1 


for word, count in word_count.items(): #for every word (key) and every count (value) in the word_count dictionary
    print(word, count) #print the word and its count