#!/bin/sh -e

echo "Creating local directories..."
mkdir /home/pi/oasis-grow/configs
mkdir /home/pi/oasis-grow/data_out
mkdir /home/pi/oasis-grow/data_out/image_feed
mkdir /home/pi/oasis-grow/data_out/sensor_feed
mkdir /home/pi/oasis-grow/data_out/logs

echo "Moving configuration files..."
cp /home/pi/oasis-grow/default_configs/hardware_config_default_template.json /home/pi/oasis-grow/configs/hardware_config.json
cp /home/pi/oasis-grow/default_configs/access_config_default_template.json /home/pi/oasis-grow/configs/access_config.json
cp /home/pi/oasis-grow/default_configs/feature_toggles_default_template.json /home/pi/oasis-grow/configs/feature_toggles.json
cp /home/pi/oasis-grow/default_configs/device_state_default_template.json /home/pi/oasis-grow/configs/device_state.json
cp /home/pi/oasis-grow/default_configs/device_params_default_template.json /home/pi/oasis-grow/configs/device_params.json
cp /home/pi/oasis-grow/default_configs/sensor_info_default_template.json /home/pi/oasis-grow/data_out/sensor_info.json

echo "Creating new lock_file..."
cp /home/pi/oasis-grow/default_configs/locks_default_template.json /home/pi/oasis-grow/configs/locks.json

#Deprecated
#echo "Creating placeholder image..."
#cp /home/pi/oasis-grow/default_configs/default_placeholder_image.jpg /home/pi/oasis-grow/data_out/image.jpg
