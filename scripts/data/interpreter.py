#!/usr/bin/python
from data.keystore \
    import key_storage_database

from fitparse \
    import FitFile, \
           FitParseError

from data.timestamp16 \
    import T16converter

import automate_consts

import pytz
import datetime


lastTimestamp = None
last16Timestamp = None


class fit_interpreter:
    def __init__( self, entry ):
        self.entry = entry
        self.store = key_storage_database()

    def set_last_timestamp( self, v ):
        global lastTimestamp
        lastTimestamp = v

    def set_last_timestamp_16( self, v ):
        global last16Timestamp
        last16Timestamp = v
    
    def get_last_timestamp( self ):
        global lastTimestamp
        return lastTimestamp

    def get_last_timestamp_16( self ):
        global last16Timestamp
        return last16Timestamp

    def default_timestamp_16( self ):    
        global last16Timestamp
        last16Timestamp = None

    def load_into_memory( self ):
        try:
            debug( self.entry.get_fullPath() )

            fitparsed = FitFile( self.entry.get_fullPath() )
            fitparsed.parse()

            messages = fitparsed.get_messages()

            for message in messages:
                values = message.get_values()

                if automate_consts.const_timestamp in values:
                    t = self.timezone_conversion( datetime.datetime.timestamp( values[ automate_consts.const_timestamp ] ) )
                    self.updateTimestamp( t )
                    self.default_timestamp_16()

                if automate_consts.const_timestamp_16 in values:
                    convertWith = T16converter( self.get_last_timestamp(), values[ automate_consts.const_timestamp_16 ] )
                    converted_from_t16 = convertWith.run()
                    self.updateTimestamp16( converted_from_t16 )


        except FitParseError as e:
            print(e)


    def updateTimestamp( self, t ):
        if self.get_last_timestamp() == None:
            self.set_last_timestamp( t )
            return self.get_last_timestamp()

        if not self.get_last_timestamp() == t:
            self.set_last_timestamp( t )
            #print('T:' + str( self.get_last_timestamp() ) )

        return self.get_last_timestamp()


    def updateTimestamp16( self, t ):
        if self.get_last_timestamp_16() == None:
            self.set_last_timestamp_16( t )
            return self.get_last_timestamp_16()

        if not self.get_last_timestamp_16() == t:
            self.set_last_timestamp_16( t )
            #print('T16:' + str(self.get_last_timestamp_16()))

        return self.get_last_timestamp_16()


    def latest_timestamp( self ):
        if( self.get_last_timestamp() == None ):
            return None

        if( self.get_last_timestamp_16() == None ):
            return self.get_last_timestamp()

        converted_t = self.get_last_timestamp()
        filtered_converted_t = str(converted_t)[0:-6]
        
        t16 = self.get_last_timestamp_16()
        filtered_t16 = str(t16)[0:-6]

        latest = None

        if not filtered_converted_t == filtered_t16:
            latest = filtered_t16
        else:
            latest = filtered_converted_t

        return str( latest )

    def timezone_conversion( self, timestamp_int ):
        return datetime.datetime.fromtimestamp( timestamp_int, pytz.timezone( automate_consts.const_utc_denmark_copenhagen ) )

def debug( fp ):
    state = 'loading: ' + str( fp )
    print( state )
