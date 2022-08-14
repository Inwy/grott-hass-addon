#!/command/with-contenv bashio
# ==============================================================================
# Home Assistant Add-on: Grott
# Configures Grott
# ==============================================================================
readonly CONFIG=/opt/grott.ini

bashio::log "Configuring Grott using the add-on configuration"

# If config.ini does not exist, create it.
if ! bashio::fs.file_exists "$CONFIG"; then
    bashio::log.info "Creating default configuration..."
    bashio::log "Timezone: $(bashio::info.timezone)"
    crudini --set "$CONFIG" Generic mode "proxy"
fi

if  bashio::config.has_value 'verbose'; then crudini --set "$CONFIG" Generic verbose "$(bashio::config 'verbose')" fi

if  bashio::config.has_value 'mqtt_ip'; then 
    crudini --set "$CONFIG" MQTT nomqtt "False" 
    crudini --set "$CONFIG" MQTT ip "$(bashio::config 'mqtt_ip')" 
fi

if  bashio::config.has_value 'mqtt_port'; then crudini --set "$CONFIG" MQTT port "$(bashio::config 'mqtt_port')" fi

if  bashio::config.has_value 'mqtt_user'; then 
    crudini --set "$CONFIG" MQTT auth "True" 
    crudini --set "$CONFIG" MQTT user "$(bashio::config 'mqtt_user')" 
fi

if  bashio::config.has_value 'mqtt_password'; then crudini --set "$CONFIG" MQTT password "$(bashio::config 'mqtt_password')" fi