#!/bin/sh

# config ファイルの読込み
source $(cd $(dirname $0) && pwd)/config.sh

# docker イメージの作成
docker image build \
    -t ${container_image}:${container_version} \
    -f \
    Dockerfile .

# docker コンテナの起動
docker container run \
    --name ${container_name} \
    --rm \
    -it \
    ${container_image}:${container_version}