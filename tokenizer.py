import re
import json
from helpers_file import generate_date_and_text, generate_splitted_memory_verse, split_into_days, split_into_groups, generate_splitted_birthday_blessing, generate_rbt, generate_quote_and_author, generate_paragraphs, generate_topic

fp = open('result.json', 'w')
#fp2 = open('quote.json', 'w')

lines = []
with open("C:\\Users\\user\\Documents\\Seek Daily\\test.txt", encoding="ansi") as openFileObject:
    for line in openFileObject:
        lines.append(line)



days = split_into_days(lines)

almost_final_json = split_into_groups(days)
print(almost_final_json)
final_json = {}

for json_element in almost_final_json:
    received_dict = generate_date_and_text(json_element["date and text"])
    final_json.update(received_dict)

    received_dict = generate_topic(json_element["topic"])
    #print(received_dict)
    final_json.update(received_dict)
    #print("debug")
    received_dict = generate_splitted_memory_verse(json_element["memory_verse"])
    final_json.update(received_dict)
    #print("debug")
    received_dict = generate_paragraphs(json_element["paragraphs"])
    final_json.update(received_dict)

    received_dict = generate_splitted_birthday_blessing(json_element["birthday blessing"])
    final_json.update(received_dict)

    received_dict = generate_rbt(json_element["rbt passage"])
    final_json.update(received_dict)

    received_dict = generate_quote_and_author(json_element["quote and author"])
    final_json.update(received_dict)

    #print(final_json)
    json.dump(final_json, fp)
