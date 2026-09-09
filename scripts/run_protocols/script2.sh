#!/usr/bin/env bash
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

"${MONODOMAIN}" -f "${MESH_DIR}/CBG3/CBG3B.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fdx 1.0 -fdy 0.0 -fdz 0.0
"${MONODOMAIN}" -f "${MESH_DIR}/CBG3/CBG3B.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fdy 1.0 -fdz 0.0 -fdx 0.0
"${MONODOMAIN}" -f "${MESH_DIR}/CBG3/CBG3B.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fdz 1.0 -fdy 0.0 -fdx 0.0
"${MONODOMAIN}" -f "${MESH_DIR}/CBG3/CBG3B.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fdx -1.0 -fdy 0.0 -fdz 0.0
"${MONODOMAIN}" -f "${MESH_DIR}/CBG3/CBG3B.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fdy -1.0 -fdz 0.0 -fdx 0.0
"${MONODOMAIN}" -f "${MESH_DIR}/CBG3/CBG3B.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fdz -1.0 -fdy 0.0 -fdx 0.0
