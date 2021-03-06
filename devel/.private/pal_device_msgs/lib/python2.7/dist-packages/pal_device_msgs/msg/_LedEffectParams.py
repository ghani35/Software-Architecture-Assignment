# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from pal_device_msgs/LedEffectParams.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import pal_device_msgs.msg
import std_msgs.msg

class LedEffectParams(genpy.Message):
  _md5sum = "cf78e4edf6ae7c6ce024d091a1a3c19a"
  _type = "pal_device_msgs/LedEffectParams"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint8 FIXED_COLOR=0
uint8 RAINBOW=1
uint8 FADE=2
uint8 BLINK=3
uint8 PROGRESS=4
uint8 FLOW=5
uint8 PREPROGRAMMED_EFFECT=6
uint8 EFFECT_VIA_TOPIC=7
uint8 DATA_ARRAY=8

uint8 effectType

# RGBA of color, alpha will be used as intensity if supported by the led
pal_device_msgs/LedFixedColorParams fixed_color
pal_device_msgs/LedRainbowParams rainbow
pal_device_msgs/LedFadeParams fade
pal_device_msgs/LedBlinkParams blink
pal_device_msgs/LedProgressParams progress
pal_device_msgs/LedFlowParams flow
#Below are device specific, avoid them if you can
pal_device_msgs/LedPreProgrammedParams preprogrammed
pal_device_msgs/LedEffectViaTopicParams effect_via_topic
pal_device_msgs/LedDataArrayParams data_array

================================================================================
MSG: pal_device_msgs/LedFixedColorParams
# RGBA of color, alpha will be used as intensity if supported by the led
std_msgs/ColorRGBA color

================================================================================
MSG: std_msgs/ColorRGBA
float32 r
float32 g
float32 b
float32 a

================================================================================
MSG: pal_device_msgs/LedRainbowParams
# Time to perform rainbow
duration transition_duration

================================================================================
MSG: pal_device_msgs/LedFadeParams
# RGBA of color, alpha will be used as intensity if supported by the led
std_msgs/ColorRGBA first_color
std_msgs/ColorRGBA second_color

#Duration of the transition from one color to the other
duration transition_duration

#Perform a fade when going from secondColor to firstColor
bool reverse_fade


================================================================================
MSG: pal_device_msgs/LedBlinkParams
# RGBA of color, alpha will be used as intensity if supported by the led
std_msgs/ColorRGBA first_color
std_msgs/ColorRGBA second_color

duration first_color_duration
duration second_color_duration


================================================================================
MSG: pal_device_msgs/LedProgressParams
# RGBA of color, alpha will be used as intensity if supported by the led
std_msgs/ColorRGBA first_color
std_msgs/ColorRGBA second_color

#Percentage of pixels painted with the first color
float32 percentage
#Offset to begin painting the first color
float32 led_offset 


================================================================================
MSG: pal_device_msgs/LedFlowParams
# RGBA of color, alpha will be used as intensity if supported by the led
std_msgs/ColorRGBA first_color
std_msgs/ColorRGBA second_color

# Percentage of pixels painted with the first color
float32 percentage
# Flow velocity
float32 velocity


================================================================================
MSG: pal_device_msgs/LedPreProgrammedParams
#Id of pre-programmed effect, most likely device specific
uint8 preprogrammed_id

================================================================================
MSG: pal_device_msgs/LedEffectViaTopicParams
#Topic name, must be of type pal_device_msgs/LedDataArray
string topic_name

================================================================================
MSG: pal_device_msgs/LedDataArrayParams
#Data of the effect, each element in the array represents a led, 
#length should match device led count
#For devices with no RGB option, just the alpha channel will be used
std_msgs/ColorRGBA[] data
"""
  # Pseudo-constants
  FIXED_COLOR = 0
  RAINBOW = 1
  FADE = 2
  BLINK = 3
  PROGRESS = 4
  FLOW = 5
  PREPROGRAMMED_EFFECT = 6
  EFFECT_VIA_TOPIC = 7
  DATA_ARRAY = 8

  __slots__ = ['effectType','fixed_color','rainbow','fade','blink','progress','flow','preprogrammed','effect_via_topic','data_array']
  _slot_types = ['uint8','pal_device_msgs/LedFixedColorParams','pal_device_msgs/LedRainbowParams','pal_device_msgs/LedFadeParams','pal_device_msgs/LedBlinkParams','pal_device_msgs/LedProgressParams','pal_device_msgs/LedFlowParams','pal_device_msgs/LedPreProgrammedParams','pal_device_msgs/LedEffectViaTopicParams','pal_device_msgs/LedDataArrayParams']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       effectType,fixed_color,rainbow,fade,blink,progress,flow,preprogrammed,effect_via_topic,data_array

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LedEffectParams, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.effectType is None:
        self.effectType = 0
      if self.fixed_color is None:
        self.fixed_color = pal_device_msgs.msg.LedFixedColorParams()
      if self.rainbow is None:
        self.rainbow = pal_device_msgs.msg.LedRainbowParams()
      if self.fade is None:
        self.fade = pal_device_msgs.msg.LedFadeParams()
      if self.blink is None:
        self.blink = pal_device_msgs.msg.LedBlinkParams()
      if self.progress is None:
        self.progress = pal_device_msgs.msg.LedProgressParams()
      if self.flow is None:
        self.flow = pal_device_msgs.msg.LedFlowParams()
      if self.preprogrammed is None:
        self.preprogrammed = pal_device_msgs.msg.LedPreProgrammedParams()
      if self.effect_via_topic is None:
        self.effect_via_topic = pal_device_msgs.msg.LedEffectViaTopicParams()
      if self.data_array is None:
        self.data_array = pal_device_msgs.msg.LedDataArrayParams()
    else:
      self.effectType = 0
      self.fixed_color = pal_device_msgs.msg.LedFixedColorParams()
      self.rainbow = pal_device_msgs.msg.LedRainbowParams()
      self.fade = pal_device_msgs.msg.LedFadeParams()
      self.blink = pal_device_msgs.msg.LedBlinkParams()
      self.progress = pal_device_msgs.msg.LedProgressParams()
      self.flow = pal_device_msgs.msg.LedFlowParams()
      self.preprogrammed = pal_device_msgs.msg.LedPreProgrammedParams()
      self.effect_via_topic = pal_device_msgs.msg.LedEffectViaTopicParams()
      self.data_array = pal_device_msgs.msg.LedDataArrayParams()

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
      buff.write(_get_struct_B4f2i8f2iB8f4i20fB().pack(_x.effectType, _x.fixed_color.color.r, _x.fixed_color.color.g, _x.fixed_color.color.b, _x.fixed_color.color.a, _x.rainbow.transition_duration.secs, _x.rainbow.transition_duration.nsecs, _x.fade.first_color.r, _x.fade.first_color.g, _x.fade.first_color.b, _x.fade.first_color.a, _x.fade.second_color.r, _x.fade.second_color.g, _x.fade.second_color.b, _x.fade.second_color.a, _x.fade.transition_duration.secs, _x.fade.transition_duration.nsecs, _x.fade.reverse_fade, _x.blink.first_color.r, _x.blink.first_color.g, _x.blink.first_color.b, _x.blink.first_color.a, _x.blink.second_color.r, _x.blink.second_color.g, _x.blink.second_color.b, _x.blink.second_color.a, _x.blink.first_color_duration.secs, _x.blink.first_color_duration.nsecs, _x.blink.second_color_duration.secs, _x.blink.second_color_duration.nsecs, _x.progress.first_color.r, _x.progress.first_color.g, _x.progress.first_color.b, _x.progress.first_color.a, _x.progress.second_color.r, _x.progress.second_color.g, _x.progress.second_color.b, _x.progress.second_color.a, _x.progress.percentage, _x.progress.led_offset, _x.flow.first_color.r, _x.flow.first_color.g, _x.flow.first_color.b, _x.flow.first_color.a, _x.flow.second_color.r, _x.flow.second_color.g, _x.flow.second_color.b, _x.flow.second_color.a, _x.flow.percentage, _x.flow.velocity, _x.preprogrammed.preprogrammed_id))
      _x = self.effect_via_topic.topic_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.data_array.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.data_array.data:
        _x = val1
        buff.write(_get_struct_4f().pack(_x.r, _x.g, _x.b, _x.a))
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
      if self.fixed_color is None:
        self.fixed_color = pal_device_msgs.msg.LedFixedColorParams()
      if self.rainbow is None:
        self.rainbow = pal_device_msgs.msg.LedRainbowParams()
      if self.fade is None:
        self.fade = pal_device_msgs.msg.LedFadeParams()
      if self.blink is None:
        self.blink = pal_device_msgs.msg.LedBlinkParams()
      if self.progress is None:
        self.progress = pal_device_msgs.msg.LedProgressParams()
      if self.flow is None:
        self.flow = pal_device_msgs.msg.LedFlowParams()
      if self.preprogrammed is None:
        self.preprogrammed = pal_device_msgs.msg.LedPreProgrammedParams()
      if self.effect_via_topic is None:
        self.effect_via_topic = pal_device_msgs.msg.LedEffectViaTopicParams()
      if self.data_array is None:
        self.data_array = pal_device_msgs.msg.LedDataArrayParams()
      end = 0
      _x = self
      start = end
      end += 195
      (_x.effectType, _x.fixed_color.color.r, _x.fixed_color.color.g, _x.fixed_color.color.b, _x.fixed_color.color.a, _x.rainbow.transition_duration.secs, _x.rainbow.transition_duration.nsecs, _x.fade.first_color.r, _x.fade.first_color.g, _x.fade.first_color.b, _x.fade.first_color.a, _x.fade.second_color.r, _x.fade.second_color.g, _x.fade.second_color.b, _x.fade.second_color.a, _x.fade.transition_duration.secs, _x.fade.transition_duration.nsecs, _x.fade.reverse_fade, _x.blink.first_color.r, _x.blink.first_color.g, _x.blink.first_color.b, _x.blink.first_color.a, _x.blink.second_color.r, _x.blink.second_color.g, _x.blink.second_color.b, _x.blink.second_color.a, _x.blink.first_color_duration.secs, _x.blink.first_color_duration.nsecs, _x.blink.second_color_duration.secs, _x.blink.second_color_duration.nsecs, _x.progress.first_color.r, _x.progress.first_color.g, _x.progress.first_color.b, _x.progress.first_color.a, _x.progress.second_color.r, _x.progress.second_color.g, _x.progress.second_color.b, _x.progress.second_color.a, _x.progress.percentage, _x.progress.led_offset, _x.flow.first_color.r, _x.flow.first_color.g, _x.flow.first_color.b, _x.flow.first_color.a, _x.flow.second_color.r, _x.flow.second_color.g, _x.flow.second_color.b, _x.flow.second_color.a, _x.flow.percentage, _x.flow.velocity, _x.preprogrammed.preprogrammed_id,) = _get_struct_B4f2i8f2iB8f4i20fB().unpack(str[start:end])
      self.fade.reverse_fade = bool(self.fade.reverse_fade)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.effect_via_topic.topic_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.effect_via_topic.topic_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data_array.data = []
      for i in range(0, length):
        val1 = std_msgs.msg.ColorRGBA()
        _x = val1
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _get_struct_4f().unpack(str[start:end])
        self.data_array.data.append(val1)
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
      buff.write(_get_struct_B4f2i8f2iB8f4i20fB().pack(_x.effectType, _x.fixed_color.color.r, _x.fixed_color.color.g, _x.fixed_color.color.b, _x.fixed_color.color.a, _x.rainbow.transition_duration.secs, _x.rainbow.transition_duration.nsecs, _x.fade.first_color.r, _x.fade.first_color.g, _x.fade.first_color.b, _x.fade.first_color.a, _x.fade.second_color.r, _x.fade.second_color.g, _x.fade.second_color.b, _x.fade.second_color.a, _x.fade.transition_duration.secs, _x.fade.transition_duration.nsecs, _x.fade.reverse_fade, _x.blink.first_color.r, _x.blink.first_color.g, _x.blink.first_color.b, _x.blink.first_color.a, _x.blink.second_color.r, _x.blink.second_color.g, _x.blink.second_color.b, _x.blink.second_color.a, _x.blink.first_color_duration.secs, _x.blink.first_color_duration.nsecs, _x.blink.second_color_duration.secs, _x.blink.second_color_duration.nsecs, _x.progress.first_color.r, _x.progress.first_color.g, _x.progress.first_color.b, _x.progress.first_color.a, _x.progress.second_color.r, _x.progress.second_color.g, _x.progress.second_color.b, _x.progress.second_color.a, _x.progress.percentage, _x.progress.led_offset, _x.flow.first_color.r, _x.flow.first_color.g, _x.flow.first_color.b, _x.flow.first_color.a, _x.flow.second_color.r, _x.flow.second_color.g, _x.flow.second_color.b, _x.flow.second_color.a, _x.flow.percentage, _x.flow.velocity, _x.preprogrammed.preprogrammed_id))
      _x = self.effect_via_topic.topic_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.data_array.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.data_array.data:
        _x = val1
        buff.write(_get_struct_4f().pack(_x.r, _x.g, _x.b, _x.a))
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
      if self.fixed_color is None:
        self.fixed_color = pal_device_msgs.msg.LedFixedColorParams()
      if self.rainbow is None:
        self.rainbow = pal_device_msgs.msg.LedRainbowParams()
      if self.fade is None:
        self.fade = pal_device_msgs.msg.LedFadeParams()
      if self.blink is None:
        self.blink = pal_device_msgs.msg.LedBlinkParams()
      if self.progress is None:
        self.progress = pal_device_msgs.msg.LedProgressParams()
      if self.flow is None:
        self.flow = pal_device_msgs.msg.LedFlowParams()
      if self.preprogrammed is None:
        self.preprogrammed = pal_device_msgs.msg.LedPreProgrammedParams()
      if self.effect_via_topic is None:
        self.effect_via_topic = pal_device_msgs.msg.LedEffectViaTopicParams()
      if self.data_array is None:
        self.data_array = pal_device_msgs.msg.LedDataArrayParams()
      end = 0
      _x = self
      start = end
      end += 195
      (_x.effectType, _x.fixed_color.color.r, _x.fixed_color.color.g, _x.fixed_color.color.b, _x.fixed_color.color.a, _x.rainbow.transition_duration.secs, _x.rainbow.transition_duration.nsecs, _x.fade.first_color.r, _x.fade.first_color.g, _x.fade.first_color.b, _x.fade.first_color.a, _x.fade.second_color.r, _x.fade.second_color.g, _x.fade.second_color.b, _x.fade.second_color.a, _x.fade.transition_duration.secs, _x.fade.transition_duration.nsecs, _x.fade.reverse_fade, _x.blink.first_color.r, _x.blink.first_color.g, _x.blink.first_color.b, _x.blink.first_color.a, _x.blink.second_color.r, _x.blink.second_color.g, _x.blink.second_color.b, _x.blink.second_color.a, _x.blink.first_color_duration.secs, _x.blink.first_color_duration.nsecs, _x.blink.second_color_duration.secs, _x.blink.second_color_duration.nsecs, _x.progress.first_color.r, _x.progress.first_color.g, _x.progress.first_color.b, _x.progress.first_color.a, _x.progress.second_color.r, _x.progress.second_color.g, _x.progress.second_color.b, _x.progress.second_color.a, _x.progress.percentage, _x.progress.led_offset, _x.flow.first_color.r, _x.flow.first_color.g, _x.flow.first_color.b, _x.flow.first_color.a, _x.flow.second_color.r, _x.flow.second_color.g, _x.flow.second_color.b, _x.flow.second_color.a, _x.flow.percentage, _x.flow.velocity, _x.preprogrammed.preprogrammed_id,) = _get_struct_B4f2i8f2iB8f4i20fB().unpack(str[start:end])
      self.fade.reverse_fade = bool(self.fade.reverse_fade)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.effect_via_topic.topic_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.effect_via_topic.topic_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data_array.data = []
      for i in range(0, length):
        val1 = std_msgs.msg.ColorRGBA()
        _x = val1
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _get_struct_4f().unpack(str[start:end])
        self.data_array.data.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4f = None
def _get_struct_4f():
    global _struct_4f
    if _struct_4f is None:
        _struct_4f = struct.Struct("<4f")
    return _struct_4f
_struct_B4f2i8f2iB8f4i20fB = None
def _get_struct_B4f2i8f2iB8f4i20fB():
    global _struct_B4f2i8f2iB8f4i20fB
    if _struct_B4f2i8f2iB8f4i20fB is None:
        _struct_B4f2i8f2iB8f4i20fB = struct.Struct("<B4f2i8f2iB8f4i20fB")
    return _struct_B4f2i8f2iB8f4i20fB
