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

pathToDataset = '/dataset'


class dataset:
    def __init__(self):
        global pathToDataset
        
        self.set_debug_mode(False)

        self.directory_name: Final[str] = pathToDataset

        self.parent = None
        self.datasetPath = None



    def run(self):
        currentPath = getcwd()
        self.parent = abspath(join(currentPath, pardir))

        self.set_dataset( self.parent + self.directory_name )
        

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
