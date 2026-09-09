#!/usr/bin/env bash
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs x
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs y
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs x
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs y
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs x
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs y
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs x
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs y
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs x
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs y
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs xX
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs yY
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs xX
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs yY
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs xX
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs yY
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs xX
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs yY
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xX
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs yY
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs xXyY
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs yYxX
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs xXyY
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs yYxX
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs xXyY
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs yYxX
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs xXyY
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs yYxX
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xXyY
"${MONODOMAIN}" -f "${MESH_DIR}/testeH1.xml" -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs yYxX


