"""
07_materials_per_height.py
Cria um material simples e aplica cor baseada na altura (Z) do objeto.
"""
import bpy

try:
    def color_from_z(z, zmin=0.0, zmax=2.0):
        t = (z - zmin) / (zmax - zmin) if zmax > zmin else 0.0
        # gradient from blue -> green -> red
        if t < 0.5:
            # blue to green
            u = t / 0.5
            return (0.0 * (1-u) + 0.0 * u, 0.0 * (1-u) + 1.0 * u, 1.0 * (1-u) + 0.0 * u, 1.0)
        else:
            u = (t - 0.5) / 0.5
            return (0.0 * (1-u) + 1.0 * u, 1.0 * (1-u) + 0.0 * u, 0.0, 1.0)

    objs = [o for o in bpy.data.objects if o.type == 'MESH' and o.name.startswith('Esfera_')]
    if not objs:
        raise RuntimeError("Nenhuma esfera encontrada. Rode 06_generate_spheres.py primeiro.")

    for o in objs:
        z = o.location.z
        rgba = color_from_z(z)
        mat = bpy.data.materials.new(name=f"Mat_{o.name}")
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        if bsdf:
            bsdf.inputs['Base Color'].default_value = rgba
        if o.data.materials:
            o.data.materials[0] = mat
        else:
            o.data.materials.append(mat)

    print(f"Materiais aplicados a {len(objs)} esferas com base na altura.")
except Exception as e:
    print("Erro:", e)
