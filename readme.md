# Exploring Multimodal Fusion and Vision Language Models for Alzheimer’s Disease Detection

**Steps to initiate the data files after cloning this repo:**

1. `conda create -n dip_env python=3.10`
2. `conda activate dip_env`
3. `pip install -r requirements.txt`

**ADNI-1:**
1. Download 1Yr 1.5T Dataset from Shared Collections on ADNI Loni website ([https://ida.loni.usc.edu](https://ida.loni.usc.edu)).
2. SCP the ADNI Dataset to the GPU instance. Ex: `scp -r 'ADNI1_Complete 1Yr 1.5T.zip' your_username@your_gpu:`
3. Run command `unzip 'ADNI1_Complete 1Yr 1.5T.zip' -d adni_dataset`
4. Extract image files to `adni_flat_dataset` directory using the file [`create_dataset.ipynb`](https://github.com/sujayrittikar/multimodal_alzheimers_detection/blob/main/create_dataset.ipynb).
5. Refer to the `adni_subject_file_ma.json` to map each subject to image files.

**OASIS-2:**
1. Download Longitudinal Subject Data and Longitudinal Scan Data from OASIS-2 website ([https://sites.wustl.edu/oasisbrains/home/oasis-2/](https://sites.wustl.edu/oasisbrains/home/oasis-2/)).
2. SCP the files to the GPU instance like in ADNI-1 steps.
3. Unzip all the files
4. Extract image files to `oasis_2_flat_dataset` directory using the file [`create_dataset-oasis2.ipynb`](https://github.com/sujayrittikar/multimodal_alzheimers_detection/blob/main/create_dataset-oasis2.ipynb).
5. Map sessions using the Subject Data csv file.

**Dataset Access:**

Access to this repo's datasets is restricted to authorized users. The interested users can email us at [suj00rit20@gmail.com](mailto:suj00rit20@gmail.com) or [manjotsinghsran2001@gmail.com](mailto:manjotsinghsran2001@gmail.com) for access.

**Navigating this repository ⛵️**
1. For Data Analysis, multiple notebooks and experiments were conducted. These notebooks can be found in [analysis_notebooks](https://github.com/sujayrittikar/dip_project/tree/main/analysis_notebooks).
2. All forms of the ADNI dataset used are available in the `datasets` repository.
3. Preprocessing techniques with the best performance were used, and 3D MRI Scans were converted to 2D slices.
4. Unimodal Model Notebooks:
    - Image Models:
      - [3D MONAI ResNet-18 ADNI-1](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/ResNet.ipynb)
      - [3D MONAI ViT ADNI-1](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/ViT.ipynb)
      - [ViT CLAHE ADNI-1](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/ViT-CLAHE.ipynb)
      - [ViT BPS ADNI-1](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/ViT-Bit_Plane_Slicing.ipynb)
      - [2D ViT, DeIT ADNI-1](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/Uni-Modal%20and%20Multi%20Modal%20results.ipynb)
      - [BeIT ADNI-1](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/BEIT%20Model%20Code%20for%20end%20to%20end%20training%20and%20inference)
    - Tabular Models:
      - [TabNet ADNI-1](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/TabNet.ipynb)
      - [FT-Transformer ADNI-1](https://github.com/sujayrittikar/dip_project/blob/main/unimodal/Ft-transformer.ipynb)
    - Image and Tabular Models (All in One):
      - [OASIS-2 Unimodal Experiments](https://github.com/sujayrittikar/multimodal_alzheimers_detection/blob/main/unimodal/OASIS2-unimodal-experiments.ipynb)
      - [ADNI-1 Unimodal Experiments](https://github.com/sujayrittikar/multimodal_alzheimers_detection/blob/main/unimodal/ADNI%20-Unimodal%20experiments.ipynb)
5. Multimodal Model Notebooks:
    - Multimodal Fusion and VLM notebooks:
        - [ViT-BPS + TabNet Multimodal Fusion ADNI-1](https://github.com/sujayrittikar/dip_project/blob/main/multimodal/ViT-Bit_Plane_Slicing%20%2B%20Multi%20modal%20Fusion%20-%20early%20and%20mid.ipynb)
        - [ViT-BPS +_ FT-Transformer ADNI-1](https://github.com/sujayrittikar/dip_project/blob/main/multimodal/ViT-BPS_FtTransformer_3D.ipynb)
        - [DeIT + FT-Transformer ADNI-1](https://github.com/sujayrittikar/dip_project/blob/main/multimodal/Ft-transformer%20%2B%20Deit.ipynb)
        - [DeIT + FT-Transformer OASIS 2](https://github.com/sujayrittikar/multimodal_alzheimers_detection/blob/main/multimodal/OASIS2%20-%20multimodal%20experiments.ipynb)
        - [GPT-4o Mini (for both datasets - change file paths and names)](https://github.com/sujayrittikar/dip_project/blob/main/multimodal/gpt_4o.py)
        - [Deepseek VL 1.3B (for both datasets - change file paths and names)](https://github.com/sujayrittikar/dip_project/blob/main/multimodal/deepseek_vl_1_3_b.ipynb)
        - [Llava 1.5 7B Fine-tuned using Early Fusion - change file paths and names for OASIS-2, same code](https://github.com/sujayrittikar/dip_project/blob/main/multimodal/llava_adni.ipynb)
    - Multimodal (Early and Mid Fusion):
        - [OASIS-2 multimodal Experiments](https://github.com/sujayrittikar/multimodal_alzheimers_detection/blob/main/multimodal/OASIS2%20-%20multimodal%20experiments.ipynb)
        - [ADNI-1 multimodal Experiments](https://github.com/sujayrittikar/multimodal_alzheimers_detection/blob/main/multimodal/ADNI1%20Multimodal%20Experiments.ipynb)
6. The results for each model type is available in the notebooks with Margin of Errors. For 3D-ViT, LLaVa, and GPT-4o Mini, the CSVs (with 5 observations each) are available in: [result_files](https://github.com/sujayrittikar/multimodal_alzheimers_detection/tree/main/result_files). To calculate Mean and MOE, the function can be found in [calculate_moe.py](https://github.com/sujayrittikar/multimodal_alzheimers_detection/blob/main/calculate_moe.py).

*Llava model is Publicly available*
The Llava model built for ADNI 1 dataset is publicly available to use from HuggingFace at [ADNI Llava](https://huggingface.co/sujayrittikar/adni_llava_qlora)
