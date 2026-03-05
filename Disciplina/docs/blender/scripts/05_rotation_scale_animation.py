"""
05_rotation_scale_animation.py
Adiciona animação de rotação e escala ao cubo.
"""
import bpy
import math

try:
    name = "MeuCubo"
    if name not in bpy.data.objects:
        bpy.ops.mesh.primitive_cube_add(size=1, location=(0,0,0))
        bpy.context.active_object.name = name

    obj = bpy.data.objects[name]

    # Rotação: frame 1 = 0, frame 50 = 360 graus em Z
    obj.rotation_euler = (0.0, 0.0, 0.0)
    obj.keyframe_insert(data_path="rotation_euler", frame=1)

    obj.rotation_euler = (0.0, 0.0, math.radians(360.0))
    obj.keyframe_insert(data_path="rotation_euler", frame=50)

    # Escala: frame 1 = 1, frame 50 = 0.1 (sumir)
    obj.scale = (1.0, 1.0, 1.0)
    obj.keyframe_insert(data_path="scale", frame=1)

    obj.scale = (0.1, 0.1, 0.1)
    obj.keyframe_insert(data_path="scale", frame=50)

    print("Animação de rotação e escala adicionada a MeuCubo.")
except Exception as e:
    print("Erro:", e)
