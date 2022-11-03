#!/usr/bin/python
from procedures \
    import traverseDataset


def main():
    traversal = traverseDataset.dataset()
    traversal.run()

    print( 'task done' )


if __name__ == '__main__':
    main()