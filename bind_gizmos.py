bl_info = {
    "name": "Bind Gizmos",
    "author": "MrWheatley",
    "version": (1, 0),
    "blender": (2, 83, 3),
    "description": "Allows you to bind a key to cycle between gizmos or bind them to something like QWE",
    "tracker_url": "",
    "category": "Interface"}


import bpy


class ToggleGizmosRotLoc(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cycle_gizmos_rotloc"
    bl_label = "Cycle Gizmos Rotation Location"

    def execute(self, context):
        gizmo = bpy.context.space_data
        
        if gizmo.show_gizmo_object_rotate == False:
            gizmo.show_gizmo_object_rotate = True
            gizmo.show_gizmo_object_translate = False
            gizmo.show_gizmo_object_scale = False
        else:
            gizmo.show_gizmo_object_rotate = False
            gizmo.show_gizmo_object_translate = True
            gizmo.show_gizmo_object_scale = False
        return {'FINISHED'}
    
class ToggleGizmosRotLocScale(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cycle_gizmos_rotlocscale"
    bl_label = "Cycle Gizmos Rotation Location Scale"

    def execute(self, context):
        gizmo = bpy.context.space_data
        
        if gizmo.show_gizmo_object_rotate == False:
            if  gizmo.show_gizmo_object_translate == True: 
                    gizmo.show_gizmo_object_rotate = False
                    gizmo.show_gizmo_object_translate = False
                    gizmo.show_gizmo_object_scale = True
            else:
                gizmo.show_gizmo_object_rotate = True
                gizmo.show_gizmo_object_translate = False
                gizmo.show_gizmo_object_scale = False
        elif gizmo.show_gizmo_object_translate == False:
            gizmo.show_gizmo_object_rotate = False
            gizmo.show_gizmo_object_translate = True
            gizmo.show_gizmo_object_scale = False
        return {'FINISHED'}
    
class ToggleGizmosRot(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.toggle_gizmos_rot"
    bl_label = "Toggle Gizmos Rotation"

    def execute(self, context):
        gizmo = bpy.context.space_data
        
        if gizmo.show_gizmo_object_rotate == False:
            gizmo.show_gizmo_object_rotate = True
            gizmo.show_gizmo_object_translate = False
            gizmo.show_gizmo_object_scale = False
        else:
            gizmo.show_gizmo_object_rotate = False
            gizmo.show_gizmo_object_translate = False
            gizmo.show_gizmo_object_scale = False
        return {'FINISHED'}
    
class ToggleGizmosLoc(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.toggle_gizmos_loc"
    bl_label = "Toggle Gizmos Translate"

    def execute(self, context):
        gizmo = bpy.context.space_data
        
        if gizmo.show_gizmo_object_translate == False:
            gizmo.show_gizmo_object_translate = True
            gizmo.show_gizmo_object_rotate = False
            gizmo.show_gizmo_object_scale = False
        else:
            gizmo.show_gizmo_object_rotate = False
            gizmo.show_gizmo_object_translate = False
            gizmo.show_gizmo_object_scale = False
        return {'FINISHED'}    
    
class ToggleGizmosScale(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.toggle_gizmos_scale"
    bl_label = "Toggle Gizmos Scale"

    def execute(self, context):
        gizmo = bpy.context.space_data
        
        if gizmo.show_gizmo_object_scale == False:
            gizmo.show_gizmo_object_scale = True
            gizmo.show_gizmo_object_rotate = False
            gizmo.show_gizmo_object_translate = False
        else:
            gizmo.show_gizmo_object_rotate = False
            gizmo.show_gizmo_object_translate = False
            gizmo.show_gizmo_object_scale = False
        return {'FINISHED'}  

class ToggleGizmosClear(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cycle_gizmos_clear"
    bl_label = "Clear Gizmos"

    def execute(self, context):
        gizmo = bpy.context.space_data

        gizmo.show_gizmo_object_rotate = False
        gizmo.show_gizmo_object_translate = False
        gizmo.show_gizmo_object_scale = False
        return {'FINISHED'}


classes = [
    ToggleGizmosRotLoc,
    ToggleGizmosRotLocScale,
    ToggleGizmosRot,
    ToggleGizmosLoc,
    ToggleGizmosScale,
    ToggleGizmosClear
]


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
    