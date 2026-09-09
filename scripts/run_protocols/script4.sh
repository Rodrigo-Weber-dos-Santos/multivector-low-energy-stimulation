#!/usr/bin/env bash
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

"${MONODOMAIN}" -f "${MESH_DIR}/CBG4_100/CBG4_100.xml" -dt 0.05 -t 70 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.010 -fdx -1.0 -fdy 0.0 -fdz 0.0
"${MONODOMAIN}" -f "${MESH_DIR}/CBG4_100/CBG4_100.xml" -dt 0.05 -t 60 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.015 -fdx -1.0 -fdy 0.0 -fdz 0.0
"${MONODOMAIN}" -f "${MESH_DIR}/CBG4_100/CBG4_100.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.020 -fdx -1.0 -fdy 0.0 -fdz 0.0
"${MONODOMAIN}" -f "${MESH_DIR}/CBG4_100/CBG4_100.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.025 -fdx -1.0 -fdy 0.0 -fdz 0.0
"${MONODOMAIN}" -f "${MESH_DIR}/CBG4_100/CBG4_100.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.030 -fdx -1.0 -fdy 0.0 -fdz 0.0
"${MONODOMAIN}" -f "${MESH_DIR}/CBG4_100/CBG4_100.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.035 -fdx -1.0 -fdy 0.0 -fdz 0.0
"${MONODOMAIN}" -f "${MESH_DIR}/CBG4_100/CBG4_100.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.040 -fdx -1.0 -fdy 0.0 -fdz 0.0
"${MONODOMAIN}" -f "${MESH_DIR}/CBG4_100/CBG4_100.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.045 -fdx -1.0 -fdy 0.0 -fdz 0.0
"${MONODOMAIN}" -f "${MESH_DIR}/CBG4_100/CBG4_100.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.050 -fdx -1.0 -fdy 0.0 -fdz 0.0
