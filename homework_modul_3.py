#Importing library
import re
#Place text in variable
text = '''homEwork:
	tHis iz your homeWork, copy these Text to variable.

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''
#Count all kinds of spaces
whitespace_count = text.count(" ") + text.count("\t") + text.count("\n")   # Add other types of whitespace as needed

# Divide text to sentences with ". "
sentences = text.split(". ")
# Loop from 0 to end of list
for i in range(len(sentences)):
    # Capitalizes the first letter of each sentence using the capitalize() method.
    sentences[i] = sentences[i].capitalize()
# Join sentences
sentences = ". ".join(sentences)
# Divide text to sentences with "\t"
sentences = sentences.split("\t")
# Loop from 0 to end of list
for i in range(len(sentences)):
    # Capitalizes the first letter of each sentence using the upper() method.
    sentences[i] = sentences[i][0].upper() + sentences[i][1::]
# Join sentences
result_text = "\t".join(sentences)
#Initialize empty list
last_words = []
# Divide text to sentences with "."
sentences = result_text.split(".")
# Loop from 0 to end of list
for i in range(len(sentences)):
    #Find index of the last space in the sentence
    last_space_index = sentences[i].rfind(' ')
    #Add last word to list
    last_words.append(sentences[i][last_space_index + 1::])
# Join words in string
last_words_sentence = " ".join(last_words)
#Delete not necessary spaces
last_words_sentence = last_words_sentence.strip()
#Add dot to new sentence
last_words_sentence = last_words_sentence.capitalize() + '.'
#Add new sentence in the end of paragraph
result_text = result_text + '\n' + last_words_sentence
#Fix “iZ” with correct “is”
result_text = result_text.replace(" iz ", " is ")
#Print result
print(result_text)
#Print number of whitespace
print("Number of whitespace characters:", whitespace_count)


