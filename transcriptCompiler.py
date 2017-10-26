import argparse
import json
import re

if __name__ == "__main__":
    for n in range(1,9):
        parser = argparse.ArgumentParser(description='Read filenames.')
        parser.add_argument('--transcript', help='the transcript file', default = 'JSON Transcripts/1_%s.json.txt' % n)
        args = parser.parse_args()
        transcriptTXT = args.transcript
        #episodeScript = json.loads(open('JSON Transcripts/1_%s.json' % n).read())
#        episodeScript = json.loads(open(transcriptJSON).read())
        f = open('Text Transcripts/1_%s.txt' % n, 'w+')
#        for line in episodeScript:
#        for line in transcriptTXT:
        outputText = ""
        for line in open('JSON Transcripts/1_%s.json.txt' % n):
            #print line.strip()
           
            if line.strip().startswith('\"#text\": \"'):
                line = line.strip()
                offset = 10
                newstring = line[offset:len(line)-1].replace("...","###").replace("\\\"","\"").replace(".\"","$$$$").replace(".",".\n").replace("!","!\n").replace("?","?\n").replace("###","...").replace("$$$$",".\"\n").replace(" -","\n").strip("-")
                newstring = re.sub("[\[].*?[\]][ ]*","",newstring)
                outputText += newstring + " "
        for line in outputText.split('\n'):
            f.write(line.strip(' ')+"\n")
                        #            print line
#            if line.startswith('\"#text\": \"'):
#                f.write(line.strip('\"#text\": \"').strip('\"'))