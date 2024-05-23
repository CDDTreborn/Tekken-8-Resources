import bpy

# Ensure exactly two objects are selected
if len(bpy.context.selected_objects) != 2:
    print("Please select exactly two objects.")
else:
    # Get the active object (the one to duplicate) and the other selected object
    active_obj = bpy.context.view_layer.objects.active
    selected_objs = bpy.context.selected_objects
    selected_obj = selected_objs[0] if selected_objs[1] == active_obj else selected_objs[1]

    # Rename the selected object to have "_src" as the suffix
    selected_obj.name = selected_obj.name + "_src"

    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Select only the active object
    active_obj.select_set(True)

    # Duplicate the active object
    bpy.ops.object.duplicate(linked=False)
    duplicated_obj = bpy.context.view_layer.objects.active

    # Rename the duplicated object to have "_dup" as the suffix
    duplicated_obj.name = active_obj.name + "_dup"

    # Print the names of the objects for verification
    print(f"Active object renamed to: {active_obj.name}")
    print(f"Selected object renamed to: {selected_obj.name}")
    print(f"Duplicated object created with name: {duplicated_obj.name}")


# Function to find objects by suffix in the scene
def find_object_by_suffix(suffix):
    for obj in bpy.data.objects:
        if obj.name.endswith(suffix):
            return obj
    return None

# Find the objects with suffixes "_dup" and "_src"
dup_obj = find_object_by_suffix("_dup")
src_obj = find_object_by_suffix("_src")

if not dup_obj:
    print("No object ending with '_dup' found.")
elif not src_obj:
    print("No object ending with '_src' found.")
else:
    # Remove vertex groups from the "_dup" object
    bpy.context.view_layer.objects.active = dup_obj
    bpy.ops.object.vertex_group_remove(all=True)

    # Transfer vertex groups (weights) from the "_src" object to the "_dup" object
    bpy.ops.object.modifier_add(type='DATA_TRANSFER')
    mod = dup_obj.modifiers[-1]
    mod.object = src_obj
    mod.use_vert_data = True
    mod.data_types_verts = {'VGROUP_WEIGHTS'}
    mod.vert_mapping = 'NEAREST'
    mod.mix_mode = 'REPLACE'
    mod.mix_factor = 1.0
    # mod.vertex_group_match = 'NAME'

    # Apply the data transfer modifier
    bpy.ops.object.datalayout_transfer(modifier=mod.name)
    bpy.ops.object.modifier_apply(modifier=mod.name)

    # Rename the duplicated object to end with "_prpNew"
    new_name = dup_obj.name.replace("_dup", "_prpNew")
    dup_obj.name = new_name

    # Unparent the "_prpNew" object from its current parent
    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

    # Parent the "_prpNew" object to the armature of the "_src" object
    armature = src_obj.find_armature()
    if armature:
        dup_obj.select_set(True)
        bpy.context.view_layer.objects.active = armature
        bpy.ops.object.parent_set(type='ARMATURE', keep_transform=True)
    else:
        print(f"No armature found for the object '{src_obj.name}'")

    # Print completion message
    print(f"Transferred weights from '{src_obj.name}' to '{new_name}'.")
    print(f"Renamed duplicated object to: {new_name}")
    if armature:
        print(f"Parented '{new_name}' to the armature '{armature.name}'.")
    else:
        print(f"Failed to parent '{new_name}' as no armature was found.")



