#!/usr/bin/python3

import uuid
import json
import base64

def orderDict(d: dict):
    """Deep sort dictionary by keys
    
    Args:
        d (dict): unsorted dictionary
    
    Returns:
        [dict]: Sorted dictionary
    """

    return {k: orderDict(v) if isinstance(v, dict) else v for k, v in sorted(d.items())}


def getNonce():
    return str(uuid.uuid4().hex + uuid.uuid1().hex)


def getB64String(s: str, encoding="utf-8") -> str:
    """Returns an encoded base64 string
    
    Args:
        s (str): Raw string
        encoding (str, optional): Defaults to "utf-8".
    
    Returns:
        [str]: Encoded base64 string
    """

    return base64.b64encode(s.encode(encoding)).decode(encoding)