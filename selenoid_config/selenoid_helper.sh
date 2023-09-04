#!/bin/sh

# shellcheck disable=SC2164
cd ./selenoid_config

# Find selenoid config manager
CM=$(ls -a cm_*)
echo "Config Manager: $CM"
chmod +x "$CM"

# Start selenoid
bash "$CM" selenoid start --vnc

# Get browsers.json path
browsers_file_path=$(bash "$CM" selenoid status | grep "Selenoid configuration file is" | awk '{print $NF}')
echo $(cat /selenoid/browser_example.json)

# Write desirable browsers into browsers.json
echo $(cat selenoid/browser_example.json) > "$browsers_file_path"
echo "$browsers_file_path"

# Parse the JSON contents and extract the image paths
image_paths=$(echo $(cat "$browsers_file_path") | grep -o '"image": "[^"]*' | awk -F': "' '{print $2}')

# Loop through image paths and pull Docker images
echo "Pull Docker Images"
for image_path in $image_paths; do
    docker pull "$image_path"
done

# Reboot selenoid
bash "$CM" selenoid stop
bash "$CM" selenoid start