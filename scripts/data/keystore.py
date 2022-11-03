#!/usr/bin/python
from files.storage \
    import storagePageFile

from os.path \
    import isdir

from os \
    import mkdir

from data.searchStore \
    import find_store_files

root_tmp_path = "/tmp/"
tmp_soft_path = "/garmin-data-storage"

completePath = root_tmp_path + tmp_soft_path


def init_directory():
    global completePath
    fullPath = completePath

    if( not isdir( fullPath ) ):
        mkdir( fullPath )
        return True

    # Done nothing
    return False


# 
class key_storage_database:
    def __init__( self ):
        init_directory()

        self.__files = None
        self.__clear_files()
        
        self.load()

    def __clear_files( self ):
        self.__files = []

    def load( self ):
        global completePath
        self.__files = find_store_files( completePath )


    def write( self ):
        pass

    def flush( self ):
        pass

    def __cache( self ):
        pass
