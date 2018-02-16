# Instructions for excercise
#In this challenge, you get to play the role of chief linguist at a local learning academy. As chief linguist, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.

#Your task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:

#* Import a text file filled with a paragraph of your choosing.

#* Assess the passage for each of the following:

#  * Approximate word count

# * Approximate sentence count

#  * Approximate letter count (per word)

#  * Average sentence length (in words)

#* As an example, this passage:

#> “Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident - a blot of black upon a world of crimson and gold.”

#...would yield these results:

#```
#Paragraph Analysis
#-----------------
#Approximate Word Count: 122
#Approximate Sentence Count: 5
#Average Letter Count: 4.56557377049
#Average Sentence Length: 24.4
#```

#* **Special Hint:** You may find this code snippet helpful when determining sentence length (look into [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) if interested in learning more):

#```python
#import re
#re.split("(?&lt;=[.!?]) +", paragraph)
#

import re # from instuctions 

#filename of the input file
inputFile = "raw_data/paragraph_2.txt"


#variables to work with
wordCount = 0       #word count
sentenceCount = 0   #sentence count
avgLtrCnt = 0       #average letter count
avgSntLen = 0       #average sentence length

# Read the text file
with open(inputFile) as text_data:
     
     # Store the contents as string, format for reading
     text = text_data.read().replace("\n", " ")
   
    
#calculate wordcount by parsing by spaces
wordArray = text.split(" ")
wordCount = len(wordArray)  

#calculate sentence count
sentenceArray = re.split("(?<=[.!?]) +", text)  #would have never found this without the hint
sentenceCount = len(sentenceArray)

#calculate letter count per work
#avgWord = wordArray
#list1 = ['foo', 'bar', 'bob', 'jess', 'google', 'alphabet']
total = 0
for i in wordArray:
    total += len(i)
avgLtrCnt = float(total) / float(len(wordArray))

#calculate average sentence length
total = 0
for i in sentenceArray:
    total += len(i)
avgSntLen = float(total) / float(len(sentenceArray))


print("\nParagraph Analysis")
print("__________________________________________________________")
print("Approximate word count: " + str(wordCount))
print("Approximate sentence count: " + str(sentenceCount))
print("Average letter per word count: " + str(avgLtrCnt))
print("Average words per sentence count: " + str(avgSntLen))