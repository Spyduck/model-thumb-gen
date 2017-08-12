#!/usr/bin/env python3


# edit this line to point to blender binary
#  example:
#  blender_dir = r"C:\Program Files\Blender Foundation\Blender\blender.exe"
blender_dir = r"C:\Program Files\Blender Foundation\Blender\blender.exe"


import os
import sys
import subprocess

script_dir = os.path.dirname(os.path.realpath(__file__))

def render_dir(rootdir):
	for root, subFolders, files in os.walk(rootdir):
		for file in files:
			if file.endswith('.obj') or file.endswith('.dae'):
				render_model(os.path.join(root,file))
def render_model(modeldir):
	outdir = os.path.dirname(modeldir)
	filename = os.path.splitext(os.path.basename(modeldir))[0]
	extension = os.path.splitext(modeldir)[1]
	try:
		os.remove(os.path.join(outdir, 'thumb_'+filename+'.png'))
	except:
		pass
	subprocess.run([blender_dir, '-b', os.path.join(script_dir,'thumbnailer.blend'), '--python', 'thumbnailer.py' ,'-o', os.path.join(outdir, 'thumb_'+filename), '-f', '0', '--', modeldir], shell=True, cwd=script_dir)
	try:
		print(os.path.join(outdir, 'thumb_'+filename+'0000.png'))
		os.rename(os.path.join(outdir, 'thumb_'+filename+'0000.png'), os.path.join(outdir, 'thumb_'+filename+'.png'))
	except:
		pass
loaded = True
try:
	arg = sys.argv[1]
except:
	loaded = False
	arg = ''
if os.path.isfile(arg) and (arg.endswith('.obj') or arg.endswith('.dae')):
	render_model(arg)
elif os.path.isdir(arg):
	render_dir(arg)
else:
	loaded = False
if not loaded:
	print(arg)
	print('First argument should be a folder or model (.obj or .dae)')
	print('Press enter to exit')
	input()