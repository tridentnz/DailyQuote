### Terminal Quotes

#### Prolog
Hello. I wanted to create a quote serving program written in python!
I want to be able to pass an argument to my program to tell what kind of quote I want to see.
For example, ```python ./quote.py matrix``` This example would serve a quote from the matrix movie.
`
Day 1: 

Parsing arguments into a python script via the command line.

One solution was for me to use the ***sys*** library which enables us to grab command line arguments
but there is one issue. This method only allows for arguments to be arbitrarily index
and doesn't have named arguments.

For example, ```python ./script.py arg1 arg2 arg3 ```
arg1 will be argv[1] arg2 will be argv[2], etc

The arguments are numbered based on position NOTE: segway to argparse.


