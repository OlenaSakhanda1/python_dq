#Importing library
import re

def normalizing_letter_cases_in_text(text):
    sentences = text.split(". ")
    for i in range(len(sentences)):
        sentences[i] = sentences[i].capitalize()
    sentences = ". ".join(sentences)

    sentences = sentences.split("\t")
    for i in range(len(sentences)):
        sentences[i] = sentences[i][0].upper() + sentences[i][1::]
    result_text = "\t".join(sentences)
    return result_text

def sentence_with_last_words(result_text):
    last_words = []
    sentences = result_text.split(".")
    for i in range(len(sentences)):
        last_space_index = sentences[i].rfind(' ')
        last_words.append(sentences[i][last_space_index + 1::])
    last_words_sentence = " ".join(last_words)
    last_words_sentence = last_words_sentence.strip()
    last_words_sentence = last_words_sentence.capitalize() + '.'
    return last_words_sentence

text = '''homEwork:
	tHis iz your homeWork, copy these Text to variable.

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

if __name__ == '__main__':
    whitespace_count = text.count(" ") + text.count("\t") + text.count("\n")
    result_text = normalizing_letter_cases_in_text(text)
    last_words_sentence = sentence_with_last_words(result_text)
    new_text = result_text + '\n' + last_words_sentence
    corrected_text = result_text.replace(" iz ", " is ")

    print(corrected_text)
    print("Number of whitespace characters:", whitespace_count)


