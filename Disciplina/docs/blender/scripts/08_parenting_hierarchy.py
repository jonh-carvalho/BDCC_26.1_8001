"""
08_parenting_hierarchy.py
Cria um empty como pai e parentiza o cubo e a primeira esfera (se existirem). Anima o pai.
"""
import bpy

try:
    # Criar empty
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0,0,0))
    parent = bpy.context.active_object
    parent.name = 'Parent_Empty'

    # Garantir existência do cubo
    if 'MeuCubo' not in bpy.data.objects:
        bpy.ops.mesh.primitive_cube_add(size=1, location=(1,0,0))
        bpy.context.active_object.name = 'MeuCubo'

    cube = bpy.data.objects['MeuCubo']
    cube.parent = parent

    # Parentizar primeira esfera, se existir
    sphere = None
    for o in bpy.data.objects:
        if o.name.startswith('Esfera_'):
            sphere = o
            break
    if sphere:
        sphere.parent = parent

    # Animar o parent
    parent.location = (0,0,0)
    parent.keyframe_insert(data_path='location', frame=1)
    parent.location = (0,2,0)
    parent.keyframe_insert(data_path='location', frame=50)

    print('Parent criado, filhos parentizados e animação aplicada ao parent.')
except Exception as e:
    print('Erro:', e)
