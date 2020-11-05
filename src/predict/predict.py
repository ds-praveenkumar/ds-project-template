#
# Created on Fri Nov 06 2020 12:09:18 AM
#
# author: Praveen Kumar
#
# github url: https://github.com/ds-praveenkumar/
#
# filename: predict.py
#


""" makes prediction """
import torch

from src.build.build import 

class Predict:
    """ Make prediction on test data """
    def __init__(self):
        """ Initilize model parameters  """

        dl = enumerate(mnist_train_loader)
        _, (datas, targets) = next(dl)
        logits = model.forward(datas)

        try_idx = 0
        output, target = torch.argmax(logits[try_idx]), targets[try_idx]
        result = output.item() == target.item()
        print(f'output {output.item()} and target is {target.item()}, so the result is {result} ')