#!/usr/bin/env python3

from subprocess import run, Popen


def combine(parts, final):
    code = 'import bpy;'
    for part in parts:
        code += "bpy.ops.import_mesh.stl(filepath='%s');" % part
    code += "bpy.ops.export_mesh.stl(filepath='%s');" % final
    run(['/opt/blender/blender', '--background', '--python-expr', code])


parts = ['/opt/kids3d/head.stl', '/opt/kids3d/body.stl', '/opt/kids3d/legs.stl']
final = '/opt/kids3d/custom.stl'
combine(parts, final)
