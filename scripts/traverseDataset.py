#!/usr/bin/python
from os \
    import getcwd, \
           walk, \
           pardir

from os.path \
    import abspath, \
           join

from typing \
    import Final

from datasetEntry \
    import entry_found, generate_entry

pathToDataset = '/dataset'


def get_parent( fromPath ):
    return abspath( join( fromPath, pardir ) )

def repository_parent():
    return get_parent( getcwd() )

def combine_str(a, b):
    return a + b


class dataset:
    def __init__(self):
        global pathToDataset

        self.debug = False

        self.directory_name: Final[str] = pathToDataset

        self.parent = None
        self.datasetPath = None

        self.found = None
        self.index = None


    def run(self):
        self.init_found()
        self.init_index()

        self.parent = repository_parent()
        self.set_dataset( combine_str( self.parent, self.directory_name ) )

        self.__traverse()


    def __traverse(self):
        for root, dirs, files in walk( self.get_dataset(), topdown=True ):
            for filename in files:

                foundPath = join( root, filename )
                entry = generate_entry( self.get_dataset(), foundPath )

                self.found.append(entry)


    def get_dataset(self):
        return self.datasetPath

    def set_dataset(self, value):
        self.datasetPath = value


    def get_parent(self):
        return self.parent

    def set_parent(self, value):
        self.parent = value

    
    def is_debugging(self):
        return self.debug

    def set_debug_mode(self, value):
        self.debug = value


    def get_found(self):
        return self.found

    def set_found(self, v):
        self.found = v

    def init_found(self):
        self.set_found( [] )

    def get_index(self):
        return self.index

    def set_index(self, v):
        self.index = v

    def init_index(self):
        self.set_index( [] )

