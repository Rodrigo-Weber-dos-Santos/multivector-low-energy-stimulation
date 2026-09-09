#!/usr/bin/env bash
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs xXyY
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs yYxX
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xXyY
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs yYxX
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs xXy
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs yYx
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs xXy
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs yYx
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs xXy
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs yYx
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs xXy
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs yYx
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xXy
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs yYx


