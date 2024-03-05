#!/usr/bin/python

class storage_index:
    def __init__( self ):
        self.loaded = False
        
    def get_loaded( self ):
        return bool( self.loaded )

    def set_loaded( self, value ):
        self.loaded = bool( value )