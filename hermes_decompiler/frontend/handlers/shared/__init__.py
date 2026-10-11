from ._define_property import define_non_enumerable
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
