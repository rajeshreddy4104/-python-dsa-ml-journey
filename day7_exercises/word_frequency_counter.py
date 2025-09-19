text = "where are the fucking chocolates brotther chocolates"
words = text.split()

freq={}

for word in words:
    freq[word]=freq.get(word,0)+1
print(freq)