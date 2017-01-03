# -*- coding: utf-8 -*-

from numpy import *
import os
import xml.etree.ElementTree as et
import scipy.io.wavfile.read
        
class WordList :
    def __init__(self, name, description, words) :
        try :
            index = int(name.split(" ")[-2])
            speaker_quality = name.split(" ")[-1][1:-1]
        except : 
            index = 0
            speaker_quality = "U"
        self.name = name
        self.index = index
        self.description = description
        self.speaker_quality = speaker_quality
        self.words = words

class Word : 
    def __init__(self, name, parent_wordlist, index, wave_data, duration, fech) :
        self.name = name
        self.parent_wordlist_name = parent_wordlist_name
        self.index = index
        self.wave_data_location = wave_data_location
        self.duration = duration

def parseOtoSuiteWordList(otoSuiteFolder="./otosuite") :
    #est ce que le dossier existe
    try : os.chdir(otoSuiteFolder)
    except : return -1
    rootDir = os.path.abspath(os.curdir())
    for folder in os.listdir(rootDir) :
        #est ce que le dossier contient un fichier de définition otosuite
        curdir = (os.path.sep).join([rootDir, folder])
        try : 
            xmldef_file = (os.path.sep).join([curdir, "0.wordlistdefinition"])
            tree = et.parse(xmldef_file)
        except : continue
        #parsing
        r = tree.getroot()
        for wordlist in r.findall(".//Wordlist") :
            wordlistname = wordlist.find("Name").text
            description = wordlist.find("Description").text
            item_number = len(wordlist.find(".//WordDefinition"))
            words = []
            wave_file_name = None
            wave_file_loc = None
            wave_data = None
            wave_fech = None
            for word in wordlist.findall(".//WordDefinition") :
                if wave_file_name == None :
                    wave_file_name = word.find("FileName").text
                    wave_file_loc = (os.path.sep).join([curdir, wave_file_name])
                    wave_fech, data = scipy.io.wavfile.read(wave_file_loc)
                    wave_data = data[:,0]
                else : 
                    assert wave_file_name == word.find("FileName").text
                word_name = word.find("Word").text
                word_timepos = word.find("StartPosition").text
                word_duration = word.find("Duration").text
                
                