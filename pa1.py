#!/usr/bin/env python3

#**********************************************************************
# Copyright (c) 2019
#  Sang-Hoon Kim <sanghoonkim@ajou.ac.kr>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
#**********************************************************************

import sys
from array import array

memory = array('B', [
    # Memory is initialized with random values
    0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77,
    0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff,
    0x62, 0x61, 0x64, 0x61, 0x63, 0x61, 0x66, 0x65,
    0x64, 0x65, 0x61, 0x64, 0x62, 0x65, 0x65, 0x66,
    0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77,
    0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff,
    0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff,
    0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77,
    0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77,
    0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff,
    ] + [ 0 ] * ((1 << 19) - 80)
)

registers = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 2, 3, 4, 5, 6, 7,
    0x10, 0x14, 0x18, 0x1c, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
]


#*************************************************************************
# TODO: Interprete given MIPS instructions with @opcode and @operands
#
#   Assume you input "0 17 18 8 0 32" on the prompt. Then, it is parsed and
# delivered to this function with following argument values;
#
#  @opcode = 0
#  @operands[] = {17, 18, 8, 0, 32, ....},
#  @nr_operands = 5
#
#   @opcode 0 indicates this is an arithmetic operation with function code 32
# (value in operands[4]), which is "add". According to the MIPS reference chart,
# the arguments are in R-format which implies;
#
#  operands[0] = rs = 17
#  operands[1] = rt = 18
#  operands[2] = rd = 8
#  operands[3] = shamt = 0
#
#   Thus, interpreting the instruction adds the values in registers[17] and
# registers[18] and store it into register[8], which is equivalent to
# 0x14 + 0x18 = 0x2c. Thus registers[8] should be changed from 0 to 0x2c.

def process_instruction(opcode, operands):
    yield   # <-- TODO Remove this line while implementing this function

#**************************************************************************
# Simple MIPS interpreter framework
#
#   You may not need to understand what it does nor change below code ;-).
# The only thing you should know is, however, opcode 99 is for special
# operations to inspect the status of the machine.
#
#   If you just input 99 in the prompt, all register values will be dumped;
#
# >> 99
# [00]          0 0x00000000
# [01]          0 0x00000000
# [02]          0 0x00000000
# [03]          0 0x00000000
#    ....
# [31]          0 0x00000000
#
#   Similarly, opcode 99 followed by starting address and length dumps the
# memory contents at the specified location. For example, 99 16 32 implies
# the command to dump 32 bytes of memory contents starting from 0x10 (== 16)
#
# >> 99 16 32
# 00000010:  62 61 64 61    b a d a
# 00000014:  63 61 66 65    c a f e
# 00000018:  64 65 61 64    d e a d
# 0000001c:  62 65 65 66    b e e f
# 00000020:  00 11 22 33      " 3
# 00000024:  44 55 66 77    D U f w
# 00000028:  88 99 aa bb    � � � �
# 0000002c:  cc dd ee ff    � � � �

def __dump_registers():
    for i in range(len(registers)):
        print("[%02d] %10u  0x%08x" % (i, registers[i], registers[i]))

def __dump_memory(addr, length):
    print("%d %x" % (len(memory), len(memory)))
    for i in range(addr, addr + length, 4):
        print("%08x:  %02x %02x %02x %02x    %c %c %c %c" % (i,
            memory[i], memory[i + 1], memory[i + 2], memory[i + 3],
            memory[i], memory[i + 1], memory[i + 2], memory[i + 3] ))

def __run_program():
    print(">> ", end='', flush=True)
    for l in sys.stdin:
        instruction = l.strip().split(" ")

        if len(instruction) == 0:
            break;

        opcode = int(instruction[0])
        operands = [ int(o) for o in instruction[1:] ]

        if opcode == 99:
            if len(operands) == 0:
                __dump_registers()
            else:
                __dump_memory(operands[0], operands[1])
        else:
            process_instruction(opcode, operands);

        print("\n>> ", end='', flush=True)

def main():
    print("*********************************************************")
    print("*            >> ICT331 MIPS interpreter v0.01 <<        *")
    print("*                                                       *")
    print("*                                       .--.            *")
    print("*                           .--------.  |__|            *")
    print("*                           |.------.|  |=.|            *")
    print("*                           || >>_  ||  |--|            *")
    print("*                           |'------'|  |  |            *")
    print("*                           ')______('~~|__|            *")
    print("*                                                       *")
    print("*********************************************************")
    print()

    __run_program();

if __name__ == "__main__":
    main();

