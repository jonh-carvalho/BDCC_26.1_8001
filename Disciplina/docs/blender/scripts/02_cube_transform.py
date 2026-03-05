"""
02_cube_transform.py
Cria um cubo e aplica translação, rotação e escala.
"""
import bpy
import math

try:
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
    obj = bpy.context.active_object
    obj.name = "MeuCubo"

    # Aplicar transformações
    obj.location = (1.0, 2.0, 0.5)
    obj.rotation_euler = (0.0, 0.0, math.radians(45.0))
    obj.scale = (1.0, 2.0, 0.5)

    print(f"Criado {obj.name} em {obj.location}, rot={tuple(map(math.degrees, obj.rotation_euler))}, scale={obj.scale}")
except Exception as e:
    print("Erro:", e)
