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
        "name": "Growatt - {0}".format(device),
        "identifiers": device,
        "via_device": "Grott"
    }

    msgs = []
    msgs.append({
        "topic": "homeassistant/sensor/growatt_{0}_string1_power/config".format(device),
        "payload": json.dumps({
            "device_class": "power",
            "state_topic":  stateTopic,
            "value_template": "{{ value_json['values']['pv1watt'] | int / 10 }}",
            "unique_id": "grott_{0}_string1_power".format(device),
            "object_id": "grott_{0}_string1_power".format(device),
            "unit_of_measurement": "W",
            "name": "String 1 - Power",
            "device": deviceObject
        }),
        "retain": True
    });

    msgs.append({
        "topic": "homeassistant/sensor/growatt_{0}_string1_current/config".format(device),
        "payload": json.dumps({
            "device_class": "current",
            "state_topic":  stateTopic,
            "value_template": "{{ value_json['values']['pv1current'] | int / 10 }}",
            "unique_id": "grott_{0}_string1_current".format(device),
            "object_id": "growatt_{0}_string1_current".format(device),
            "unit_of_measurement": "A",
            "name": "String 1 - Current",
            "device": deviceObject
        }),
        "retain": True
    });

    msgs.append({
        "topic": "homeassistant/sensor/growatt_{0}_string1_voltage/config".format(device),
        "payload": json.dumps({
            "device_class": "voltage",
            "state_topic":  stateTopic,
            "value_template": "{{ value_json['values']['pv1voltage'] | int / 10 }}",
            "unique_id": "grott_{0}_string1_voltage".format(device),
            "object_id": "growatt_{0}_string1_voltage".format(device),
            "unit_of_measurement": "V",
            "name": "String 1 - Voltage",
            "device": deviceObject
        }),
        "retain": True
    });

    msgs.append({
        "topic": "homeassistant/sensor/growatt_{0}_string2_power/config".format(device),
        "payload": json.dumps({
            "device_class": "power",
            "state_topic":  stateTopic,
            "value_template": "{{ value_json['values']['pv2watt'] | int / 10 }}",
            "unique_id": "grott_{0}_string2_power".format(device),
            "object_id": "growatt_{0}_string2_power".format(device),
            "unit_of_measurement": "W",
            "name": "String 2 - Power",
            "device": deviceObject
        }),
        "retain": True
    });

    msgs.append({
        "topic": "homeassistant/sensor/growatt_{0}_string2_current/config".format(device),
        "payload": json.dumps({
            "device_class": "current",
            "state_topic":  stateTopic,
            "value_template": "{{ value_json['values']['pv2current'] | int / 10 }}",
            "unique_id": "grott_{0}_string2_current".format(device),
            "object_id": "growatt_{0}_string2_current".format(device),
            "unit_of_measurement": "A",
            "name": "String 2 - Current",
            "device": deviceObject
        }),
        "retain": True
    });

    msgs.append({
        "topic": "homeassistant/sensor/growatt_{0}_string2_voltage/config".format(device),
        "payload": json.dumps({
            "device_class": "voltage",
            "state_topic":  stateTopic,
            "value_template": "{{ value_json['values']['pv2voltage'] | int / 10 }}",
            "unique_id": "grott_{0}_string2_voltage".format(device),
            "object_id": "growatt_{0}_string2_voltage".format(device),
            "unit_of_measurement": "V",
            "name": "String 2 - Voltage",
            "device": deviceObject
        }),
        "retain": True
    });

    msgs.append({
        "topic": "homeassistant/sensor/growatt_{0}_power_input/config".format(device),
        "payload": json.dumps({
            "device_class": "power",
            "state_topic":  stateTopic,
            "value_template": "{{ value_json['values']['pvpowerin'] | int / 10 }}",
            "unique_id": "grott_{0}_power_input".format(device),
            "object_id": "growatt_{0}_power_input".format(device),
            "unit_of_measurement": "W",
            "name": "Power input",
            "device": deviceObject
        }),
        "retain": True
    });

    msgs.append({
        "topic": "homeassistant/sensor/growatt_{0}_power_output/config".format(device),
        "payload": json.dumps({
            "device_class": "power",
            "state_topic":  stateTopic,
            "value_template": "{{ value_json['values']['pvpowerout'] | int / 10 }}",
            "unique_id": "grott_{0}_power_output".format(device),
            "object_id": "growatt_{0}_power_output".format(device),
            "unit_of_measurement": "W",
            "name": "Power output",
            "device": deviceObject
        }),
        "retain": True
    });

    msgs.append({
        "topic": "homeassistant/sensor/growatt_{0}_grid_frequency/config".format(device),
        "payload": json.dumps({
            "device_class": "frequency",
            "state_topic":  stateTopic,
            "value_template": "{{ value_json['values']['pvfrequentie'] | int / 100 }}",
            "unique_id": "grott_{0}_grid_frequency".format(device),
            "object_id": "growatt_{0}_grid_frequency".format(device),
            "unit_of_measurement": "Hz",
            "name": "Grid frequency",
            "icon": "mdi:waveform",
            "device": deviceObject
        }),
        "retain": True
    });

    msgs.append({
        "topic": "homeassistant/sensor/growatt_{0}_phase_voltage/config".format(device),
        "payload": json.dumps({
            "device_class": "voltage",
            "state_topic":  stateTopic,
            "value_template": "{{ value_json['values']['pvgridvoltage'] | int / 10 }}",
            "unique_id": "grott_{0}_phase_voltage".format(device),
            "object_id": "growatt_{0}_phase_voltage".format(device),
            "unit_of_measurement": "V",
            "name": "Phase voltage",
            "device": deviceObject
        }),
        "retain": True
    });

    msgs.append({
        "topic": "homeassistant/sensor/growatt_{0}_energy_today/config".format(device),
        "payload": json.dumps({
            "device_class": "energy",
            "state_topic":  stateTopic,
            "value_template": "{{ value_json['values']['pvenergytoday'] | int / 10 }}",
            "unique_id": "grott_{0}_energy_today".format(device),
            "object_id": "growatt_{0}_energy_today".format(device),
            "unit_of_measurement": "kWh",
            "name": "Generated energy (today)",
            "icon": "mdi:solar-power",
            "last_reset": "1970-01-01T00:00:00+00:00",
            "state_class": "measurement",
            "device": deviceObject
        }),
        "retain": True
    });

    msgs.append({
        "topic": "homeassistant/sensor/growatt_{0}_energy_total/config".format(device),
        "payload": json.dumps({
            "device_class": "energy",
            "state_topic":  stateTopic,
            "value_template": "{{ value_json['values']['pvenergytotal'] | int / 10 }}",
            "unique_id": "grott_{0}_energy_total".format(device),
            "object_id": "growatt_{0}_energy_total".format(device),
            "unit_of_measurement": "kWh",
            "name": "Generated energy (total)",
            "icon": "mdi:solar-power",
            "last_reset": "1970-01-01T00:00:00+00:00",
            "state_class": "total_increasing",
            "device": deviceObject
        }),
        "retain": True
    });

    msgs.append({
        "topic": "homeassistant/sensor/growatt_{0}_inverter_temperature/config".format(device),
        "payload": json.dumps({
            "device_class": "temperature",
            "state_topic":  stateTopic,
            "value_template": "{{ value_json['values']['pvtemperature'] | int / 10 }}",
            "unique_id": "grott_{0}_inverter_temperature".format(device),
            "object_id": "growatt_{0}_inverter_temperature".format(device),
            "unit_of_measurement": "°C",
            "name": "Inverter temperature",
            "device": deviceObject
        }),
        "retain": True
    });
    
    try:
        publish.multiple(msgs, hostname=conf.mqttip,port=conf.mqttport, client_id="grott_autodiscovery", keepalive=60, auth=conf.pubauth)
        if conf.verbose: print("\t - " + 'MQTT messages sent') 
    except TimeoutError:     
        if conf.verbose: print("\t - " + 'MQTT connection time out error') 
    except ConnectionRefusedError:     
        if conf.verbose: print("\t - " + 'MQTT connection refused by target')     
    except BaseException as error:     
        if conf.verbose: print("\t - "+ 'MQTT send failed:', str(error)) 

    with open_makedirs(deviceFile, 'a') as f:
        f.write("")

    return resultcode