import wx
import gui
import os
import csv
import random

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
    session_id = None
    session_date = None
    session_length = None
    session_lang = None

    flashcards = None  # list of the loaded flashcards
    used_flashcard_ids = []

    overall_avg = None
    session_avg = None

    def __init__(self):
        print('init without anything else')

    def __init__(self, session_id, session_date, session_length, session_lang, flashcards, used_flashcard_ids,
                 overall_avg, session_avg):
        self.session_id, self.session_date, self.session_length, self.session_lang, self.flashcards, self.used_flashcard_ids, self.overall_avg, self.session_avg = session_id, session_date, session_length, session_lang, flashcards, used_flashcard_ids, overall_avg, session_avg

    def draw_flashcard(self):  # DRAW
        d = random.choice([x for x in self.flashcards if self.flashcards.index(x) not in self.used_flashcard_ids])
        self.used_flashcard_ids.append(self.flashcards.index(d))
        return d


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
