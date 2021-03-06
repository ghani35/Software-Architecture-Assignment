# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from pal_navigation_msgs/Emergency.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class Emergency(genpy.Message):
  _md5sum = "a23e1ed551a213a5d03f1cf6db037717"
  _type = "pal_navigation_msgs/Emergency"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Emergency stop msg
bool data
bool forward
bool backward
std_msgs/String[] msgs


================================================================================
MSG: std_msgs/String
string data
"""
  __slots__ = ['data','forward','backward','msgs']
  _slot_types = ['bool','bool','bool','std_msgs/String[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       data,forward,backward,msgs

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Emergency, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.data is None:
        self.data = False
      if self.forward is None:
        self.forward = False
      if self.backward is None:
        self.backward = False
      if self.msgs is None:
        self.msgs = []
    else:
      self.data = False
      self.forward = False
      self.backward = False
      self.msgs = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3B().pack(_x.data, _x.forward, _x.backward))
      length = len(self.msgs)
      buff.write(_struct_I.pack(length))
      for val1 in self.msgs:
        _x = val1.data
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.msgs is None:
        self.msgs = None
      end = 0
      _x = self
      start = end
      end += 3
      (_x.data, _x.forward, _x.backward,) = _get_struct_3B().unpack(str[start:end])
      self.data = bool(self.data)
      self.forward = bool(self.forward)
      self.backward = bool(self.backward)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.msgs = []
      for i in range(0, length):
        val1 = std_msgs.msg.String()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.data = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.data = str[start:end]
        self.msgs.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3B().pack(_x.data, _x.forward, _x.backward))
      length = len(self.msgs)
      buff.write(_struct_I.pack(length))
      for val1 in self.msgs:
        _x = val1.data
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.msgs is None:
        self.msgs = None
      end = 0
      _x = self
      start = end
      end += 3
      (_x.data, _x.forward, _x.backward,) = _get_struct_3B().unpack(str[start:end])
      self.data = bool(self.data)
      self.forward = bool(self.forward)
      self.backward = bool(self.backward)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.msgs = []
      for i in range(0, length):
        val1 = std_msgs.msg.String()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.data = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.data = str[start:end]
        self.msgs.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3B = None
def _get_struct_3B():
    global _struct_3B
    if _struct_3B is None:
        _struct_3B = struct.Struct("<3B")
    return _struct_3B
