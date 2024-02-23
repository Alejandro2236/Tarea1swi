import os.path
import re


class File():
    def __init__(self, path: str):
        self._path = path

    def CountWordOcurrences(self, word: str):
        """
        Read the text file and count how many times the given word appears.
        :param word: The word that will be searched and counted in the file
        :return: The total ocurrences of the word in the file
        """
        try:
            with open(self._path, 'r', encoding='utf-8') as file:
                text = file.read()
                ocurrences = len(re.findall(r'\b' + re.escape(word.lower()) + r'\b', text.lower()))
                return ocurrences
        except FileNotFoundError:
            raise FileNotFoundError("File doesn't found")

    def __str__(self):
        return os.path.basename(self._path)
