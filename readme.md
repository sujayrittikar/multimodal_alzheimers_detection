**Steps to initiate the data files**

1. conda create -n dip_env python=3.10
2. conda activate dip_env
3. pip install -r requirements.txt
4. SCP the ADNI Dataset to the GPU instance
5. unzip 'ADNI1_Complete 1Yr 1.5T.zip' -d adni_dataset
6. Extract image files to adni_flat_dataset to resolve directory structure
7. Refer to the adni_subject_file_ma.json to map each subject to image files and, ADNI1_Complete_1Yr_1.5T_1_26_2025.csv to refer to the CSV data for files.
