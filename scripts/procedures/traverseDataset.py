#!/usr/bin/python
from os \
    import getcwd, \
           walk, \
           pardir


from os.path \
    import abspath, \
           join

from os.path import splitext

from typing \
    import Final


from procedures.objects.datasetEntry \
    import generate_entry

from procedures.objects.indices \
    import index_entry


pathToDataset = '/dataset'


def get_parent( fromPath ):
    return abspath( join( fromPath, pardir ) )

def repository_parent():
    return get_parent( getcwd() )

def combine_str( a, b ):
    return a + b

def is_fit_file( path ):
    splitted = splitext( path )

    if( splitted[ len( splitted ) -1 ] == '.fit' ):
        return True

    return False


class dataset:
    def __init__( self ):
        global pathToDataset

        self.debug = False

        self.directory_name: Final[str] = pathToDataset

        self.parent = None
        self.datasetPath = None

        self.found = None
        self.index = None

    def size( self ):
        return len( self.found )


    def run( self ):
        self.init_found()
        self.init_index()

        self.parent = repository_parent()
        self.set_dataset( combine_str( self.parent, self.directory_name ) )

        self.__traverse()
        self.__index()


    def __traverse( self ):
        for root, dirs, files \
            in walk( self.get_dataset(), topdown=True ):

            for filename \
                in files:

                foundPath = join( root, filename )

                if( is_fit_file( foundPath ) ):
                    entry = generate_entry( self.get_dataset(), foundPath )
                    self.found.append( entry )


    def __index( self ):
        if self.found == None:
            return

        iterator = 0

        for element \
            in self.found:

            record_date = element.get_date()

            if not self.origin_is_in_set( record_date ):
                new_indice = index_entry()

                new_indice.set_key( record_date )
                new_indice.set_start_position( iterator )
                
                self.index.append( new_indice )

            iterator = iterator + 1


    def origin_is_in_set( self, key ):
        rV = False

        for indice \
            in self.index:

            if indice.compare( key ):
                rV = True
                break

        return bool( rV )


    def get_dataset( self ):
        return self.datasetPath

    def set_dataset( self, value ):
        self.datasetPath = value


    def get_parent( self ):
        return self.parent

    def set_parent( self, value ):
        self.parent = value

    
    def is_debugging( self ):
        return self.debug

    def set_debug_mode( self, value ):
        self.debug = value


    def get_found( self ):
        return self.found

    def set_found( self, v ):
        self.found = v

    def init_found( self ):
        self.set_found( [] )


    def get_index( self ):
        return self.index

    def set_index( self, v ):
        self.index = v

    def init_index( self ):
        self.set_index( [] )

