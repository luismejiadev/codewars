#https://www.codewars.com/kata/assembler-interpreter-part-ii/train/python

import shlex

def assembler_interpreter(program, debug=False, break_point=30):
    program = program.splitlines()
    comment_indicator = ";"
    ret_pointers = []
    cmp_result = None
    reg, labels = {}, {}
    get_value = lambda v:  reg[v] if v in reg else int(v)
    program_lines = []
    labels = {line[:-1]: i for i, line in enumerate(program) if line.endswith(":")}

    i = 0
    while i < len(program):
        line = program[i].strip()
        if debug:
            print "###"
            print reg
            print line
            if break_point <= 0:
                break
            else:
                break_point -= 1

        cmd = line
        if not line or line[0] == comment_indicator:
            i += 1
            continue
        if line.endswith(":"):
            i += 1
            labels[line[:-1]] = i
            continue
        elif line == 'ret':
            current_label, i = ret_pointers.pop()
            i += 1
            continue
        CS = line.find(comment_indicator)
        cmd = line[:CS] if CS > -1 else line
        FS = cmd.find(" ")
        if FS > -1:
            args = (cmd[FS + 1:]).strip().split(",")
            cmd = cmd[:FS]
        if cmd == 'end':
            return output
        elif cmd == 'msg':
            line = line[FS+1:CS] if CS > -1 else line[FS+1:]
            args = map(
                lambda x: x[:-1] if x[-1] == "," else x,
                shlex.split(line)
            )
            output = "".join(map(
                lambda v:  str(get_value(v)) if v in reg else v,
                args
            ))
            i += 1
            continue
        k = args[0].strip()
        if len(args) > 1:
            v = args[1].strip()

        if cmd == 'inc': reg[k] += 1
        elif cmd == 'dec': reg[k] -= 1
        elif cmd == 'add': reg[k] += get_value(v)
        elif cmd == 'sub': reg[k] -= get_value(v)
        elif cmd == 'mul': reg[k] *= get_value(v)
        elif cmd == 'div': reg[k] /= get_value(v)
        elif cmd == 'mov': reg[k] = get_value(v)
        elif cmd == 'cmp': cmp_result = float(get_value(k) + 1) / (get_value(v) + 1)
        elif cmd == 'jnz' and (reg[k] if k in reg else int(k)): i += int(v) - 1
        elif cmd == 'call': ret_pointers.append((k, i)); i = labels[k]
        else:
            jump = False
            if cmd == "jmp":                     jump = True
            elif cmd == 'jne' and cmp_result != 1: jump = True
            elif cmd == 'je' and cmp_result == 1:  jump = True
            elif cmd == 'jge' and cmp_result >= 1: jump = True
            elif cmd == 'jg' and cmp_result > 1:   jump = True
            elif cmd == 'jle' and cmp_result <= 1: jump = True
            elif cmd == 'jl' and cmp_result < 1:   jump = True
            if jump:
                i = labels[k]
        i += 1
    return -1

"""
We want to create an interpreter of assembler which will support the following instructions:
mov x, y - copy y (either an integer or the value of a register) into register x.
inc x - increase the content of register x by one.
dec x - decrease the content of register x by one.
add x, y - add the content of the register x with y (either an integer or the value of a register) and stores the result in x (i.e. register[x] += y).
sub x, y - subtract y (either an integer or the value of a register) from the register x and stores the result in x (i.e. register[x] -= y).
mul x, y - same mith multiply (i.e. register[x] *= y).
div x, y - same with integer division (i.e. register[x] /= y).
label: - define a label position (label = identifier + ":", an identifier being a string that does not match any other command). Jump commands and call are aimed to these labels positions in the program.
jmp lbl - jumps to to the label lbl.

cmp x, y - compares x (either an integer or the value of a register) and y (either an integer or the value of a register). The result is used in the conditional jumps (jne, je, jge, jg, jle and jl)
jne lbl - jump to the label lbl if the values of the previous cmp command were not equal.
je lbl - jump to the label lbl if the values of the previous cmp command were equal.
jge lbl - jump to the label lbl if x was greater or equal than y in the previous cmp command.
jg lbl - jump to the label lbl if x was greater than y in the previous cmp command.
jle lbl - jump to the label lbl if x was less or equal than y in the previous cmp command.
jl lbl - jump to the label lbl if x was less than y in the previous cmp command.

call lbl - call to the subroutine identified by lbl. When a ret is found in a subroutine, the instruction pointer should return to the instruction next to this call command.
ret - when a ret is found in a subroutine, the instruction pointer should return to the instruction that called the current function.
msg 'Register: ', x - this instruction stores the output of the program. It may contain text strings (delimited by single quotes) and registers. The number of arguments isn't limited and will vary, depending on the program.
end - this instruction indicates that the program ends correctly, so the stored output is returned (if the program terminates without this instruction it should return the default output: see below).
; comment - comments should not be taken in consideration during the execution of the program.

"""

program = """
; My first program
mov  a, 5
inc  a
call function
msg  '(5+1)/2 = ', a    ; output message
end

function:
    div  a, 2
    ret
"""
r = assembler_interpreter(program)
print r
assert r == '(5+1)/2 = 3'


program2 = """
mov   a, 5
mov   b, a
mov   c, a
call  proc_fact
call  print
end

proc_fact:
    dec   b
    mul   c, b
    cmp   b, 1
    jne   proc_fact
    ret

print:
    msg   a, '! = ', c ; output text
    ret
"""
r = assembler_interpreter(program2)
print r
assert r == '5! = 120'

program3 = """
mov   a, 8            ; value
mov   b, 0            ; next
mov   c, 0            ; counter
mov   d, 0            ; first
mov   e, 1            ; second
call  proc_fib
call  print
end

proc_fib:
    cmp   c, 2
    jl    func_0
    mov   b, d
    add   b, e
    mov   d, e
    mov   e, b
    inc   c
    cmp   c, a
    jle   proc_fib
    ret

func_0:
    mov   b, c
    inc   c
    jmp   proc_fib

print:
    msg   'Term ', a, ' of Fibonacci series is: ', b        ; output text
    ret
"""
r = assembler_interpreter(program3)
print r
assert r == 'Term 8 of Fibonacci series is: 21'


program4 = """
mov   a, 11           ; value1
mov   b, 3            ; value2
call  mod_func
msg   'mod(', a, ', ', b, ') = ', d        ; output
end

; Mod function
mod_func:
    mov   c, a        ; temp1
    div   c, b
    mul   c, b
    mov   d, a        ; temp2
    sub   d, c
    ret
"""
r = assembler_interpreter(program4)
print r
assert r == 'mod(11, 3) = 2'


program5 = """
call  func1
call  print
end

func1:
    call  func2
    ret

func2:
    ret

print:
    msg 'This program should return -1'
"""

r = assembler_interpreter(program5, debug=False)
print r
assert r == -1

program6 = """
mov   a, 2            ; value1
mov   b, 10           ; value2
mov   c, a            ; temp1
mov   d, b            ; temp2
call  proc_func
call  print
end

proc_func:
    cmp   d, 1
    je    continue
    mul   c, a
    dec   d
    call  proc_func

continue:
    ret

print:
    msg a, '^', b, ' = ', c
    ret
"""
r = assembler_interpreter(program6, debug=False, break_point=200)
print r
assert r == "2^10 = 1024"
