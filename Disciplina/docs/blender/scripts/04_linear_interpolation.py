"""
04_linear_interpolation.py
Altera a interpolação dos keyframes do objeto para LINEAR.
"""
import bpy

try:
    obj_name = "MeuCubo"
    if obj_name not in bpy.data.objects:
        raise RuntimeError(f"Objeto '{obj_name}' não encontrado. Execute 02/03 primeiro.")

    obj = bpy.data.objects[obj_name]
    if not obj.animation_data or not obj.animation_data.action:
        raise RuntimeError("Objeto não possui animação (action).")

    action = obj.animation_data.action
    for fcurve in action.fcurves:
        for kp in fcurve.keyframe_points:
            kp.interpolation = 'LINEAR'

    print("Interpolação das keyframes definida para LINEAR.")
except Exception as e:
    print("Erro:", e)
