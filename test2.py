import re

def generate_splitted_memory_verse(memory_verse_full):
    verse_reference_pattern = "\s[1-3].*"
    # DEBUG: "[1-3]?\s*\w+\s*\d+:\d+\s*"
    # DEBUG: "[1-3]?\s*\w+\s*\d+.*|[1-3]?\s*\w+\s*\d+\s*|[1-3]?\s*\w+\s*\d+:\d+.*|[1-3]?\s*\w+\s*\d+:\d+\s*"

    #memory_verse_full = "Whoever loves his brother lives in the light, and there is\nnothing in him to make him stumble. 1 John 2:10, NIV"
    #memory_verse_full.encode("ansi")
    memory_verse_list = memory_verse_full.split(" ")
    print (memory_verse_list)

    temp_list = []
    reference_start = None
    reference_string = ""
    verse_text = ""
    for index in range(len(memory_verse_list)):
        #print("debug")
        if (re.match("\d+:\d+", memory_verse_list[index])): #if you find a token with a colon
            #print(memory_verse_list[index])
            if (re.match("\(?\w+", memory_verse_list[index-1])): # if the token before is a word
                print("debug")
                reference_start = index - 1

                if(re.match(".*\n?.*[1-3]", memory_verse_list[index-2])): # if two tokens before has a number as in 1 John 2:3
                    #print("debug")
                    temp_list = memory_verse_list[index-2].split("\n")
                    if(len(temp_list) == 2):
                        reference_string += temp_list[1] + " "
                    else:
                        reference_string += memory_verse_list[index-2] + " "
                    reference_start = index - 2


                temp_list = memory_verse_list[index-1].split("\n")
                if(len(temp_list) == 2):
                    reference_string += temp_list[1] + " "
                else:
                    reference_string += memory_verse_list[index-1] + " "
            for i in range(index, len(memory_verse_list)):
                reference_string += memory_verse_list[i] + " "

            for i in range(reference_start - 1):
                verse_text += memory_verse_list[i] + " "

            if(len(temp_list) == 2):
                verse_text += temp_list[0] + " "
            else:
                verse_text += memory_verse_list[reference_start - 1] + " "

            break

    #print(verse_text)
    #print()
    #print(reference_string)
    dictionary = {"memoryverse": reference_string, "memoryversetext": verse_text}
    print (dictionary)

f = open("C:\\Users\\user\\Documents\\Seek Daily\\sample.txt", encoding="ansi")
sample = f.read()
#print(sample)
generate_splitted_memory_verse(sample)
