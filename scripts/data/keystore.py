#!/usr/bin/python
from files.storage \
    import storagePageFile

from os.path \
    import isdir

from os \
    import mkdir

from data.store.storage_database \
    import storage_database

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
        self.database = storage_database()

    def __clear_files( self ):
        self.__files = []

    # Setup index
    def load( self ):
        global completePath
        

    def find( self, key ):
        pass

    def build_structure( self, key, value ):
        pass

    def delete_structure( self, key ):
        pass

    def __remove_cache( self, key ):

        pass


    def write( self ):
        pass

    def flush( self ):
        pass

    def __cache( self ):
        pass
