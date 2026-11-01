from ._define_property import define_non_enumerable
from ._typeof_mask import build_typeof_condition
from ._literal_fold import (
    fold_array_element,
    fold_into_literal,
    fold_object_property,
    fold_slot_value,
    object_property,
    property_access,
    slot_key,
    static_key,
)

__all__ = [
    "build_typeof_condition",
    "define_non_enumerable",
    "fold_array_element",
    "fold_into_literal",
    "fold_object_property",
    "fold_slot_value",
    "object_property",
    "property_access",
    "slot_key",
    "static_key",
]
