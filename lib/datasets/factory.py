# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""Factory method for easily getting imdbs by name."""

__sets = {}

from datasets.pascal_voc import pascal_voc
from datasets.coco import coco
from datasets.compcars import compcars
from datasets.carsample import carsample
from datasets.vehicle import vehicle
from datasets.tattoo import tattoo

import numpy as np

# Set up voc_<year>_<split> using selective search "fast" mode
for year in ['2007', '2012']:
    for split in ['train', 'val', 'trainval', 'test']:
        name = 'voc_{}_{}'.format(year, split)
        __sets[name] = (lambda split=split, year=year: pascal_voc(split, year))

# Set up coco_2014_<split>
for year in ['2014']:
    for split in ['train', 'val', 'minival', 'valminusminival']:
        name = 'coco_{}_{}'.format(year, split)
        __sets[name] = (lambda split=split, year=year: coco(split, year))

# Set up coco_2015_<split>
for year in ['2015']:
    for split in ['test', 'test-dev']:
        name = 'coco_{}_{}'.format(year, split)
        __sets[name] = (lambda split=split, year=year: coco(split, year))

# Set up compcars_<split>
for split in ['train', 'val', 'trainval']:
    name = 'compcars_{}'.format(split)
    __sets[name] = (lambda split=split: compcars(split))


# Set up carsimple_<split>
for split in ['train', 'val', 'trainval']:
    name = 'carsample_{}'.format(split)
    __sets[name] = (lambda split=split: carsample(split))


for split in ['fold']:
    for num in range(5):
        name = 'carsample_{}{}'.format(split, num)
        __sets[name] = (lambda split=split: carsample(split, num))

# Set up vehicle_<split>
for split in ['train', 'val', 'trainval']:
    name = 'vehicle_{}'.format(split)
    __sets[name] = (lambda split=split: vehicle(split))


# Set up tattoo_<split>
for split in ['train', 'val', 'trainval']:
    name = 'tattoo_{}'.format(split)
    __sets[name] = (lambda split=split: tattoo(split))


def get_imdb(name):
    """Get an imdb (image database) by name."""
    if not __sets.has_key(name):
        raise KeyError('Unknown dataset: {}'.format(name))
    return __sets[name]()

def list_imdbs():
    """List all registered imdbs."""
    return __sets.keys()
