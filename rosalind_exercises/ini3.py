# Problem INI3 - Strings and Lists 

# Description: 
# Given: A string s of length at most 200 letters and four integers a, b, c and d. 
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

# Code answer:
s = "SSfd7fIngerophrynusFKmvK6eIrFbxHj0Kbe3dWBoDX6lSLMQiD4eDjwCriF1yTWnZcyLQh96v393ro7oExL5EFtyxofo3TxkpTAF4imLRJwQhWkDkJZBOvNmLtnD6Jv3mmSmwUahrS8g9yx25tRGjXEKt1mSBcuEwBaeopiQ7Olb2bRferinaBhVOKUl4qlQLYYx."
a=6
b=18
c=177
d=182

word1= s[a:b+1]
word2= s[c:d+1]
print (word1, word2)

# Answer: Ingerophrynus ferina