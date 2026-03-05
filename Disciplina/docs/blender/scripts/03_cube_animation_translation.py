"""
03_cube_animation_translation.py
Insere keyframes para translação do cubo (frame 1 -> frame 50).
"""
import bpy

try:
    # Garantir que existe o cubo; caso negativo, criar
    if "MeuCubo" not in bpy.data.objects:
        bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
        bpy.context.active_object.name = "MeuCubo"

    obj = bpy.data.objects["MeuCubo"]

    # Frame range
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 50

    # Inserir keyframes de location
    obj.location.x = -2.0
    obj.keyframe_insert(data_path="location", frame=1)

    obj.location.x = 2.0
    obj.keyframe_insert(data_path="location", frame=50)

    print("Keyframes de translação inseridos em MeuCubo (frames 1 e 50).")
except Exception as e:
    print("Erro:", e)
