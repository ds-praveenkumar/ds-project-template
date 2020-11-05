#
# Created on Fri Nov 06 2020 12:02:43 AM
#
# author: Praveen Kumar
#
# github url: https://github.com/ds-praveenkumar/
#
# filename: train.py
#

""" Trains the model """

from src.build.build import  LitAutoEncoder
from pytorch_lightning import Trainer


class Train:
    """ Train the  model """


    def __init__(self):
        """ initilize parameters """
        model = LitAutoEncoder()
        trainer = Trainer(max_epochs=5, gpus=1)
        trainer.fit(model, mnist_train_loader)