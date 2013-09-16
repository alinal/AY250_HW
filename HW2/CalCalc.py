import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store_true', default=False, dest='Unfilled_Histogram',
                    help='True to use an unfilled histogram')

parser.add_argument('-n', action='store',default=10, type=int,  dest='dataN',
                    help='Store a constant value')

parser.add_argument('-T', action='store', default='No Title', dest='title',
                    help='Store a simple value')


results = parser.parse_args()
