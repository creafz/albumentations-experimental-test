import random

import numpy as np
import albumentations as A

from albumentations_experimental.transforms import Subtract


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)


def test_subtract_is_serializable(image):
    aug = Subtract(subtract_value=10)
    serialized_aug = A.to_dict(aug)
    deserialized_aug = A.from_dict(serialized_aug)
    set_seed(42)
    aug_data = aug.apply(image)
    set_seed(42)
    deserialized_aug_data = deserialized_aug.apply(image)
    assert np.array_equal(aug_data, deserialized_aug_data)
