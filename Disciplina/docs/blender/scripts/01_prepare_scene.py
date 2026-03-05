"""
01_prepare_scene.py
Limpa a cena (restaura cena vazia) para iniciar os exercícios.
Execute dentro do Blender (Scripting) ou via CLI:
"C:\\Program Files\\Blender Foundation\\Blender 4.5\\blender.exe" --background --python "01_prepare_scene.py"
"""
import bpy

try:
    # Restaura configurações de fábrica com cena vazia
    bpy.ops.wm.read_factory_settings(use_empty=True)
    print("Cena limpa e pronta para exercícios.")
except Exception as e:
    print("Erro ao limpar cena:", e)
