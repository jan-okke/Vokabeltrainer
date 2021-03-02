import wx
import gui
import os

App = wx.App()


class MainFrame(gui.UserInterfaceFrame):
    def __init__(self, parent):
        super().__init__(parent)

    # TODO


class Data:
    def __init__(self, content):
        self.content = content

    def as_list(self):
        return list(self.content)  # TODO

    def as_dict(self):
        return dict(self.content)  # TODO


class Statistics:
    def __init__(self):
        self.number_trainings = 0
        self.number_known_vocabularies = 0
        self.tried_languages = []
        self.correct_guesses = 0
        self.wrong_guesses = 0
        self.success_rate = 0  # in percentage

    def load(self, cwd):
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

    def save(self, data: Data):
        pass  # TODO


class Trainer:
    def __init__(self):
        self.statistics = Statistics()
        self.statistics.load(os.getcwd())

    def start_training(self, vocabulary_list_name, language):
        # GUI.TODO
        Vocabulary = VocabularyList(os.getcwd())
        Vocabulary.load(vocabulary_list_name, language)
        self.statistics.wrong_guesses += 1  # like this TODO


class VocabularyList:
    def __init__(self, cwd: str):
        self.cwd = cwd  # current working directory
        self.vocabulary_list = []

    def load(self, name: str, language: str) -> Data:
        try:
            data = Data(open(self.cwd + "\\" + name, "r"))
            # TODO: language
            return data  # TODO
        except FileNotFoundError:
            wx.MessageBox("Invalid vocabulary list name!")

    def save(self, name: str, data: Data):
        file = open(self.cwd + "\\" + name, "w")
        # No exception because files that don't exists will be created
        # TODO: saving process in correct data segments
