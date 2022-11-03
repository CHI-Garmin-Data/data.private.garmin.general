#!/usr/bin/python
from procedures \
    import traverseDataset

from procedures \
    import dataset_iterator

import fitparse

def main():

    traversal = traverseDataset.dataset()
    traversal.run()

    iterate = dataset_iterator.iterate( traversal )
    iterate.start_at_beginning()
    
    while( iterate.is_to_continue_towards_end() ):
        c = iterate.get_value()

        print(c.get_fullPath())
        exit()
        

        iterate.forward()
        

    print( 'task done' )


if __name__ == '__main__':
    main()