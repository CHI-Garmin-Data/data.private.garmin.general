#!/usr/bin/python
from files.storage \
    import storagePageFile

class store_entry:
    def __init__( self ):
        self.file_path = None

        self.key = None
        self.data = None

    def get_data( self ):
        self.init_data()

        if isinstance( self.data, dict ):
            return self.data
        else:
            return None

    def set_data( self, data ):
        if isinstance( data, dict ):
            self.data = data

    def size_of_data( self ):
        return len( self.data )

    def insert_data( self, data ):
        self.init_data()
        self.data[ str( self.size_of_data() ) ] = data

    def get_key( self ):
        return str( self.key )

    def set_key( self, value ):
        self.key = str( value ).lower()


    def get_file_path( self ):
        return self.file_path

    def set_file_path( self, path ):
        self.file_path = path


    def init_data( self ):
        if self.data == None:
            self.data = {}

    def __str__( self ):
        r = 'key: ' + str( self.key )
        r = r + '\r\n'

        r = r + 'data: ' + str( self.data )
        r = r + '\r\n'

        return r
