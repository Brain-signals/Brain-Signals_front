import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
from scipy import ndimage


def NII_to_3Darray(path):
    NII = nib.load(path).get_fdata()
    return NII


def show_nii_2D(volume):
    slice_x = int(volume.shape[0]/2)
    slice_y = int(volume.shape[1]/2)
    slice_z = int(volume.shape[2]/2)

    fig, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(10,4))
    ax1.imshow(volume[slice_x,:,:],cmap='gray')
    ax1.set_ylabel('Y axis')
    ax1.set_xlabel('Z axis')
    ax1.tick_params(bottom=False,left=False,labelbottom=False,labelleft=False)
    ax2.imshow(volume[:,slice_y,:],cmap='gray')
    ax2.set_ylabel('X axis')
    ax2.set_xlabel('Z axis')
    ax2.tick_params(bottom=False,left=False,labelbottom=False,labelleft=False)
    ax3.imshow(volume[:,:,slice_z],cmap='gray')
    ax3.set_ylabel('X axis')
    ax3.set_xlabel('Y axis')
    ax3.tick_params(bottom=False,left=False,labelbottom=False,labelleft=False)
    return fig


# def show_nii_3D(volume):
#     volume = ndimage.zoom(volume,np.array([96/volume.shape[0], 96/volume.shape[1], 1]))
#     # Define frames
#     nb_frames = volume.shape[-1] - 1 #minus 1 frame for initial display
#     fig = go.Figure(frames=[go.Frame(data=go.Surface(z=(nb_frames/10 - k * 0.1) * np.ones((96, 96)),
#                                                     surfacecolor=np.rot90(volume[:,:,nb_frames - k]),
#                                                     cmin=0, cmax=255
#                                                     ),
#                                     name=str(k) # you need to name the frame for the animation to behave properly
#                                     )
#                     for k in range(20,nb_frames-10)])

#     # Add data to be displayed before animation starts
#     fig.add_trace(go.Surface(
#         z=nb_frames/10 * np.ones((96, 96)),
#         surfacecolor=np.rot90(volume[:,:,nb_frames]),
#         colorscale='Gray',
#         cmin=0, cmax=255,
#         colorbar=dict(thickness=20, ticklen=4)
#         ))

#     # Layout
#     fig.update_layout(
#         title='Slices in volumetric data',
#         width=600,
#         height=600,
#         scene=dict(
#             zaxis=dict(range=[0, nb_frames/10], autorange=False),
#             aspectratio=dict(x=1, y=1, z=1)),
#         updatemenus = [{"buttons": [
#                       {
#                           "args": [None, frame_args(50)],
#                           "label": "&#9654;", # play symbol
#                           "method": "animate",
#                       },
#                       {
#                           "args": [[None], frame_args(0)],
#                           "label": "&#9724;", # pause symbol
#                           "method": "animate",
#                       },
#                   ],
#                   "direction": "left",
#                   "pad": {"r": 10, "t": 70},
#                   "type": "buttons",
#                   "x": 0.1,
#                   "y": 0,
#               }
#           ],
#           sliders=sliders
#     )
#   return fig
