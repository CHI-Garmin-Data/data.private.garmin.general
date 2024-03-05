#!/usr/bin/python
from files.storage \
    import storagePageFile

from os.path \
    import isdir

from os \
    import mkdir

from data.store.storage_database \
    import storage_database

from data.store.store_entry \
    import store_entry


root_tmp_path = "/tmp/"
tmp_soft_path = "/garmin-data-storage"

completePath = root_tmp_path + tmp_soft_path

data_structure = None

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
        global data_structure
        init_directory()

        if data_structure == None:
            data_structure = []

        self.__clear_files()
        
        self.load()
        self.database = storage_database()

    def __clear_files( self ):
        pass        

    def exists_key( self, key ):
        if len( self.get_structure() ) == 0:
            return False

        for element in self.get_structure():
            if element.get_key() == str( key ).lower():
                return True

        return False

    def search( self, key ):
        for element in self.get_structure():
            if( element.get_key() ) == str( key ).lower():
                return element
        
        return None


    def build_structure( self, key, value ):
        if self.exists_key( key ):
            element = self.search( key )

            if( element == None ):
                raise Exception( "Element couldn't be found." )

            element.insert_data( value )
        else:
            newElement = store_entry()

            newElement.set_key( key )
            newElement.insert_data( value )

            structure = self.get_structure()
            structure.append( newElement )

            self.set_structure( structure )
        

    def update_structure( self, key, value ):
        pass


    def delete_structure( self, key ):
        pass


    # Setup index
    def load( self ):
        global completePath

    def save( self ):
        pass

    def write( self ):
        pass

    def flush( self ):
        pass

    def get_structure( self ):
        global data_structure
        return data_structure

    def set_structure( self, value ):
        global data_structure
        data_structure = value

    def __cache( self ):
        pass
