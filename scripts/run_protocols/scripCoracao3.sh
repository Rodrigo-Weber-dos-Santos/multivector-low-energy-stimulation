#!/usr/bin/env bash
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

"${MONODOMAIN}" -f "${MESH_DIR}/teste.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs X
"${MONODOMAIN}" -f "${MESH_DIR}/teste.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs Y
"${MONODOMAIN}" -f "${MESH_DIR}/teste.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs X
"${MONODOMAIN}" -f "${MESH_DIR}/teste.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs Y
"${MONODOMAIN}" -f "${MESH_DIR}/teste.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs X
"${MONODOMAIN}" -f "${MESH_DIR}/teste.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs Y
"${MONODOMAIN}" -f "${MESH_DIR}/teste.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs X
"${MONODOMAIN}" -f "${MESH_DIR}/teste.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs Y
"${MONODOMAIN}" -f "${MESH_DIR}/teste.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs X
"${MONODOMAIN}" -f "${MESH_DIR}/teste.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs Y


