# author: Ajwahir
# Engineering Design Department
# IIT Madras
# email: ajwahir@gmail.com

# Generation of depth views

# exec(open("/home/raman/Classification/views_images/blender_views.py").read())

import bpy
import os
import math
import numpy as np
import glob
import time
from math import radians


from os import listdir
from os.path import isfile, join

context = bpy.context

models_path = "/home/raman/Classification/Images"
models = sorted(glob.glob(models_path+"/*/*.ply"))
nviews = 20

scene = bpy.context.scene

missed_models_list = []


#######################################33

# model_path = models[0]

# print(model_path)   
# bpy.ops.import_mesh.ply(filepath=model_path)
# # bpy.ops.export_scene.obj(filepath=model_path[:-4]+'.obj')

# # model_path = model_path[:-4]+'.obj'

# # bpy.ops.import_scene.obj(filepath=model_path, filter_glob="*.obj")
# # os.system(command)
# # try:
# #     bpy.ops.import_scene.obj(filepath=model_path, filter_glob="*.obj")
# # except:
# #     missed_models_list.append(model_path)
# #     continue        
# imported = bpy.context.selected_objects[0]
# bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
# # 
# maxDimension = 5.0
# scaleFactor = maxDimension / max(imported.dimensions)
# # scaleFactor = maxDimension / 5
# imported.scale = (scaleFactor,scaleFactor,scaleFactor)
# imported.location = (0, 0, 0)
# imported.rotation_mode = 'XYZ'
# views = np.linspace(0, 2*np.pi, nviews, endpoint=False)
# print (views)  

# bpy.ops.object.editmode_toggle()
# bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region=None, TRANSFORM_OT_translate={"value":(0.001,0.001,0.001), "constraint_axis":(False,False,False)})

# new_mat = bpy.data.materials.new("mat_name")
# imported.active_material = new_mat

# imported.active_material.type = 'WIRE'
# imported.active_material.emit = 1
# bpy.ops.object.editmode_toggle()

# for i in range(nviews):
#         imported.rotation_euler[2] = views[i]
#         imported.rotation_euler[0] = np.pi
#         filename = model_path.split("/")[-1]
#         print (filename)
#         bpy.ops.view3d.camera_to_view_selected()
#         context.scene.render.filepath = model_path+"_whiteshaded_v"+str(i)+".png"
#         bpy.ops.render.render( write_still=True )




# meshes_to_remove = []
# for ob in bpy.context.selected_objects:
#     meshes_to_remove.append(ob.data)
# bpy.ops.object.delete()
# # Remove the meshes from memory too
# for mesh in meshes_to_remove:
#     bpy.data.meshes.remove(mesh)
# # 
# imported = None
# del imported
####################################################3



for model_path in models:
    print(model_path)   
    bpy.ops.import_mesh.ply(filepath=model_path)
    # bpy.ops.export_scene.obj(filepath=model_path[:-4]+'.obj')
    # # command = 'ply2obj '+model_path[:-4]+'.ply -o '+model_path[:-4]+'.obj'
    # model_path = model_path[:-4]+'.obj'
    # # os.system(command)
    # try:
    #     bpy.ops.import_scene.obj(filepath=model_path, filter_glob="*.obj")
    # except:
    #     missed_models_list.append(model_path)
    #     continue        
    imported = bpy.context.selected_objects[0]
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    # 
    maxDimension = 5.0
    scaleFactor = maxDimension / max(imported.dimensions)
    # scaleFactor = maxDimension / 5
    imported.scale = (scaleFactor,scaleFactor,scaleFactor)
    imported.location = (0, 0, 0)
    imported.rotation_mode = 'XYZ'

    ################*******************************************************
    #object rotation
    # imported.rotation_euler[0]=np.random.uniform(0,radians(30))
    imported.rotation_euler.rotate_axis("X", radians(30))
    # imported.rotation_euler[0]=np.random.uniform(0,0.5)

    # imported.rotation_euler[2]=np.random.uniform(0,radians(360))
    # imported.rotation_euler[2]=np.random.uniform(0,3.14*2)

    ################********************************************************

    views = np.linspace(0, 2*np.pi, nviews, endpoint=False)
    print (views)


    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region=None, TRANSFORM_OT_translate={"value":(0.001,0.001,0.001), "constraint_axis":(False,False,False)})

    new_mat = bpy.data.materials.new("mat_name")
    imported.active_material = new_mat

    imported.active_material.type = 'WIRE'
    imported.active_material.emit = 1
    bpy.ops.object.editmode_toggle()

    for i in range(nviews):
        imported.rotation_euler[2] = views[i]
        imported.rotation_euler[0] = np.pi
        filename = model_path.split("/")[-1]
        print (filename)
        bpy.ops.view3d.camera_to_view_selected()
        context.scene.render.filepath = model_path+"_whiteshaded_v"+str(i)+".png"
        bpy.ops.render.render( write_still=True )
        # time.sleep(5)
        # 
    meshes_to_remove = []
    for ob in bpy.context.selected_objects:
        meshes_to_remove.append(ob.data)
    bpy.ops.object.delete()
    # Remove the meshes from memory too
    for mesh in meshes_to_remove:
        bpy.data.meshes.remove(mesh)
    # 
    imported = None
    del imported