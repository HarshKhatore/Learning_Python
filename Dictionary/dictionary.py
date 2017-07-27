import requests
import os
import installation
try:
    from lxml import etree
except ImportError:
    installation.install()
    from lxml import etree

def main():
    with open("wordlist.txt", "r") as filestream:
        for line in filestream:
            wordList = line.replace(" ", "").split(',')
    
    # A dictionary to store meaning of all words
    meaning = {}        
    for word in wordList:
        # REMEMBER TO HIDE THE PRODUCT KEY
        url = "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/"+word+"?key=<your_key>";
        try:
            re = requests.get(url)
            root = etree.fromstring(re.content)
            meaning[word] = root.xpath('//entry_list/entry/def/dt/text()')
        except requests.ConnectionError as e:
            print "Connection error. Check your network connection."
    
    write = open("meanings.txt", "w")
        
    for k, v in meaning.iteritems():
        write.write(k+":\n")
        no_of_meanings = len(meaning[k])
        
        if no_of_meanings > 4:
            no_of_meanings = 4
            
        for i in range(no_of_meanings):
            meaning[k][i] = meaning[k][i].replace(":"," ")
            if(len(meaning[k][i]) > 1):
                write.write("\t->"+meaning[k][i]+"\n\n")
        
if __name__ == "__main__":
    main()
