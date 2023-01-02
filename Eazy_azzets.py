bl_info = {
	"name":"Eazy Azzets",
	"author": "Yam K.",
	"version": (0,2),
	"blender": (2,80,0),
	"location": "",
	"Description": "Making asset browser for GTA 5 Easier",
	"warning": "",
	"category": "Yam K."
}

import bpy

def eazy_azzets():
    
    objects = bpy.context.scene.objects
    
    for obj in objects:
        if obj.name.endswith('.#dr'):
         obj.parent = None
         obj.name = obj.name[:-4]
         obj.asset_mark()
         obj.asset_generate_preview()
        if not obj.asset_data:
         bpy.data.objects.remove(obj)
           
    
    num_rows = num_columns = int(len(objects) ** 0.5)

    total_dimensions = [sum(obj.dimensions[axis] for obj in objects) for axis in range(2)]

    margin = 1  

    total_margin = [(num_columns - 1) * margin, (num_rows - 1) * margin]

    total_dimensions = [total_dimensions[axis] + total_margin[axis] for axis in range(2)]

    center = [total_dimensions[axis] / 2 for axis in range(2)]

    current_position = [center[0] - (total_dimensions[0] / 2), center[1] - (total_dimensions[1] / 2)]

    for i, obj in enumerate(objects):
        obj.location.x = current_position[0] + obj.dimensions.x / 2
        obj.location.y = current_position[1] + obj.dimensions.y / 2

        current_position[0] += obj.dimensions.x + margin
        if (i + 1) % num_columns == 0:
            current_position[0] = center[0] - (total_dimensions[0] / 2)
            current_position[1] += obj.dimensions.y + margin

class DoItButton(bpy.types.Operator):
    """Run the Eazy Azzets script"""
    bl_idname = "object.eazy_azzets"
    bl_label = "Do It ! Just do it !"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        eazy_azzets()
        return {'FINISHED'}
        
class EazyAzzetsPanel(bpy.types.Panel):
    """Eazy Azzets panel"""
    bl_label = "Eazy Azzets"
    bl_idname = "OBJECT_PT_eazy_azzets"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Eazy Azzets"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.eazy_azzets")
        
def register():
    bpy.utils.register_class(DoItButton)
    bpy.utils.register_class(EazyAzzetsPanel)

def unregister():
    bpy.utils.unregister_class(DoItButton)
    bpy.utils.unregister_class(EazyAzzetsPanel)

if __name__ == "__main__":
    register()        




















