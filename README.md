ICT331 2019 Spring Programming Assignment #1

* Goal: Implement a simple MIPS interpreter.

* Description:
  - Provided code defines a bare MIPS machine with 32 32-bit registers(`registers[0]` -- `registers[31]`) and 512~KB memory (`memory[0]`--`memory[0x79999]`).

  - The input is space-separated decimal numbers encoding the fields of MIPS instructions. For example, a input string "0 17 18 8 0 32" means an MIPS instruction with opcode 0 and 5 operands, which implies it is in R-format. Therefore, each field of the instruction is;
		```
		- opcode: 0, funct: 32 (add)
		- rs: 17
		- rt: 18
		- rd: 8
		- shamt: 0
		```
  - Thus, your interpreter should add values in register 17 and 18, which is 0x14 and 0x18 initially, and store the result (0x2c) into register 8.

  - The interpreter should be able to process following operations for full points. Note the number in /* */ indicates the opcode (and funct).
		```
		- ADD,  /* 0 0x20 */
		- ADDI, /* 0x08   */
		- SUB,  /* 0 0x22 */
		- LW,   /* 0x23   */
		- SW,   /* 0x2b   */
		- SLL,  /* 0 0x00 */
		- SLR,  /* 0 0x02 */
		- SRA,  /* 0 0x03 */
		- AND,  /* 0 0x21 */
		- ANDI, /* 0x0c   */
		- OR,   /* 0 0x25 */
		- ORI,  /* 0x0d   */
		- NOR,  /* 0 0x27 */
		```

  - Good news; error handling will not be tested. (i.e., assume all inputs are given correctly complying the MIPS specification)


* Submit:
	- Source code: *C or Python source file renamed to your student ID number* (Either C or Python works for your submission).

	- Report: One-page *PDF* document describing your system design and implementation. Don't spend much of your time making it pretty but clearly describe your key ideas in implementation.


* Due: April 12, 11:59pm
	- Submit them into AjouBb.
