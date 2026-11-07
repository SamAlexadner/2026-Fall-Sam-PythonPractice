import os  

def main():
    file_name = input("Enter the name of the input file: ")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, file_name)
    # sorry, I can't use text.txt, so I have to import os
    # or use abspath "C:\Users\shend\OneDrive\2026 Fall Smster\CPSC Fall\CPSC-3310 intro object-oriented\Assignment 9\text.txt"
    # but it will comfilt with input function, so I use this from email_menu.py

    with open(file_path,"r") as infile:
        all_text = infile.read()  # read the text to a big string
        words = all_text.split()  # brakd the big string to the word with list
        unique_words = set(words)  # make list to set, and set auto remove duplicates 
        word_count = {}  # use dict to store the data
        for word in unique_words:  # go set find unique word for one time
            count = words.count(word)  # get word count in words list
            word_count[word] = count  # store in dict
        print(f"{'Word':<15} Occurrences")
        print('-' * 50)
        for key, value in word_count.items():
            print(f"{key:<15}{value}")


if __name__=="__main__":
    main()    
