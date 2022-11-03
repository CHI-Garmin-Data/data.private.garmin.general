#!/usr/bin/python
import ntpath


def generate_entry( rootOfDataset, foundFile ):
    entry = entry_found()
    entry.set_fullPath( foundFile )

    lengthOfRoot = len( rootOfDataset )
    filename = ntpath.basename( foundFile )
    file_len = len( filename )

    rest_date = foundFile[1 + lengthOfRoot:(-file_len - 1)]

    if "/" in rest_date:
        rest_date = rest_date.replace ("/", ":" )
    
    if "\\" in rest_date:
        rest_date.replace( "\\", ":" )

    entry.set_date( rest_date )
    
    return entry


class entry_found:
    def __init__( self ):
        self.fullPath = None
        self.date = None

    def set_fullPath( self, value ):
        self.fullPath = str( value )

    def get_fullPath( self ):
        return str( self.fullPath )

    def __str__get_full_path( self ):
        if self.get_fullPath() == None:
            return str( 'Empty' )

        return str( self.get_fullPath() )


    def get_date( self ):
        return self.date

    def set_date( self, v ):
        self.date = v

    def __str__get_date( self ):
        if self.get_date() == None:
            return 'Empty'

        return str( self.get_date() )

    def __str__( self ):
        value = None

        value = self.__append_to_string( value, "fullpath = " )
        value = self.__append_to_string( value, self.__str__get_full_path() )

        value = self.__append_space( value )

        value = self.__append_to_string( value, "dor = " )
        value = self.__append_to_string( value, self.__str__get_date() )


        return value
    
    def __append_to_string( self, a, b ):
        start = a

        if start == None:
            start = str( '' )

        return str( start + b )


    def __append_space( self, value ):
        return str( str( value ) + "\r\n" )