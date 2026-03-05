"""
06_generate_spheres.py
Gera 50 esferas distribuídas aleatoriamente dentro de uma caixa.
"""
import bpy
import random

try:
    bpy.ops.wm.read_factory_settings(use_empty=True)
    n = 50
    for i in range(n):
        x = random.uniform(-2.0, 2.0)
        y = random.uniform(-2.0, 2.0)
        z = random.uniform(0.0, 2.0)
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.08, location=(x, y, z))
        s = bpy.context.active_object
        s.name = f"Esfera_{i:03d}"
    print(f"Geradas {n} esferas na cena.")
except Exception as e:
    print("Erro:", e)
