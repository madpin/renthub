from fastapi.logger import logger
import re

def get_attr_try(obj, attr):
    try:
        return getattr(obj, attr)
    except Exception as e:
        logger.error(f"Error getting the obj attribute {attr}\n{e}")

def str_to_float_arr(value: str):
    arr = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", value)
    return [float(x) for x in arr]

def str_to_float(value: str, raise_errors:bool = False, *, default_value:float = None) -> float:
    if isinstance(value, int):
        return float(value)
    elif isinstance(value, float):
        return value

    arr = str_to_float_arr(value)
    
    if len(arr) == 0:
        if default_value:
            return default_value
        elif raise_errors:
            raise ValueError("`value` does not convert to float")
        else:
            return None
    elif len(arr) > 1:
        if raise_errors:
            raise ValueError("`value` does not convert to float")
        else:
            return None
    else:
        return float(arr[0])
        