#!/usr/bin/env python3


from subprocess import run, Popen


test = run(['/opt/blender/blender', '--background', '--python', 'hello.py'])
print(test)
