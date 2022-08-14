#!/command/with-contenv bashio
# ==============================================================================
# Home Assistant Add-on: Grott
# Configures Grott
# ==============================================================================
readonly CONFIG=/opt/config.ini

bashio::log "Configuring Grott using the add-on configuration"

# If config.ini does not exist, create it.
if ! bashio::fs.file_exists "$CONFIG"; then
    bashio::log "Creating default configuration..."
    bashio::log "Timezone: $(bashio::info.timezone)"
    crudini --set "$CONFIG" Generic mode "proxy"
fi

if  bashio::config.has_value 'verbose'; then 
    bashio::log "Setting verbose"
    crudini --set "$CONFIG" Generic verbose "$(bashio::config 'verbose')" 
fi

if  bashio::config.has_value 'mqtt_ip'; then 
    bashio::log "Setting MQTT IP"
    crudini --set "$CONFIG" MQTT nomqtt "False" 
    crudini --set "$CONFIG" MQTT ip "$(bashio::config 'mqtt_ip')" 
fi

if  bashio::config.has_value 'mqtt_port'; then 
    bashio::log "Setting MQTT port"
    crudini --set "$CONFIG" MQTT port "$(bashio::config 'mqtt_port')" 
fi

if  bashio::config.has_value 'mqtt_user'; then 
    bashio::log "Setting MQTT user"
    crudini --set "$CONFIG" MQTT auth "True" 
    crudini --set "$CONFIG" MQTT user "$(bashio::config 'mqtt_user')" 
fi

if  bashio::config.has_value 'mqtt_password'; then 
    bashio::log "Setting MQTT password"
    crudini --set "$CONFIG" MQTT password "$(bashio::config 'mqtt_password')" 
fi

bashio::log "Done changing configuration"