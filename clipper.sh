#!/bin/bash


cat $1 | sed -e "s|.*gi\|\(.*\)\|g.*|\1|" -e "s|.*gi\|\(.*\)\|r.*|\1|" -e "s|.*gi\|\(.*\)\|d.*|\1|" -e "s|.*_gi_\(.*\)*|\1|"  > clipped



