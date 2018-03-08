# http://www.codewars.com/kata/simple-assembler-interpreter/python

code1 = '''\
    mov a 5
    inc a
    dec a
    dec a
    jnz a -1
    inc a
'''
code2 = '''\
    mov c 12
    mov b 0
    mov a 200
    dec a
    inc b
    jnz a -2
    dec c
    mov a b
    jnz c -5
    jnz 0 1
    mov c a
'''


def simple_assembler(program):
    reg, i = {}, 0
    while i < len(program):
        cmd, k, v = (program[i] +' 0').split()[:3]
        if cmd == 'inc': reg[k] += 1
        if cmd == 'dec': reg[k] -= 1
        if cmd == 'mov': reg[k] = reg[v] if v in reg else int(v)
        if cmd == 'jnz' and (reg[k] if k in reg else int(k)):
            i += int(v) - 1
        i += 1
    return reg

import datetime
start = datetime.datetime.now()
r1 = simple_assembler(code1.splitlines())
print (datetime.datetime.now()-start)
assert r1 == {'a': 1}
start = datetime.datetime.now()
r2 = simple_assembler(code2.splitlines())
print (datetime.datetime.now()-start)
assert r2 ==  {'a': 409600, 'c': 409600, 'b': 409600}
code3 = ['mov a 1', 'mov b 1', 'mov c 0', 'mov d 26', 'jnz c 2', 'jnz 1 5', 'mov c 7', 'inc d', 'dec c', 'jnz c -2', 'mov c a', 'inc a', 'dec b', 'jnz b -2', 'mov b c', 'dec d', 'jnz d -6', 'mov c 18', 'mov d 11', 'inc a', 'dec d', 'jnz d -2', 'dec c', 'jnz c -5']
r3 = simple_assembler(code3)
print r3
assert r3 == {'a': 318009, 'b': 196418, 'c': 0, 'd': 0}
