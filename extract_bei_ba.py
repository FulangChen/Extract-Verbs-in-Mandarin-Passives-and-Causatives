import csv
import re
import os

folder = "wiki_zh" # downloaded from https://github.com/brightmart/nlp_chinese_corpus (wiki2019zh)
path = os.path.join(os.getcwd(), folder)

f_bei = open("bei.txt", "w", encoding='utf-8')
f_ba = open("ba.txt", "w", encoding='utf-8')
for filename in os.listdir(path):
    path2 = os.path.join(path, filename)
    for filename2 in os.listdir(path2):
        path3 = os.path.join(path2, filename2)
        print(path3)
        with open(path3, 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                for sent in row:
                    match = re.search("[^。，：]*被[^。，：]*", sent)
                    if match:
                        s = match.group().split("\\n")[-1] + "\n"
                        f_bei.write(s)
                        # print(s)
                    match = re.search("[^。，：]*把[^。，：]*", sent)
                    if match:
                        s = match.group().split("\\n")[-1] + "\n"
                        f_ba.write(s)
                        # print(s)
        file.close()
f_ba.close()
f_bei.close()