#!/command/with-contenv bashio
# ==============================================================================
# Home Assistant Add-on: Grott
# Configures Grott
# ==============================================================================

if  bashio::config.has_value 'verbose'; then export gverbose="$(bashio::config 'gverbose')"; fi

if ! bashio::services.available "mqtt"; then
    bashio::log.info "No internal MqTT service found"
else
    export gmqttip="$(bashio::services "mqtt" "host")"
    export gmqttport="$(bashio::services "mqtt" "port")"
    export gmqttauth="True"
    export gmqttuser="$(bashio::services "mqtt" "username")"
    export gmqttpassword="$(bashio::services "mqtt" "password")"
fi