#!/bin/bash

dir="path to the files"
for f in "$dir"/*; do
  cat "$f"
done