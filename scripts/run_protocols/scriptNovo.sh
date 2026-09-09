#!/usr/bin/env bash
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

"${MONODOMAIN}" -f "${MESH_DIR}/CBG2_100/CBG2B_100.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs x
"${MONODOMAIN}" -f "${MESH_DIR}/CBG2_100/CBG2B_100.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xXzZ
"${MONODOMAIN}" -f "${MESH_DIR}/CBG3_100/CBG3B_100.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs x
"${MONODOMAIN}" -f "${MESH_DIR}/CBG3_100/CBG3B_100.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xXzZ
"${MONODOMAIN}" -f "${MESH_DIR}/CBG4_100/CBG4B_100.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs x
"${MONODOMAIN}" -f "${MESH_DIR}/CBG4_100/CBG4B_100.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xXzZ
