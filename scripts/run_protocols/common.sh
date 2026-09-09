#!/usr/bin/env bash
set -euo pipefail

PROTOCOL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${PROTOCOL_DIR}/../.." && pwd)"
MESH_DIR="${MESH_DIR:-${REPO_ROOT}/data/meshes}"

if [[ -z "${MONODOMAIN:-}" ]]; then
  if command -v monodomain >/dev/null 2>&1; then
    MONODOMAIN="$(command -v monodomain)"
  elif [[ -x "${REPO_ROOT}/code/cardiaxFull/build/app/monodomain" ]]; then
    MONODOMAIN="${REPO_ROOT}/code/cardiaxFull/build/app/monodomain"
  elif [[ -x "${PWD}/monodomain" ]]; then
    MONODOMAIN="${PWD}/monodomain"
  else
    echo "Set MONODOMAIN=/path/to/monodomain or add monodomain to PATH." >&2
    exit 1
  fi
fi
