import datetime
import pytz


class T16converter:
    def __init__( self, latestTimestamp, timestamp16 ):
        self.latestTimestamp = latestTimestamp
        self.timestamp16 = timestamp16

    def run(self):
        timestamp = int( datetime.datetime.timestamp( self.latestTimestamp ) ) - 631065600
        tmpV = timestamp
        tmpV += ( self.timestamp16 - ( tmpV & 0xFFFF ) ) & 0xFFFF

        return datetime.datetime.fromtimestamp( ( tmpV + 631065600 ), pytz.timezone( 'Europe/Copenhagen' ) )
