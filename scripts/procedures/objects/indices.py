#!/usr/bin/python

class index_entry:
    def __init__( self ):
        self.start_position = None
        self.key = None
    
    def get_start_position( self ):
        return int( self.start_position )

    def set_start_position( self, v ):
        self.start_position = int( v )

    def get_key( self ):
        return str( self.key )

    def set_key( self, v ):
        self.key = str( v )

    def compare(self, wValue):
        return str(self.key) == str(wValue)


    def __str__(self):
        rV = ''

        rV = rV + 'Start_position:' + str(self.get_start_position()) + '\r\n'
        rV = rV + 'Key:' + str(self.get_key()) + '\r\n'

        return str(rV)