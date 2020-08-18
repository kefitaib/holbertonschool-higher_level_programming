#!/bin/bash
curl -sI "$1" | grep Length | cut -d' ' -f2
