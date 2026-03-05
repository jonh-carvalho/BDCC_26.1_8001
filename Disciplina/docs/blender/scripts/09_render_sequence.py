"""
09_render_sequence.py
Configura render e renderiza a animação. Altere scene.render.filepath conforme desejado.
"""
import bpy
import os

try:
    scene = bpy.context.scene
    scene.render.engine = 'BLENDER_EEVEE'

    # Pasta de saída (relativa ao blend) - aqui usamos pasta 'renders' ao lado do .blend
    out_dir = os.path.join(bpy.path.abspath('//'), 'renders')
    os.makedirs(out_dir, exist_ok=True)
    scene.render.filepath = os.path.join(out_dir, 'frame_')
    scene.render.image_settings.file_format = 'PNG'

    print('Iniciando render da animação para:', scene.render.filepath)
    bpy.ops.render.render(animation=True)
    print('Render finalizado.')
except Exception as e:
    print('Erro:', e)
