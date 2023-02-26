#!/command/with-contenv bashio
# ==============================================================================
# Home Assistant Add-on: Grott
# Configures Grott
# ==============================================================================
readonly CONFIG=/opt/grott/config.ini

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

if  bashio::services.available 'mqtt'; then 
    bashio::log "Setting MQTT settings"
    crudini --set "$CONFIG" MQTT nomqtt "False" 
    crudini --set "$CONFIG" MQTT ip "$(bashio::services mqtt "host")" 
    crudini --set "$CONFIG" MQTT port "$(bashio::services mqtt "port")" 
    crudini --set "$CONFIG" MQTT auth "True" 
    crudini --set "$CONFIG" MQTT user "$(bashio::services mqtt "username")" 
    crudini --set "$CONFIG" MQTT password "$(bashio::services mqtt "password")" 
else
    bashio::exit.nok "MQTT service is not available"
fi

if  bashio::config.has_value 'pvoutput'; then 
    bashio::log "Setting PVOutput settings"

    pvOutputSettings = $(bashio::config 'pvoutput')

    crudini --set "$CONFIG" PVOutput pvoutput "True" 
    crudini --set "$CONFIG" PVOutput apikey "$(pvOutputSettings.apikey)"

    inverters = pvOutputSettings.inverters

    if [${#inverters[@]} -gt 1]; then
        crudini --set "$CONFIG" PVOutput pvinterters "$(invertersLenght)"
        for i in pvOutputSettings.inverters:
            inverter = pvOutputSettings.inverters[i]

            crudini --set "$CONFIG" PVOutput "systemid".format "$(pvOutputSettings.inverters[].systemId)"
            crudini --set "$CONFIG" PVOutput systemid "$(pvOutputSettings.inverters[0].systemId)"
    else
        crudini --set "$CONFIG" PVOutput systemid "$(pvOutputSettings.inverters[0].systemId)"
    fi
fi

bashio::log "Done changing configuration"