# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logging.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='logging.proto',
  package='extensions.core_api.cast_channel.proto',
  syntax='proto2',
  serialized_pb=_b('\n\rlogging.proto\x12&extensions.core_api.cast_channel.proto\"\xa0\x05\n\x0bSocketEvent\x12?\n\x04type\x18\x01 \x01(\x0e\x32\x31.extensions.core_api.cast_channel.proto.EventType\x12\x18\n\x10timestamp_micros\x18\x02 \x01(\x03\x12\x0f\n\x07\x64\x65tails\x18\x03 \x01(\t\x12\x18\n\x10net_return_value\x18\x04 \x01(\x05\x12\x19\n\x11message_namespace\x18\x05 \x01(\t\x12G\n\x0bready_state\x18\x06 \x01(\x0e\x32\x32.extensions.core_api.cast_channel.proto.ReadyState\x12Q\n\x10\x63onnection_state\x18\x07 \x01(\x0e\x32\x37.extensions.core_api.cast_channel.proto.ConnectionState\x12\x45\n\nread_state\x18\x08 \x01(\x0e\x32\x31.extensions.core_api.cast_channel.proto.ReadState\x12G\n\x0bwrite_state\x18\t \x01(\x0e\x32\x32.extensions.core_api.cast_channel.proto.WriteState\x12G\n\x0b\x65rror_state\x18\n \x01(\x0e\x32\x32.extensions.core_api.cast_channel.proto.ErrorState\x12\x63\n\x1a\x63hallenge_reply_error_type\x18\x0b \x01(\x0e\x32?.extensions.core_api.cast_channel.proto.ChallengeReplyErrorType\x12\x16\n\x0enss_error_code\x18\x0c \x01(\x05\"\xfe\x01\n\x15\x41ggregatedSocketEvent\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0b\x65ndpoint_id\x18\x02 \x01(\x05\x12N\n\x11\x63hannel_auth_type\x18\x03 \x01(\x0e\x32\x33.extensions.core_api.cast_channel.proto.ChannelAuth\x12I\n\x0csocket_event\x18\x04 \x03(\x0b\x32\x33.extensions.core_api.cast_channel.proto.SocketEvent\x12\x12\n\nbytes_read\x18\x05 \x01(\x03\x12\x15\n\rbytes_written\x18\x06 \x01(\x03\"\xb6\x01\n\x03Log\x12^\n\x17\x61ggregated_socket_event\x18\x01 \x03(\x0b\x32=.extensions.core_api.cast_channel.proto.AggregatedSocketEvent\x12,\n$num_evicted_aggregated_socket_events\x18\x02 \x01(\x05\x12!\n\x19num_evicted_socket_events\x18\x03 \x01(\x05*\xc0\x06\n\tEventType\x12\x16\n\x12\x45VENT_TYPE_UNKNOWN\x10\x00\x12\x17\n\x13\x43\x41ST_SOCKET_CREATED\x10\x01\x12\x17\n\x13READY_STATE_CHANGED\x10\x02\x12\x1c\n\x18\x43ONNECTION_STATE_CHANGED\x10\x03\x12\x16\n\x12READ_STATE_CHANGED\x10\x04\x12\x17\n\x13WRITE_STATE_CHANGED\x10\x05\x12\x17\n\x13\x45RROR_STATE_CHANGED\x10\x06\x12\x12\n\x0e\x43ONNECT_FAILED\x10\x07\x12\x16\n\x12TCP_SOCKET_CONNECT\x10\x08\x12\x1d\n\x19TCP_SOCKET_SET_KEEP_ALIVE\x10\t\x12\x18\n\x14SSL_CERT_WHITELISTED\x10\n\x12\x16\n\x12SSL_SOCKET_CONNECT\x10\x0b\x12\x15\n\x11SSL_INFO_OBTAINED\x10\x0c\x12\x1b\n\x17\x44\x45R_ENCODED_CERT_OBTAIN\x10\r\x12\x1c\n\x18RECEIVED_CHALLENGE_REPLY\x10\x0e\x12\x18\n\x14\x41UTH_CHALLENGE_REPLY\x10\x0f\x12\x15\n\x11\x43ONNECT_TIMED_OUT\x10\x10\x12\x17\n\x13SEND_MESSAGE_FAILED\x10\x11\x12\x14\n\x10MESSAGE_ENQUEUED\x10\x12\x12\x10\n\x0cSOCKET_WRITE\x10\x13\x12\x13\n\x0fMESSAGE_WRITTEN\x10\x14\x12\x0f\n\x0bSOCKET_READ\x10\x15\x12\x10\n\x0cMESSAGE_READ\x10\x16\x12\x11\n\rSOCKET_CLOSED\x10\x19\x12\x1f\n\x1bSSL_CERT_EXCESSIVE_LIFETIME\x10\x1a\x12\x1b\n\x17\x43HANNEL_POLICY_ENFORCED\x10\x1b\x12\x1f\n\x1bTCP_SOCKET_CONNECT_COMPLETE\x10\x1c\x12\x1f\n\x1bSSL_SOCKET_CONNECT_COMPLETE\x10\x1d\x12\x1d\n\x19SSL_SOCKET_CONNECT_FAILED\x10\x1e\x12\x1e\n\x1aSEND_AUTH_CHALLENGE_FAILED\x10\x1f\x12 \n\x1c\x41UTH_CHALLENGE_REPLY_INVALID\x10 \x12\x14\n\x10PING_WRITE_ERROR\x10!*(\n\x0b\x43hannelAuth\x12\x07\n\x03SSL\x10\x01\x12\x10\n\x0cSSL_VERIFIED\x10\x02*\x85\x01\n\nReadyState\x12\x14\n\x10READY_STATE_NONE\x10\x01\x12\x1a\n\x16READY_STATE_CONNECTING\x10\x02\x12\x14\n\x10READY_STATE_OPEN\x10\x03\x12\x17\n\x13READY_STATE_CLOSING\x10\x04\x12\x16\n\x12READY_STATE_CLOSED\x10\x05*\xa7\x02\n\x0f\x43onnectionState\x12\x13\n\x0f\x43ONN_STATE_NONE\x10\x01\x12\x1a\n\x16\x43ONN_STATE_TCP_CONNECT\x10\x02\x12#\n\x1f\x43ONN_STATE_TCP_CONNECT_COMPLETE\x10\x03\x12\x1a\n\x16\x43ONN_STATE_SSL_CONNECT\x10\x04\x12#\n\x1f\x43ONN_STATE_SSL_CONNECT_COMPLETE\x10\x05\x12\"\n\x1e\x43ONN_STATE_AUTH_CHALLENGE_SEND\x10\x06\x12+\n\'CONN_STATE_AUTH_CHALLENGE_SEND_COMPLETE\x10\x07\x12,\n(CONN_STATE_AUTH_CHALLENGE_REPLY_COMPLETE\x10\x08*\x85\x01\n\tReadState\x12\x13\n\x0fREAD_STATE_NONE\x10\x01\x12\x13\n\x0fREAD_STATE_READ\x10\x02\x12\x1c\n\x18READ_STATE_READ_COMPLETE\x10\x03\x12\x1a\n\x16READ_STATE_DO_CALLBACK\x10\x04\x12\x14\n\x10READ_STATE_ERROR\x10\x05*\x8d\x01\n\nWriteState\x12\x14\n\x10WRITE_STATE_NONE\x10\x01\x12\x15\n\x11WRITE_STATE_WRITE\x10\x02\x12\x1e\n\x1aWRITE_STATE_WRITE_COMPLETE\x10\x03\x12\x1b\n\x17WRITE_STATE_DO_CALLBACK\x10\x04\x12\x15\n\x11WRITE_STATE_ERROR\x10\x05*\xdb\x02\n\nErrorState\x12\x16\n\x12\x43HANNEL_ERROR_NONE\x10\x01\x12\"\n\x1e\x43HANNEL_ERROR_CHANNEL_NOT_OPEN\x10\x02\x12&\n\"CHANNEL_ERROR_AUTHENTICATION_ERROR\x10\x03\x12\x1f\n\x1b\x43HANNEL_ERROR_CONNECT_ERROR\x10\x04\x12\x1e\n\x1a\x43HANNEL_ERROR_SOCKET_ERROR\x10\x05\x12!\n\x1d\x43HANNEL_ERROR_TRANSPORT_ERROR\x10\x06\x12!\n\x1d\x43HANNEL_ERROR_INVALID_MESSAGE\x10\x07\x12$\n CHANNEL_ERROR_INVALID_CHANNEL_ID\x10\x08\x12!\n\x1d\x43HANNEL_ERROR_CONNECT_TIMEOUT\x10\t\x12\x19\n\x15\x43HANNEL_ERROR_UNKNOWN\x10\n*\xb9\x04\n\x17\x43hallengeReplyErrorType\x12\x1e\n\x1a\x43HALLENGE_REPLY_ERROR_NONE\x10\x01\x12)\n%CHALLENGE_REPLY_ERROR_PEER_CERT_EMPTY\x10\x02\x12,\n(CHALLENGE_REPLY_ERROR_WRONG_PAYLOAD_TYPE\x10\x03\x12$\n CHALLENGE_REPLY_ERROR_NO_PAYLOAD\x10\x04\x12\x30\n,CHALLENGE_REPLY_ERROR_PAYLOAD_PARSING_FAILED\x10\x05\x12\'\n#CHALLENGE_REPLY_ERROR_MESSAGE_ERROR\x10\x06\x12%\n!CHALLENGE_REPLY_ERROR_NO_RESPONSE\x10\x07\x12/\n+CHALLENGE_REPLY_ERROR_FINGERPRINT_NOT_FOUND\x10\x08\x12-\n)CHALLENGE_REPLY_ERROR_CERT_PARSING_FAILED\x10\t\x12\x37\n3CHALLENGE_REPLY_ERROR_CERT_NOT_SIGNED_BY_TRUSTED_CA\x10\n\x12\x33\n/CHALLENGE_REPLY_ERROR_CANNOT_EXTRACT_PUBLIC_KEY\x10\x0b\x12/\n+CHALLENGE_REPLY_ERROR_SIGNED_BLOBS_MISMATCH\x10\x0c\x42\x02H\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_EVENTTYPE = _descriptor.EnumDescriptor(
  name='EventType',
  full_name='extensions.core_api.cast_channel.proto.EventType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EVENT_TYPE_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAST_SOCKET_CREATED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY_STATE_CHANGED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECTION_STATE_CHANGED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_STATE_CHANGED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRITE_STATE_CHANGED', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_STATE_CHANGED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECT_FAILED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TCP_SOCKET_CONNECT', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TCP_SOCKET_SET_KEEP_ALIVE', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SSL_CERT_WHITELISTED', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SSL_SOCKET_CONNECT', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SSL_INFO_OBTAINED', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DER_ENCODED_CERT_OBTAIN', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RECEIVED_CHALLENGE_REPLY', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_CHALLENGE_REPLY', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECT_TIMED_OUT', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_MESSAGE_FAILED', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE_ENQUEUED', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOCKET_WRITE', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE_WRITTEN', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOCKET_READ', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE_READ', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOCKET_CLOSED', index=23, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SSL_CERT_EXCESSIVE_LIFETIME', index=24, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_POLICY_ENFORCED', index=25, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TCP_SOCKET_CONNECT_COMPLETE', index=26, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SSL_SOCKET_CONNECT_COMPLETE', index=27, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SSL_SOCKET_CONNECT_FAILED', index=28, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_AUTH_CHALLENGE_FAILED', index=29, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_CHALLENGE_REPLY_INVALID', index=30, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PING_WRITE_ERROR', index=31, number=33,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1175,
  serialized_end=2007,
)
_sym_db.RegisterEnumDescriptor(_EVENTTYPE)

EventType = enum_type_wrapper.EnumTypeWrapper(_EVENTTYPE)
_CHANNELAUTH = _descriptor.EnumDescriptor(
  name='ChannelAuth',
  full_name='extensions.core_api.cast_channel.proto.ChannelAuth',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SSL', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SSL_VERIFIED', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2009,
  serialized_end=2049,
)
_sym_db.RegisterEnumDescriptor(_CHANNELAUTH)

ChannelAuth = enum_type_wrapper.EnumTypeWrapper(_CHANNELAUTH)
_READYSTATE = _descriptor.EnumDescriptor(
  name='ReadyState',
  full_name='extensions.core_api.cast_channel.proto.ReadyState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READY_STATE_NONE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY_STATE_CONNECTING', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY_STATE_OPEN', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY_STATE_CLOSING', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY_STATE_CLOSED', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2052,
  serialized_end=2185,
)
_sym_db.RegisterEnumDescriptor(_READYSTATE)

ReadyState = enum_type_wrapper.EnumTypeWrapper(_READYSTATE)
_CONNECTIONSTATE = _descriptor.EnumDescriptor(
  name='ConnectionState',
  full_name='extensions.core_api.cast_channel.proto.ConnectionState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONN_STATE_NONE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONN_STATE_TCP_CONNECT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONN_STATE_TCP_CONNECT_COMPLETE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONN_STATE_SSL_CONNECT', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONN_STATE_SSL_CONNECT_COMPLETE', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONN_STATE_AUTH_CHALLENGE_SEND', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONN_STATE_AUTH_CHALLENGE_SEND_COMPLETE', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONN_STATE_AUTH_CHALLENGE_REPLY_COMPLETE', index=7, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2188,
  serialized_end=2483,
)
_sym_db.RegisterEnumDescriptor(_CONNECTIONSTATE)

ConnectionState = enum_type_wrapper.EnumTypeWrapper(_CONNECTIONSTATE)
_READSTATE = _descriptor.EnumDescriptor(
  name='ReadState',
  full_name='extensions.core_api.cast_channel.proto.ReadState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READ_STATE_NONE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_STATE_READ', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_STATE_READ_COMPLETE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_STATE_DO_CALLBACK', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_STATE_ERROR', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2486,
  serialized_end=2619,
)
_sym_db.RegisterEnumDescriptor(_READSTATE)

ReadState = enum_type_wrapper.EnumTypeWrapper(_READSTATE)
_WRITESTATE = _descriptor.EnumDescriptor(
  name='WriteState',
  full_name='extensions.core_api.cast_channel.proto.WriteState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WRITE_STATE_NONE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRITE_STATE_WRITE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRITE_STATE_WRITE_COMPLETE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRITE_STATE_DO_CALLBACK', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRITE_STATE_ERROR', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2622,
  serialized_end=2763,
)
_sym_db.RegisterEnumDescriptor(_WRITESTATE)

WriteState = enum_type_wrapper.EnumTypeWrapper(_WRITESTATE)
_ERRORSTATE = _descriptor.EnumDescriptor(
  name='ErrorState',
  full_name='extensions.core_api.cast_channel.proto.ErrorState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_ERROR_NONE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_ERROR_CHANNEL_NOT_OPEN', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_ERROR_AUTHENTICATION_ERROR', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_ERROR_CONNECT_ERROR', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_ERROR_SOCKET_ERROR', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_ERROR_TRANSPORT_ERROR', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_ERROR_INVALID_MESSAGE', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_ERROR_INVALID_CHANNEL_ID', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_ERROR_CONNECT_TIMEOUT', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_ERROR_UNKNOWN', index=9, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2766,
  serialized_end=3113,
)
_sym_db.RegisterEnumDescriptor(_ERRORSTATE)

ErrorState = enum_type_wrapper.EnumTypeWrapper(_ERRORSTATE)
_CHALLENGEREPLYERRORTYPE = _descriptor.EnumDescriptor(
  name='ChallengeReplyErrorType',
  full_name='extensions.core_api.cast_channel.proto.ChallengeReplyErrorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_REPLY_ERROR_NONE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_REPLY_ERROR_PEER_CERT_EMPTY', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_REPLY_ERROR_WRONG_PAYLOAD_TYPE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_REPLY_ERROR_NO_PAYLOAD', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_REPLY_ERROR_PAYLOAD_PARSING_FAILED', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_REPLY_ERROR_MESSAGE_ERROR', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_REPLY_ERROR_NO_RESPONSE', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_REPLY_ERROR_FINGERPRINT_NOT_FOUND', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_REPLY_ERROR_CERT_PARSING_FAILED', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_REPLY_ERROR_CERT_NOT_SIGNED_BY_TRUSTED_CA', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_REPLY_ERROR_CANNOT_EXTRACT_PUBLIC_KEY', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_REPLY_ERROR_SIGNED_BLOBS_MISMATCH', index=11, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=3116,
  serialized_end=3685,
)
_sym_db.RegisterEnumDescriptor(_CHALLENGEREPLYERRORTYPE)

ChallengeReplyErrorType = enum_type_wrapper.EnumTypeWrapper(_CHALLENGEREPLYERRORTYPE)
EVENT_TYPE_UNKNOWN = 0
CAST_SOCKET_CREATED = 1
READY_STATE_CHANGED = 2
CONNECTION_STATE_CHANGED = 3
READ_STATE_CHANGED = 4
WRITE_STATE_CHANGED = 5
ERROR_STATE_CHANGED = 6
CONNECT_FAILED = 7
TCP_SOCKET_CONNECT = 8
TCP_SOCKET_SET_KEEP_ALIVE = 9
SSL_CERT_WHITELISTED = 10
SSL_SOCKET_CONNECT = 11
SSL_INFO_OBTAINED = 12
DER_ENCODED_CERT_OBTAIN = 13
RECEIVED_CHALLENGE_REPLY = 14
AUTH_CHALLENGE_REPLY = 15
CONNECT_TIMED_OUT = 16
SEND_MESSAGE_FAILED = 17
MESSAGE_ENQUEUED = 18
SOCKET_WRITE = 19
MESSAGE_WRITTEN = 20
SOCKET_READ = 21
MESSAGE_READ = 22
SOCKET_CLOSED = 25
SSL_CERT_EXCESSIVE_LIFETIME = 26
CHANNEL_POLICY_ENFORCED = 27
TCP_SOCKET_CONNECT_COMPLETE = 28
SSL_SOCKET_CONNECT_COMPLETE = 29
SSL_SOCKET_CONNECT_FAILED = 30
SEND_AUTH_CHALLENGE_FAILED = 31
AUTH_CHALLENGE_REPLY_INVALID = 32
PING_WRITE_ERROR = 33
SSL = 1
SSL_VERIFIED = 2
READY_STATE_NONE = 1
READY_STATE_CONNECTING = 2
READY_STATE_OPEN = 3
READY_STATE_CLOSING = 4
READY_STATE_CLOSED = 5
CONN_STATE_NONE = 1
CONN_STATE_TCP_CONNECT = 2
CONN_STATE_TCP_CONNECT_COMPLETE = 3
CONN_STATE_SSL_CONNECT = 4
CONN_STATE_SSL_CONNECT_COMPLETE = 5
CONN_STATE_AUTH_CHALLENGE_SEND = 6
CONN_STATE_AUTH_CHALLENGE_SEND_COMPLETE = 7
CONN_STATE_AUTH_CHALLENGE_REPLY_COMPLETE = 8
READ_STATE_NONE = 1
READ_STATE_READ = 2
READ_STATE_READ_COMPLETE = 3
READ_STATE_DO_CALLBACK = 4
READ_STATE_ERROR = 5
WRITE_STATE_NONE = 1
WRITE_STATE_WRITE = 2
WRITE_STATE_WRITE_COMPLETE = 3
WRITE_STATE_DO_CALLBACK = 4
WRITE_STATE_ERROR = 5
CHANNEL_ERROR_NONE = 1
CHANNEL_ERROR_CHANNEL_NOT_OPEN = 2
CHANNEL_ERROR_AUTHENTICATION_ERROR = 3
CHANNEL_ERROR_CONNECT_ERROR = 4
CHANNEL_ERROR_SOCKET_ERROR = 5
CHANNEL_ERROR_TRANSPORT_ERROR = 6
CHANNEL_ERROR_INVALID_MESSAGE = 7
CHANNEL_ERROR_INVALID_CHANNEL_ID = 8
CHANNEL_ERROR_CONNECT_TIMEOUT = 9
CHANNEL_ERROR_UNKNOWN = 10
CHALLENGE_REPLY_ERROR_NONE = 1
CHALLENGE_REPLY_ERROR_PEER_CERT_EMPTY = 2
CHALLENGE_REPLY_ERROR_WRONG_PAYLOAD_TYPE = 3
CHALLENGE_REPLY_ERROR_NO_PAYLOAD = 4
CHALLENGE_REPLY_ERROR_PAYLOAD_PARSING_FAILED = 5
CHALLENGE_REPLY_ERROR_MESSAGE_ERROR = 6
CHALLENGE_REPLY_ERROR_NO_RESPONSE = 7
CHALLENGE_REPLY_ERROR_FINGERPRINT_NOT_FOUND = 8
CHALLENGE_REPLY_ERROR_CERT_PARSING_FAILED = 9
CHALLENGE_REPLY_ERROR_CERT_NOT_SIGNED_BY_TRUSTED_CA = 10
CHALLENGE_REPLY_ERROR_CANNOT_EXTRACT_PUBLIC_KEY = 11
CHALLENGE_REPLY_ERROR_SIGNED_BLOBS_MISMATCH = 12



_SOCKETEVENT = _descriptor.Descriptor(
  name='SocketEvent',
  full_name='extensions.core_api.cast_channel.proto.SocketEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='extensions.core_api.cast_channel.proto.SocketEvent.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp_micros', full_name='extensions.core_api.cast_channel.proto.SocketEvent.timestamp_micros', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='details', full_name='extensions.core_api.cast_channel.proto.SocketEvent.details', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='net_return_value', full_name='extensions.core_api.cast_channel.proto.SocketEvent.net_return_value', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_namespace', full_name='extensions.core_api.cast_channel.proto.SocketEvent.message_namespace', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ready_state', full_name='extensions.core_api.cast_channel.proto.SocketEvent.ready_state', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connection_state', full_name='extensions.core_api.cast_channel.proto.SocketEvent.connection_state', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_state', full_name='extensions.core_api.cast_channel.proto.SocketEvent.read_state', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='write_state', full_name='extensions.core_api.cast_channel.proto.SocketEvent.write_state', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_state', full_name='extensions.core_api.cast_channel.proto.SocketEvent.error_state', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='challenge_reply_error_type', full_name='extensions.core_api.cast_channel.proto.SocketEvent.challenge_reply_error_type', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nss_error_code', full_name='extensions.core_api.cast_channel.proto.SocketEvent.nss_error_code', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=730,
)


_AGGREGATEDSOCKETEVENT = _descriptor.Descriptor(
  name='AggregatedSocketEvent',
  full_name='extensions.core_api.cast_channel.proto.AggregatedSocketEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='extensions.core_api.cast_channel.proto.AggregatedSocketEvent.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='endpoint_id', full_name='extensions.core_api.cast_channel.proto.AggregatedSocketEvent.endpoint_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel_auth_type', full_name='extensions.core_api.cast_channel.proto.AggregatedSocketEvent.channel_auth_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='socket_event', full_name='extensions.core_api.cast_channel.proto.AggregatedSocketEvent.socket_event', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes_read', full_name='extensions.core_api.cast_channel.proto.AggregatedSocketEvent.bytes_read', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes_written', full_name='extensions.core_api.cast_channel.proto.AggregatedSocketEvent.bytes_written', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=733,
  serialized_end=987,
)


_LOG = _descriptor.Descriptor(
  name='Log',
  full_name='extensions.core_api.cast_channel.proto.Log',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aggregated_socket_event', full_name='extensions.core_api.cast_channel.proto.Log.aggregated_socket_event', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_evicted_aggregated_socket_events', full_name='extensions.core_api.cast_channel.proto.Log.num_evicted_aggregated_socket_events', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_evicted_socket_events', full_name='extensions.core_api.cast_channel.proto.Log.num_evicted_socket_events', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=990,
  serialized_end=1172,
)

_SOCKETEVENT.fields_by_name['type'].enum_type = _EVENTTYPE
_SOCKETEVENT.fields_by_name['ready_state'].enum_type = _READYSTATE
_SOCKETEVENT.fields_by_name['connection_state'].enum_type = _CONNECTIONSTATE
_SOCKETEVENT.fields_by_name['read_state'].enum_type = _READSTATE
_SOCKETEVENT.fields_by_name['write_state'].enum_type = _WRITESTATE
_SOCKETEVENT.fields_by_name['error_state'].enum_type = _ERRORSTATE
_SOCKETEVENT.fields_by_name['challenge_reply_error_type'].enum_type = _CHALLENGEREPLYERRORTYPE
_AGGREGATEDSOCKETEVENT.fields_by_name['channel_auth_type'].enum_type = _CHANNELAUTH
_AGGREGATEDSOCKETEVENT.fields_by_name['socket_event'].message_type = _SOCKETEVENT
_LOG.fields_by_name['aggregated_socket_event'].message_type = _AGGREGATEDSOCKETEVENT
DESCRIPTOR.message_types_by_name['SocketEvent'] = _SOCKETEVENT
DESCRIPTOR.message_types_by_name['AggregatedSocketEvent'] = _AGGREGATEDSOCKETEVENT
DESCRIPTOR.message_types_by_name['Log'] = _LOG
DESCRIPTOR.enum_types_by_name['EventType'] = _EVENTTYPE
DESCRIPTOR.enum_types_by_name['ChannelAuth'] = _CHANNELAUTH
DESCRIPTOR.enum_types_by_name['ReadyState'] = _READYSTATE
DESCRIPTOR.enum_types_by_name['ConnectionState'] = _CONNECTIONSTATE
DESCRIPTOR.enum_types_by_name['ReadState'] = _READSTATE
DESCRIPTOR.enum_types_by_name['WriteState'] = _WRITESTATE
DESCRIPTOR.enum_types_by_name['ErrorState'] = _ERRORSTATE
DESCRIPTOR.enum_types_by_name['ChallengeReplyErrorType'] = _CHALLENGEREPLYERRORTYPE

SocketEvent = _reflection.GeneratedProtocolMessageType('SocketEvent', (_message.Message,), dict(
  DESCRIPTOR = _SOCKETEVENT,
  __module__ = 'logging_pb2'
  # @@protoc_insertion_point(class_scope:extensions.core_api.cast_channel.proto.SocketEvent)
  ))
_sym_db.RegisterMessage(SocketEvent)

AggregatedSocketEvent = _reflection.GeneratedProtocolMessageType('AggregatedSocketEvent', (_message.Message,), dict(
  DESCRIPTOR = _AGGREGATEDSOCKETEVENT,
  __module__ = 'logging_pb2'
  # @@protoc_insertion_point(class_scope:extensions.core_api.cast_channel.proto.AggregatedSocketEvent)
  ))
_sym_db.RegisterMessage(AggregatedSocketEvent)

Log = _reflection.GeneratedProtocolMessageType('Log', (_message.Message,), dict(
  DESCRIPTOR = _LOG,
  __module__ = 'logging_pb2'
  # @@protoc_insertion_point(class_scope:extensions.core_api.cast_channel.proto.Log)
  ))
_sym_db.RegisterMessage(Log)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)
