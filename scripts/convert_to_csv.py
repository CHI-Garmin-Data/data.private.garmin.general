#!/usr/bin/python
from procedures \
    import traverseDataset

from procedures \
    import dataset_iterator

from data \
    import interpreter


def parse( entry ):
    data = interpreter.fit_interpreter( entry )
    data.load_into_memory()
    
    

def main():
    traversal = traverseDataset.dataset()
    traversal.run()

    iterate = dataset_iterator.iterate( traversal )
    iterate.start_at_beginning()
    
    while( iterate.is_to_continue_towards_end() ):
        c = iterate.get_value()

        parse( c )

        iterate.forward()
        

    print( 'task done' )


if __name__ == '__main__':
    main()