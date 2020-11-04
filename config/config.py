#
# Created on Wed Nov 04 2020 11:15:39 PM
#
# author: Praveen Kumar
#
# github url: https://github.com/ds-praveenkumar/
#
# filename: config.py
#


from pathlib import Path

class Config:
    """ stores default configuration """


    ROOT_DIR = Path(Path.cwd()).resolve().as_posix()
    DATA_DIR = Path(ROOT_DIR) / "data"
    RAW_DATA = Path(DATA_DIR) / "raw"
    PROCESSED_DATA = Path(DATA_DIR) / "processed"
    CLAENED_DATA = Path(DATA_DIR) / "cleaned"

    MODELS_DIR = Path(ROOT_DIR) / "models"
    NB_DIR = Path(ROOT_DIR) / "notebooks"
    DOCS_DIR = Path(ROOT_DIR) / "docs" 
               
    SRC_DIR = Path(ROOT_DIR) / "src" 
    BUILD_DIR = Path(SRC_DIR.as_posix()) / "build" 
    PREPARE_DIR = Path(SRC_DIR.as_posix()) / "prepare" 
    PREDICT_DIR = Path(SRC_DIR.as_posix()) / "predict"   
