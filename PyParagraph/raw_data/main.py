#import the library
import os

#create the pass to the file with text
os.chdir(os.path.dirname(os.path.abspath(__file__)))
paragraph = os.path.join('paragraph_1.txt')

#open text file for reading
txt=open(paragraph,'r')

if txt.mode=='r':
    
    #read text file into paragraph and create a list with the words
    paragraph=txt.read()
    words=paragraph.split(' ')
    
    #find the number of words in paragraph
    word_count=len(words)

    #initialise variables for counting of sentences and total length of the words
    sentence_count=0
    total_word_length=0

    #find total length of the words
    for word in words:

        word_length=len(word)
        total_word_length=total_word_length+word_length
        
        #find number of sentences
        for letters in word:
            if letters==".":
                sentence_count=sentence_count+1
    
    #find average number of letters in the words and average number of words in a sentence
    average_letters_count=format((total_word_length/word_count), ".1f")
    average_sentence_length=format((word_count/sentence_count), ".1f")

    #print results on the screan
    print("Paragraph Analysis")
    print("-------------------------------------------------")
    print(f"Approximate words count: {word_count}")
    print(f"Approximate sentence count: {sentence_count}")
    print(f"Average letters count: {average_letters_count}")
    print(f"Average sentence length: {average_sentence_length}")
    print("----------------------------------------------------")


    