#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"

# Paper-aligned WLEL baseline bundle.
for script in \
  cyclenet.sh \
  informer.sh \
  patchtst.sh \
  segrnn.sh \
  seq2peak.sh \
  stid.sh \
  timemixer.sh \
  transformer.sh
do
  echo "============================================================"
  echo "RUNNING $script"
  echo "============================================================"
  bash "$DIR/$script"
done
