#!/bin/sh

# Find selenoid config manager
CM=$(ls -a cm_*)
echo "Config Manager: $CM"
chmod +x "$CM"

# Start selenoid
./"$CM" selenoid start --vnc

# Get browsers.json path
browsers_file_path=$(./"$CM" selenoid status | grep "Selenoid configuration file is" | awk '{print $NF}')

# Write desirable browsers into browsers.json
echo $(cat browser_example.json) > "$browsers_file_path"
echo "$browsers_file_path"

# Parse the JSON contents and extract the image paths
image_paths=$(echo $(cat "$browsers_file_path") | grep -o '"image": "[^"]*' | awk -F': "' '{print $2}')

# Loop through image paths and pull Docker images
echo "Pull Docker Images"
for image_path in $image_paths; do
    docker pull "$image_path"
done

# Reboot selenoid
./"$CM" selenoid stop
./"$CM" selenoid start