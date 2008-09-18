# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _lwes

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name) or (name == "thisown"):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types



lwes_event_type_db_create = _lwes.lwes_event_type_db_create

lwes_event_type_db_destroy = _lwes.lwes_event_type_db_destroy

lwes_emitter_create = _lwes.lwes_emitter_create

lwes_emitter_create_with_ttl = _lwes.lwes_emitter_create_with_ttl

lwes_emitter_emit = _lwes.lwes_emitter_emit

lwes_emitter_emitto = _lwes.lwes_emitter_emitto

lwes_emitter_destroy = _lwes.lwes_emitter_destroy

lwes_event_create = _lwes.lwes_event_create

lwes_event_create_with_encoding = _lwes.lwes_event_create_with_encoding

lwes_event_set_U_INT_16 = _lwes.lwes_event_set_U_INT_16

lwes_event_get_U_INT_16 = _lwes.lwes_event_get_U_INT_16

lwes_event_set_INT_16 = _lwes.lwes_event_set_INT_16

lwes_event_get_INT_16 = _lwes.lwes_event_get_INT_16

lwes_event_set_U_INT_32 = _lwes.lwes_event_set_U_INT_32

lwes_event_get_U_INT_32 = _lwes.lwes_event_get_U_INT_32

lwes_event_set_INT_32 = _lwes.lwes_event_set_INT_32

lwes_event_get_INT_32 = _lwes.lwes_event_get_INT_32

lwes_event_set_U_INT_64 = _lwes.lwes_event_set_U_INT_64

lwes_event_get_U_INT_64 = _lwes.lwes_event_get_U_INT_64

lwes_event_set_INT_64 = _lwes.lwes_event_set_INT_64

lwes_event_get_INT_64 = _lwes.lwes_event_get_INT_64

lwes_event_set_STRING = _lwes.lwes_event_set_STRING

lwes_event_get_STRING = _lwes.lwes_event_get_STRING

lwes_event_set_IP_ADDR_w_string = _lwes.lwes_event_set_IP_ADDR_w_string

lwes_event_get_IP_ADDR = _lwes.lwes_event_get_IP_ADDR

lwes_event_set_BOOLEAN = _lwes.lwes_event_set_BOOLEAN

lwes_event_get_BOOLEAN = _lwes.lwes_event_get_BOOLEAN

lwes_event_destroy = _lwes.lwes_event_destroy

