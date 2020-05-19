from predictionio import EventClient
from datetime import datetime
import pytz
client = EventClient('FDUakPq4PpcPUVWrEF-3AsEDRjeXq2k3LWO_5kM1CjxayPmKzXlqlgHRtO5Wh4Xo', "http://10.228.81.5:7070")
print(client)
first_event_properties = {
    "prop1" : 1,
    "prop2" : "value2",
    "prop3" : [1, 2, 3],
    "prop4" : True,
    "prop5" : ["a", "b", "c"],
    "prop6" : 4.56 ,
    }
first_event_time = datetime(
  2004, 12, 13, 21, 39, 45, 618000, pytz.timezone('US/Mountain'))
first_event_response = client.create_event(
    event="my_event",
    entity_type="user",
    entity_id="uid",
    properties=first_event_properties,
    event_time=first_event_time,
)
print(first_event_response)
second_event_properties = {
    "someProperty" : "value1",
    "anotherProperty" : "value2",
    }
# second_event_response = client.create_event(
#     event="my_event",
#     entity_type="user",
#     entity_id="uid",
#     target_entity_type="item",
#     target_entity_id="iid",
#     properties=second_event_properties,
#     event_time=datetime(2014, 12, 13, 21, 38, 45, 618000, pytz.utc))