import matplotlib.pyplot as plt
import nibabel as nib

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

def NII_to_3Darray(path):
    NII = nib.load(path).get_fdata()
    return NII
