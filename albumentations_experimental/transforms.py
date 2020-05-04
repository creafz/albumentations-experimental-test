from albumentations.core.serialization import SerializableMeta, CLASS_FULLNAME_KEY, get_obj_class_fullname
from albumentations.core.utils import format_args


class Subtract(metaclass=SerializableMeta):

    def __init__(self, subtract_value):
        self.subtract_value = subtract_value

    def apply(self, image):
        return image - self.subtract_value

    def _to_dict(self):
        """
        Must be implemented in the transform class to support serialization. This method should return the unique
        identifier for the transform class in `CLASS_FULLNAME_KEY` as well as all arguments. Those arguments will be
        serialized and later those arguments will be passed to the __init__ method while instantiating a deserialized
        version of the transform.
        """
        return {
            CLASS_FULLNAME_KEY: get_obj_class_fullname(self),
            "subtract_value": self.subtract_value,
        }

    def __repr__(self):
        """
        Should be implemented to return a prettified string representation of the transform.
        """
        return "{name}({args})".format(
            name=self.__class__.__name__,
            args=format_args({"subtract_value": self.subtract_value})
        )
