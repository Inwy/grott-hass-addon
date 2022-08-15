import json
import os
import paho.mqtt.publish as publish

def open_makedirs(filename, *args, **kwargs):
    """ Open file, creating the parent directories if neccesary. """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    return open(filename, *args, **kwargs)

def grottext(conf, data, jsonmsg) :
    """
    Grot extension to send autodiscovery data to home assistant
    """

    resultcode = 0
    outpath = "/opt/devices"

    if conf.verbose : print("\t - " + "Grott extension to send auto discovery data to Home Assistant")

    jsonobj = json.loads(jsonmsg)

    device = jsonobj["device"]
    deviceFile = os.path.join(outpath, "{0}.dat".format(device))
    deviceAlreadyAnnounced = os.path.exists(deviceFile)

    if deviceAlreadyAnnounced :
        if conf.verbose : print("\t - " + "Device {0} already announced to Home Assistant, ignoring".format(device)) 
        return resultcode

    stateTopic = "homeassistant/sensor/growatt_inverter/state"
    deviceObject = {
        "manufacturer": "Growatt",
        "name": "Growatt inverter - {0}".format(device),
        "identifiers": device,
        "via_device": "Grott"
    }

    discoveryObject = {
        "device_class": "power",
        "state_topic":  stateTopic,
        "value_template": "{{ value_json['values']['pv1watt'] | int / 10 }}",
        "unique_id": "growatt_{0}_string1_watt".format(device),
        "unit_of_measurement": "W",
        "name": "Growatt inverter {0} - String 1 (Watt)".format(device),
        "device": deviceObject
    }

    jsonmsg = json.dumps(discoveryObject) 
    mqttTopic = "homeassistant/sensor/growatt_{0}_string1_watt/config".format(device)
    
    try:
        publish.single(mqttTopic, payload=jsonmsg, qos=0, retain=True, hostname=conf.mqttip,port=conf.mqttport, client_id="grott_autodiscovery", keepalive=60, auth=conf.pubauth)
        if conf.verbose: print("\t - " + 'MQTT message message sent') 
    except TimeoutError:     
        if conf.verbose: print("\t - " + 'MQTT connection time out error') 
    except ConnectionRefusedError:     
        if conf.verbose: print("\t - " + 'MQTT connection refused by target')     
    except BaseException as error:     
        if conf.verbose: print("\t - "+ 'MQTT send failed:', str(error)) 

    with open_makedirs(deviceFile, 'a') as f:
        f.write("")

    return resultcode