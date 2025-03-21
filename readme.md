# Exploring Multimodal Fusion and Vision Language Models for Alzheimer’s Disease Detection

**Steps to initiate the data files after cloning this repo:**

1. `conda create -n dip_env python=3.10`
2. `conda activate dip_env`
3. `pip install -r requirements.txt`
4. Download 1Yr 1.5T Dataset from Shared Collections on ADNI Loni website ([https://ida.loni.usc.edu](https://ida.loni.usc.edu)).
5. SCP the ADNI Dataset to the GPU instance. Ex: `scp -r 'ADNI1_Complete 1Yr 1.5T.zip' your_username@your_gpu:`
6. Run command `unzip 'ADNI1_Complete 1Yr 1.5T.zip' -d adni_dataset`
7. Extract image files to `adni_flat_dataset` directory using the `create_dataset.ipynb` file.
8. Refer to the `adni_subject_file_ma.json` to map each subject to image files.

**Navigating this repository ⛵️**
1. For Data Analysis, multiple notebooks and experiments were conducted. These notebooks can be found in [analysis_notebooks](https://github.com/sujayrittikar/dip_project/tree/main/analysis_notebooks).
2. All forms of the ADNI dataset used are available in the `datasets` repository.
3. Preprocessing techniques with best performance were used and 3D MRI Scans were converted to 2D slices. These pre-processed images can be found here: [https://github.com/sujayrittikar/dip_project/tree/main/preprocessed_images_3](https://github.com/sujayrittikar/dip_project/tree/main/preprocessed_images_3).
4. Unimodal Model Notebooks:
    - Image Models:
      - [3D MONAI ResNet-18](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/ResNet.ipynb)
      - [3D MONAI ViT](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/ViT.ipynb)
      - [ViT CLAHE](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/ViT-CLAHE.ipynb)
      - [ViT BPS](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/ViT-Bit_Plane_Slicing.ipynb)
      - [2D ViT, DeIT](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/Uni-Modal%20and%20Multi%20Modal%20results.ipynb)
      - [BeIT](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/BEIT%20Model%20Code%20for%20end%20to%20end%20training%20and%20inference)
    - Tabular Models:
      - [TabNet](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/TabNet.ipynb)
      - [Ft-Transformer](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/Ft-transformer.ipynb)
5. Multimodal Model Notebooks:
    - [ViT-BPS + TabNet Multimodal Fusion](https://github.com/sujayrittikar/dip_project/blob/main/multimodal/ViT-Bit_Plane_Slicing%20%2B%20Multi%20modal%20Fusion%20-%20early%20and%20mid.ipynb)
    - [ViT-BPS +_ Ft-Transformer](https://github.com/sujayrittikar/dip_project/blob/main/multimodal/ViT-BPS_FtTransformer_3D.ipynb)
    - [DeIT + Ft-Transformer](https://github.com/sujayrittikar/dip_project/blob/main/multimodal/Ft-transformer%20%2B%20Deit.ipynb)
    - [GPT-4o Mini](https://github.com/sujayrittikar/dip_project/blob/main/multimodal/gpt_4o.py)
    - [Deepseek VL 1.3B](https://github.com/sujayrittikar/dip_project/blob/main/multimodal/deepseek_vl_1_3_b.ipynb)
