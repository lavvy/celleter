#!/bin/bash

git clone https://github.com/lavvy/celleter.git

cd celleter

dpkg-buildpackage -b
