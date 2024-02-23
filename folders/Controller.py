from folders.Folder import Folder


class Controller():

    def __init__(self):
        pass

    def CountWordOcurrencesOnFolder(self):
        """
        Reads the folder path and the searched word to be from the user, and starts the process to count the
        ocurrences of the word inside the given folder
        """
        folderPath: str = input("Enter the full path to the folder: ")
        word: str = input("Enter the word you wish to search for: ")
        folder = Folder(folderPath)
        print(f"Ocurrences of the word '{word}' in {folder}")
        print(f"Total in {folder}: {folder.CountWordOcurrences(word)}")
