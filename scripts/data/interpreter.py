#!/usr/bin/python
from data.keystore \
    import key_store

from fitparse \
    import FitFile, \
           FitParseError


class fit_interpreter:
    def __init__( self, entry ):
        self.entry = entry
        self.store = key_store()
    
    def load_into_memory( self ):
        try:
            debug( self.entry.get_fullPath() )
            fitparsed = FitFile( self.entry.get_fullPath() )
            fitparsed.parse()

            messages = fitparsed.get_messages()

            for message in messages:
                values = message.get_values()

                print(values)

        except FitParseError as e:
            print(e)


def debug( fp ):
    state = 'loading: ' + str( fp )
    print( state )
