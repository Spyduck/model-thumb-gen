# --python thumbnailer.py -- path.obj
import sys, bpy, os.path
path = sys.argv[sys.argv.index("--") + 1:][0]
#path = "Z:\\Projects\\palette\\potato_box.obj"
print('=========')
print(path)
ext = os.path.splitext(path)[1][1:]
if ext == 'obj':
	# load obj
	bpy.ops.import_scene.obj(filepath=path) #, filter_glob="*.obj;*.mtl", use_smooth_groups=True, use_split_objects=True, use_split_groups=True, use_groups_as_vgroups=False, use_image_search=True, split_mode='ON', global_clamp_size=0, axis_forward='-Z', axis_up='Y')
elif ext == 'dae':
	# dae
	bpy.ops.wm.collada_import(filepath=path)
# align active camera to selected
bpy.ops.view3d.camera_to_view_selected()