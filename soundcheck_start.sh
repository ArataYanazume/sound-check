#!/bin/sh

# config ファイルの読込み
source $(cd $(dirname $0) && pwd)/config.sh

# docker イメージの作成
docker image build \
    -t ${image_name}:${image_version} \
    -f Dockerfile .

# docker コンテナの起動
docker container run \
    --name ${container_name} \
    --rm \
    -it \
    ${image_name}:${image_version}