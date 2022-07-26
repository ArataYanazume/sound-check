#!/bin/sh

# config ファイルの読込み
script_path="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
config_path="${script_path}/config.sh"
source $config_path

# docker の起動
docker image build -t ${container_image}:${container_version} -f Dockerfile .
docker container run -it ${container_image}:${container_version}