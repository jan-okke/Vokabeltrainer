import wx
import gui
import os
import csv

App = wx.App()


class MainFrame(gui.UserInterfaceFrame):
    def __init__(self, parent):
        super().__init__(parent)

    # TODO


"""
class Data:
    def __init__(self, content):
        self.content = content

    def as_list(self):
        return list(self.content)  # TODO

    def as_dict(self):
        return dict(self.content)  # TODO
"""


class Statistics:
    def __init__(self):
        self.number_trainings = 0
        self.number_known_vocabularies = 0
        self.tried_languages = []
        self.correct_guesses = 0
        self.wrong_guesses = 0
        self.success_rate = 0  # in percentage

    def load(self, cwd):
        """
        try:
            data = Data(open(cwd + "\\statistics.txt", "r")).as_dict()
            self.number_trainings = int(data["NumberTrainings"])
            self.number_known_vocabularies = int(data["NumberKnownVocabularies"])
            self.tried_languages = list(data["TriedLanguages"])
            self.correct_guesses = int(data["CorrectGuesse  s"])
            self.wrong_guesses = int(data["WrongGuesses"])
            self.success_rate = self.correct_guesses / (self.correct_guesses + self.wrong_guesses) * 100

        except FileNotFoundError:
            wx.MessageBox("Couldn't load the local statistics file.")
        """
        pass

    def save(self, data):
        pass  # TODO


class Trainer:
    def __init__(self):
        self.statistics = Statistics()
        self.statistics.load(os.getcwd())

    def start_training(self, vocabulary_list_name, language):
        # GUI.TODO
        Vocabulary = VocabularyList(os.getcwd())
        Vocabulary.load(vocabulary_list_name)
        self.statistics.wrong_guesses += 1  # like this TODO


class VocabularyData:
    def __init__(self, languages, name):
        self.languages = languages
        self.name = name
        self.content = []

    def add_content(self, content: list = ["lang1", "lang2"]):
        self.content.append(content)

    def clear(self):
        self.content.clear()


class VocabularyList:
    def __init__(self, cwd: str):
        self.cwd = cwd + "\\Vocabulary\\"  # current working directory
        self.vocabulary_list = []

    def load(self, vocabulary_name: str) -> VocabularyData:
        data = open(self.cwd + vocabulary_name + ".txt", "r")
        csv_data = csv.reader(data)
        # new_data = VocabularyData(csv_data[0], vocabulary_name)
        index = 0
        new_data = VocabularyData([], "")  # Empty, ignore
        for _data in csv_data:
            index += 1
            if index == 1:
                new_data = VocabularyData(_data, vocabulary_name)
                continue
            new_data.add_content(_data)
        # print(new_data.content, new_data.languages, new_data.name)

        return new_data

    def save(self, data: VocabularyData):
        path = self.cwd + data.name + ".txt"
        output = open(path, "w", newline="")
        writer = csv.writer(output)
        writer.writerow(data.languages)
        for content in data.content:
            writer.writerow(content)

def test():
    TestList = VocabularyList(os.getcwd())
    d = TestList.load("test2")
    d.add_content(["Vogel", "bird"])
    TestList.save(d)
