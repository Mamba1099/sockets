#calculate the volume of a cone given RADIUS and HEIGHT
#volume of a cone = 1/3 * (math.pi) * radius**2 *HEIGHT

import math
import argparse

parser = argparse.ArgumentParser( description="Calculate the Volume of a cone")
parser.add_argument('-r', '--Radius', type=int, metavar='', required=True, help='radius of the cone')
parser.add_argument('-H', '--height', type=int, metavar='', required=True, help='height of the cone')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet' )
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args()

def volume_cone(Radius, height):
    volume = 1/3 * (math.pi) * (Radius**2) * height
    return volume

if __name__ == '__main__':
    volume = (volume_cone(args.Radius, args.height))
    if args.quiet:
        print (volume)
    elif args.verbose:
        print('Volume of the cone with Radius %s and height %s is %s ' % (args.Radius, args.height, volume))
    else:
       print('volume of the cone = %s'%volume)
    
