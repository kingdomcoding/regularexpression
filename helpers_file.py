import re
def generate_splitted_memory_verse(memory_verse_full):
    verse_reference_pattern = "\s[1-3].*"
    # DEBUG: "[1-3]?\s*\w+\s*\d+:\d+\s*"
    # DEBUG: "[1-3]?\s*\w+\s*\d+.*|[1-3]?\s*\w+\s*\d+\s*|[1-3]?\s*\w+\s*\d+:\d+.*|[1-3]?\s*\w+\s*\d+:\d+\s*"

    #memory_verse_full = "Whoever loves his brother lives in the light, and there is\nnothing in him to make him stumble. 1 John 2:10, NIV"
    #memory_verse_full.encode("ansi")
    memory_verse_list = memory_verse_full.split(" ")
    #print (memory_verse_list)

    temp_list = []
    reference_start = None
    reference_string = ""
    verse_text = ""
    for index in range(len(memory_verse_list)):
        if (re.match("\d+:\d+", memory_verse_list[index])): #if you find a token with a colon
            if (re.match("\(?\w+", memory_verse_list[index-1])): # if the token before is a word
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
    return (dictionary)

def generate_date_and_text(date_and_text):
    date_pattern = """.*Sunday, January \d?\d\s|.*Monday, January \d?\d\s|.*Tuesday, January \d?\d\s|.*Wednesday, January \d?\d\s|.*Thursday, January \d?\d\s|.*Friday, January \d?\d\s|.*Saturday, January \d?\d\s|.*Sunday, February \d?\d\s|.*Monday, February \d?\d\s|.*Tuesday, February \d?\d\s|.*Wednesday, February \d?\d\s|.*Thursday, February \d?\d\s|.*Friday, February \d?\d\s|.*Saturday, February \d?\d\s|.*Sunday, March \d?\d\s|.*Monday, March \d?\d\s|.*Tuesday, March \d?\d\s|.*Wednesday, March \d?\d\s|.*Thursday, March \d?\d\s|.*Friday, March \d?\d\s|.*Saturday, March \d?\d\s|.*Sunday, April \d?\d\s|.*Monday, April \d?\d\s|.*Tuesday, April \d?\d\s|.*Wednesday, April \d?\d\s|.*Thursday, April \d?\d\s|.*Friday, April \d?\d\s|.*Saturday, April \d?\d\s|.*Sunday, May \d?\d\s|.*Monday, May \d?\d\s|.*Tuesday, May \d?\d\s|.*Wednesday, May \d?\d\s|.*Thursday, May \d?\d\s|.*Friday, May \d?\d\s|.*Saturday, May \d?\d\s|.*Sunday, June \d?\d\s|.*Monday, June \d?\d\s|.*Tuesday, June \d?\d\s|.*Wednesday, June \d?\d\s|.*Thursday, June \d?\d\s|.*Friday, June \d?\d\s|.*Saturday, June \d?\d\s|.*Sunday, July \d?\d\s|.*Monday, July \d?\d\s|.*Tuesday, July \d?\d\s|.*Wednesday, July \d?\d\s|.*Thursday, July \d?\d\s|.*Friday, July \d?\d\s|.*Saturday, July \d?\d\s|.*Sunday, August \d?\d\s|.*Monday, August \d?\d\s|.*Tuesday, August \d?\d\s|.*Wednesday, August \d?\d\s|.*Thursday, August \d?\d\s|.*Friday, August \d?\d\s|.*Saturday, August \d?\d\s|.*Sunday, September \d?\d\s|.*Monday, September \d?\d\s|.*Tuesday, September \d?\d\s|.*Wednesday, September \d?\d\s|.*Thursday, September \d?\d\s|.*Friday, September \d?\d\s|.*Saturday, September \d?\d\s|.*Sunday, October \d?\d\s|.*Monday, October \d?\d\s|.*Tuesday, October \d?\d\s|.*Wednesday, October \d?\d\s|.*Thursday, October \d?\d\s|.*Friday, October \d?\d\s|.*Saturday, October \d?\d\s|.*Sunday, Nobember \d?\d\s|.*Monday, Nobember \d?\d\s|.*Tuesday, Nobember \d?\d\s|.*Wednesday, Nobember \d?\d\s|.*Thursday, Nobember \d?\d\s|.*Friday, Nobember \d?\d\s|.*Saturday, Nobember \d?\d\s|.*Sunday, December \d?\d\s|.*Monday, December \d?\d\s|.*Tuesday, December \d?\d\s|.*Wednesday, December \d?\d\s|.*Thursday, December \d?\d\s|.*Friday, December \d?\d\s|.*Saturday, December \d?\d\s
    """

    #sample = "Tuesday, January 1 1 John 2:9-11"

    match_string = re.match(date_pattern, date_and_text)
    date = ""
    if(match_string):
        date = match_string.group()
        #print(date)
    text = date_and_text.replace(date, '')
    # TODO: #date = date.trim()
    # TODO: #text = text.trim()

    return {"date": date, "text": text}

def split_into_days(lines):
    pattern = "Sunday,.*|Monday,.*|Tuesday,.*|Wednesday,.*|Thursday,.*|Friday,.*|Saturday,.*"
    days = []
    day = []
    p = re.compile(pattern, re.IGNORECASE)
    for line in lines:
        if (p.match(line)):
            if (day != []):
                days.append(day)
            day = []
            day.append(line)
        else:
            day.append(line)
        days.append(day)
    return days

def split_into_groups(days):
    almost_final_json = []

    verse_pattern = ".*AMP.*|.*ESV.*|.*GNB.*|.*KJV.*|.*TLB.*|.*NAS.*|.*NASB.*|.*NIV.*|.*NKJV.*|.*NLT.*|.*RSV.*|.*NET.*|.*\d$|.*\d\s*$|.*\d,$|.*\d\)$|.*\d[a-z]$"
    birthday_blessing_start_pattern = "^.*Birthday.*"
    rbt_passage_pattern = ".*RBT.*"

    for day in days:
        day_almost_json = {}
        day_almost_json["date and text"] = day[0]
        day_almost_json["topic"] = day[1]

        json_fields = ["", "", "", "", ""]
        json_field_counter = 0
        for i in range(2, len(day)):
            if (json_field_counter == 0):
                if (not re.match(verse_pattern, day[i])):
                    json_fields[json_field_counter] += day[i]
                else:
                    json_fields[json_field_counter] += day[i]
                    json_field_counter += 1

            elif (json_field_counter == 1):
                if not (re.match(birthday_blessing_start_pattern, day[i])):
                    json_fields[json_field_counter] += day[i]
                else:
                    json_field_counter += 1
                    json_fields[json_field_counter] += day[i] # append first line to birthday blessing string
                    if (re.match(verse_pattern, day[i])): # hence, it matches birthday blessing end pattern
                        json_field_counter += 1 #increment counter to skip birthday blessing entirely. already gotten to the end of the one line birthday blessing
            elif (json_field_counter == 2):
                if not (re.match(verse_pattern, day[i])): # hence, does it match birthday blessing end pattern?
                    json_fields[json_field_counter] += day[i]
                else:
                    json_fields[json_field_counter] += day[i]
                    json_field_counter += 1
            elif (json_field_counter == 3):
                if not (re.match(rbt_passage_pattern, day[i])): # was deceived by a verse patter to think start of rbt
                    json_fields[json_field_counter - 1] += day[i] # add it to the rbt string (the previous string)
                else:
                    json_fields[json_field_counter] += day[i]
                    json_field_counter += 1
            elif (json_field_counter == 4):
                if (i < (len(day)-1)): # If not the last element in the days
                    json_fields[json_field_counter] += day[i]



        day_almost_json["memory_verse"] = json_fields[0]
        day_almost_json["paragraphs"] = json_fields[1]
        day_almost_json["birthday blessing"] = json_fields[2]
        day_almost_json["rbt passage"] = json_fields[3]
        day_almost_json["quote and author"] = json_fields[4]


        almost_final_json.append(day_almost_json)
    return almost_final_json

def generate_paragraphs(paragraphs):
    return {"paragraphs": clean(paragraphs)}

def generate_topic(topic):
    #print("debug")
    return {"topic": clean(topic)}

def generate_splitted_birthday_blessing(birthday_blessing_full):
    verse_reference_pattern = "\s[1-3].*"

    birthday_blessing_list = birthday_blessing_full.split(" ")

    temp_list = []
    reference_start = None
    reference_string = ""
    verse_text = ""
    for index in range(len(birthday_blessing_list)):
        if (re.match("\d+:\d+", birthday_blessing_list[index])): #if you find a token with a colon
            if (re.match("\w+", birthday_blessing_list[index-1])): # if the token before is a word
                reference_start = index - 1

                if(re.match(".*\n?.*[1-3]", birthday_blessing_list[index-2])): # if two tokens before has a number as in 1 John 2:3
                    #print("debug")
                    temp_list = birthday_blessing_list[index-2].split("\n")
                    if(len(temp_list) == 2):
                        reference_string += temp_list[1] + " "
                    else:
                        reference_string += birthday_blessing_list[index-2] + " "
                    reference_start = index - 2


                temp_list = birthday_blessing_list[index-1].split("\n")
                if(len(temp_list) == 2):
                    reference_string += temp_list[1] + " "
                else:
                    reference_string += birthday_blessing_list[index-1] + " "
            for i in range(index, len(birthday_blessing_list)):
                reference_string += birthday_blessing_list[i] + " "

            for i in range(reference_start - 1):
                verse_text += birthday_blessing_list[i] + " "

            if(len(temp_list) == 2):
                verse_text += temp_list[0] + " "
            else:
                verse_text += birthday_blessing_list[reference_start - 1] + " "

            break
        elif (birthday_blessing_list[index] == "Jude" and re.match("\d+", birthday_blessing_list[index + 1])):
            for i in range(index):
                verse_text += birthday_blessing_list[i] + " "
            for i in range(index, len(birthday_blessing_list)):
                reference_string += birthday_blessing_list[i] + " "



    #print(verse_text)
    #print()
    #print(reference_string)
    verse_text_list = verse_text.split(" ")
    verse_text = ""
    for i in range(len(verse_text_list)):
        #print(verse)
        #if (re.match(".*Blessing.*|.*blessing.*", verse)):
        if (verse_text_list[i] == "Blessing:"):
            #print("debug")
            #if (re.match(".*Birthday.*|.*birthday.*", verse)):
            if (verse_text_list[i-1] == "Birthday"):
                #print("debug")
                for index in range(i + 1, len(verse_text_list)):
                    #print(index)
                    verse_text += verse_text_list[index] + " "
    #print(verse_text_list)

    dictionary = {"birthdayblessing": clean(reference_string), "birthdayblessingtext": clean(verse_text)}
    return (dictionary)

def generate_rbt(rbt_text):
    rbt_list = rbt_text.split(" ")

    rbt_text = ""
    for i in range(len(rbt_list)):
        if (rbt_list[i] == "Passage:"):
            if (rbt_list[i-1] == "RBT"):
                for index in range(i + 1, len(rbt_list)):
                    rbt_text += rbt_list[index] + " "
                #break
    #print(verse_text_list)

    dictionary = {"Rbtpassage": clean(rbt_text)}
    return (dictionary)

def generate_quote_and_author(text):
    text_list = text.split("\u00ef\u00bf\u00bd")

    author = text_list[-1]

    quote = ""
    for index in range(len(text_list) - 1):
        quote += text_list[index] + "\u00ef\u00bf\u00bd"
    dictionary = {"quote": clean(quote), "author": clean(author)}
    return (dictionary)

def clean(string):

    string =  string.strip().replace('\u00ef\u00bf\u00bd', '')
    #print (string)
    return string



'''def generate_splitted_paragraph(paragraph):
    paragraph_split_list = paragraph.split("\n")
    #print (paragraph_split_list)

    #paragraph_list = ["","", "", ""]
    paragraph_list = []
    string = ""
    for line in paragraph_split_list:
        if (re.match("[A-Z].*", line)):
            if (string == ""):
                string += line + " "
            else:
                paragraph_list.append(string)
                string = ""
                string += line + " "
        else:
            string += line + " "
            #paragraph_list.append(string)
    paragraph_list.append(string) # append the last string
    return (paragraph_list)'''
