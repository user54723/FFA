# -*- coding: utf-8 -*-

from numpy import *
import os
import xml.etree.ElementTree as et
import scipy.io.wavfile.read
        
class WordList :
    def __init__(self, name, index, speaker_quality, description, words) :
        self.name = name
        self.index = index
        self.description = description
        self.speaker_quality = speaker_quality
        self.words = words

class Word : 
    def __init__(self, name, index, wave_file, wave_start_position, wave_duration) :
        self.name = name
        self.index = index
        self.wave_file = wave_data
        self.wave_start_position = wave_start_position
        self.wave_duration = wave_duration

def parseOtoSuiteWordList(otoSuiteFolder="./otosuite") :
    #est ce que le dossier existe
    try : os.chdir(otoSuiteFolder)
    except : return -1
    rootDir = os.path.abspath(os.curdir())
    wordlists = []
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
            try :
                wordlistindex = int(wordlistname.split(" ")[-2])
                speaker_quality = wordlistname.split(" ")[-1][1:-1]
                wordlistname = " ".join(wordlistname.split(" ")[:-2])
            except : 
                wordlistindex = 0
                speaker_quality = "U"
            description = wordlist.find("Description").text
            item_number = len(wordlist.find(".//WordDefinition"))
            #On construit la liste de mot contenu dans la wordlist
            words = []
            #les données audio seront ensuite stockée sous forme de fichier wav 
            #compréssé (un par type de liste)
            wave_file_name = word.find("FileName").text
            wave_file = (os.path.sep).join([curdir, wave_file_name])
            word_index = 0
            for word in wordlist.findall(".//WordDefinition") :
                assert wave_file_name == word.find("FileName").text
                word_name = word.find("Word").text
                wave_start_position = int(word.find("StartPosition").text)
                wave_duration = int(word.find("Duration").text)
                words.append(Word(word_name, word_index, wave_file, wave_start_position, wave_duration))
                word_index += 1
            wordlists
                
import sys
from PyQt5.QtCore import QObject, pyqtSlot, QVariant
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

class FFA(QObject):
    def __init__(self, qmlContext, parent=None):
        super(FFA, self).__init__(parent)
        self.window = parent
        self.qmlContext = qmlContext
        
if __name__ == "__main__":
    app_qt = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    # Création d'un objet QQmlContext pour communiquer avec le code QML
    qmlContext = engine.rootContext()
    engine.load('ui.qml')
    window = engine.rootObjects()[0]
    py_FFA = FFA(qmlContext, window)
    qmlContext.setContextProperty("py_FFA", py_FFA)
    window.show()
    sys.exit(app_qt.exec())
                        