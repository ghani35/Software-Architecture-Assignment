// Generated by gencpp from file pal_detection_msgs/AddTexturedObject.msg
// DO NOT EDIT!


#ifndef PAL_DETECTION_MSGS_MESSAGE_ADDTEXTUREDOBJECT_H
#define PAL_DETECTION_MSGS_MESSAGE_ADDTEXTUREDOBJECT_H

#include <ros/service_traits.h>


#include <pal_detection_msgs/AddTexturedObjectRequest.h>
#include <pal_detection_msgs/AddTexturedObjectResponse.h>


namespace pal_detection_msgs
{

struct AddTexturedObject
{

typedef AddTexturedObjectRequest Request;
typedef AddTexturedObjectResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct AddTexturedObject
} // namespace pal_detection_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::pal_detection_msgs::AddTexturedObject > {
  static const char* value()
  {
    return "e516c1b4cddfd9938ab91f008085bdcc";
  }

  static const char* value(const ::pal_detection_msgs::AddTexturedObject&) { return value(); }
};

template<>
struct DataType< ::pal_detection_msgs::AddTexturedObject > {
  static const char* value()
  {
    return "pal_detection_msgs/AddTexturedObject";
  }

  static const char* value(const ::pal_detection_msgs::AddTexturedObject&) { return value(); }
};


// service_traits::MD5Sum< ::pal_detection_msgs::AddTexturedObjectRequest> should match
// service_traits::MD5Sum< ::pal_detection_msgs::AddTexturedObject >
template<>
struct MD5Sum< ::pal_detection_msgs::AddTexturedObjectRequest>
{
  static const char* value()
  {
    return MD5Sum< ::pal_detection_msgs::AddTexturedObject >::value();
  }
  static const char* value(const ::pal_detection_msgs::AddTexturedObjectRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::pal_detection_msgs::AddTexturedObjectRequest> should match
// service_traits::DataType< ::pal_detection_msgs::AddTexturedObject >
template<>
struct DataType< ::pal_detection_msgs::AddTexturedObjectRequest>
{
  static const char* value()
  {
    return DataType< ::pal_detection_msgs::AddTexturedObject >::value();
  }
  static const char* value(const ::pal_detection_msgs::AddTexturedObjectRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::pal_detection_msgs::AddTexturedObjectResponse> should match
// service_traits::MD5Sum< ::pal_detection_msgs::AddTexturedObject >
template<>
struct MD5Sum< ::pal_detection_msgs::AddTexturedObjectResponse>
{
  static const char* value()
  {
    return MD5Sum< ::pal_detection_msgs::AddTexturedObject >::value();
  }
  static const char* value(const ::pal_detection_msgs::AddTexturedObjectResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::pal_detection_msgs::AddTexturedObjectResponse> should match
// service_traits::DataType< ::pal_detection_msgs::AddTexturedObject >
template<>
struct DataType< ::pal_detection_msgs::AddTexturedObjectResponse>
{
  static const char* value()
  {
    return DataType< ::pal_detection_msgs::AddTexturedObject >::value();
  }
  static const char* value(const ::pal_detection_msgs::AddTexturedObjectResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // PAL_DETECTION_MSGS_MESSAGE_ADDTEXTUREDOBJECT_H
