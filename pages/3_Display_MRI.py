import os
import streamlit as st
from utils import show_nii_2D, NII_to_3Darray

print('\n')
print('##### RE-RUN #####')

st.set_page_config(
    page_title="Display MRI",
    page_icon="👋",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

nii_file = st.file_uploader('Upload nifti file', type = 'nii', label_visibility='visible')
if nii_file is not None:
    print(nii_file.__dict__)
    if not os.path.exists(os.path.join('tmp_files')):
        os.mkdir(os.path.join('tmp_files'))

    path = os.path.join('tmp_files', nii_file.name)
    with open(path, 'wb') as f:
        nii_content = nii_file.read()
        f.write(nii_content)
    #volume = NII_to_3Darray('/Users/adriencombes/code/adriencombes/Brain-Signals/.data/processed_datasets/camcan_cc700/sub-CC110033_T1w.nii')
    volume = NII_to_3Darray(path)
    fig = show_nii_2D(volume)
    st.pyplot(fig=None)

    os.remove(path)
