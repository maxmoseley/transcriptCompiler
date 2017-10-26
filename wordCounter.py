from collections import Counter

for n in range(1,9):
    f = open('Atypical/Word Lists/1_%s words.txt' % n, 'w+')
    file = open('Atypical/Text Transcripts/1_%s.txt' % n)
  #  for line in file:
  #      line = line.replace("...","").replace(".","").replace(",","").replace("!","").replace("?","").replace("\"","")
 #       line = line.strip("...",".",",","!","?","\"")
#    file.read().strip("...").strip(".").strip(",").strip("!").strip("?").strip("\"")
    wordcount = Counter(file.read().split())
    f.write("{}\t{}\r".format("Word", "Count"))
    for item in wordcount.items():
        f.write("{}\t{}\r".format(*item))