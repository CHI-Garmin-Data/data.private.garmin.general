#!/usr/bin/python
from procedures \
    import traverseDataset

from procedures \
    import dataset_iterator


def main():
    traversal = traverseDataset.dataset()
    traversal.run()

    iterate = dataset_iterator.iterate( traversal )
    iterate.start_at_beginning()
    
    while( iterate.is_to_continue_towards_end() ):
        e = iterate.get_value()

        iterate.forward()
        

    print( 'task done' )


if __name__ == '__main__':
    main()