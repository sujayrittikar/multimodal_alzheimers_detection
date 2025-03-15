**Steps to initiate the data files after cloning this repo**

1. `conda create -n dip_env python=3.10`
2. `conda activate dip_env`
3. `pip install -r requirements.txt`
4. Download 1Yr 1.5T Dataset from Shared Collections on ADNI Loni website ([https://ida.loni.usc.edu](https://ida.loni.usc.edu)).
5. SCP the ADNI Dataset to the GPU instance. Ex: `scp -r 'ADNI1_Complete 1Yr 1.5T.zip' your_username@your_gpu:`
6. Run command `unzip 'ADNI1_Complete 1Yr 1.5T.zip' -d adni_dataset`
7. Extract image files to `adni_flat_dataset` directory using the `create_dataset.ipynb` file.
8. Refer to the `adni_subject_file_ma.json` to map each subject to image files and, `ADNI1_Complete_1Yr_1.5T_1_26_2025.csv` to refer to the CSV data for files.
9. ## Yo man kindly check out the code of the **BEIT** transformer for the end to end training and evaluation. Also, check out the three data splits and the image directory.
10. 15 March: Check out the notebook "Uni-Modal and Multi Modal results.ipynb" located in the Uni-Modal folder. It contains the results of Uni-modal evaluations as well as the Multimodal - Early and Mid fusion
