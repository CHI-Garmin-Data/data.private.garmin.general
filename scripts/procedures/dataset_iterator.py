#!/usr/bin/python
class iterate:
    def __init__( self, traversal ):
        self.traversal = traversal

        self.position = None
        self.length = None


    def get_value( self ):
        return self.traversal.get_found()[ self.position ]


    def forward( self ):
        self.position = self.position + 1

    def backward( self ):
        self.position = self.position - 1


    def start_at_beginning( self ):
        self.position = 0
        self.length = self.traversal.size()

    def start_at_end( self ):
        self.length = self.traversal.size()
        self.position = self.length


    def is_none( self ):
        return self.position == None


    def is_to_continue_towards_end( self ):
        return int( self.position ) < int( self.length )
    
    def is_to_continue_towards_beginning( self ):
        return int( self.position ) > int( 0 )


    def get_length( self ):
        return int( self.length )

    def set_length( self, v ):
        self.length = int( v )



    def get_position( self ):
        return int( self.position )

    def set_position( self, v ):
        self.position = int(v)

