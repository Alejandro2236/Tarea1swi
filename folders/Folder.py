import os.path

from folders.File import File


class Folder():
    def __init__(self, path: str):
        if not os.path.isdir(path):
            raise FileNotFoundError(f"The folder {path} was not found")
        self._path = path
        self._files: list[File] = []
        self._GetFiles()

    def _GetFiles(self):
        """
        Search all the text files in the folder path and adds to the files list each one of them
        """
        for fileName in os.listdir(self._path):
            filePath = os.path.join(self._path, fileName)
            if os.path.isfile(filePath) and fileName.endswith(('.txt', '.xml', '.json', '.csv')):
                self._files.append(File(filePath))
        if not self._files:
            raise FileNotFoundError(f"Text files not found in {self._path}")

    def CountWordOcurrences(self, word: str) -> int:
        """
        Check the text files inside the folder and count how many times a given word appears.
        :param word: The word that will be searched and counted in the files inside the folder
        :return: The total ocurrences of the word inside the text files
        """
        count: int = 0
        for file in self._files:
            currentOcurrences = file.CountWordOcurrences(word)
            print(f"{file}: {currentOcurrences}")
            count += currentOcurrences
        return count

    def __str__(self):
        return os.path.basename(self._path)
