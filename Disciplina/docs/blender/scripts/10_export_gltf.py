"""
10_export_gltf.py
Exporta os objetos selecionados (ou toda a cena) para um arquivo GLB.
"""
import bpy
import os

try:
    # Caminho de saída (por padrão pasta 'exports' junto ao .blend)
    out_dir = os.path.join(bpy.path.abspath('//'), 'exports')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'minhaCena.glb')

    # Exportar toda a cena
    bpy.ops.export_scene.gltf(filepath=out_path, export_format='GLB')
    print('Exportado glb para:', out_path)
except Exception as e:
    print('Erro:', e)
