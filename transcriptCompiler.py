import re

if __name__ == "__main__":
    for n in range(1,9):
        f = open('Atypical/Text Transcripts/1_%s.txt' % n, 'w+')
        outputText = ""
        for line in open('Atypical/JSON Transcripts/1_%s.json.txt' % n):
            if line.strip().startswith('\"#text\": \"'):
                line = line.strip()
                offset = 10
                newstring = line[offset:len(line)-1].replace("...","###").replace("\\\"","\"").replace(".\"","$$$$").replace(".",".\n").replace("!","!\n").replace("?","?\n").replace("###","...").replace("$$$$",".\"\n").replace(" -","\n").strip("-")
                newstring = re.sub("[\[].*?[\]][ ]*","",newstring)
                outputText += newstring + " "
        for line in outputText.split('\n'):
            f.write(line.strip(' ')+"\n")