#!/bin/bash
set -e
TMP_DIR=$(mktemp -d)
git clone https://github.com/beeware/toga.git "$TMP_DIR"
rm -rf ./testbed
cp -r "$TMP_DIR/testbed" .
rm -rf "$TMP_DIR"
cd testbed
patch -p1 < ../testbed.patch
cd ..
echo "testbed directory updated successfully."
