#!/usr/bin/env bash

read n
for i in $(seq 1 10)
do
  echo "$n x $i = $((n*i))"
done