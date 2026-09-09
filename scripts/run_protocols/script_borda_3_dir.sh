#!/usr/bin/env bash
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs XxY
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs XxY
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs XxY
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs XxY
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs XxY
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs xYz
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs xYz
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs xYz
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs xYz
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xYz
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs Yyx
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs Yyx
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs Yyx
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs Yyx
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs Yyx
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs yZx
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs yZx
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs yZx
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs yZx
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs yZx
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs ZzY
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs ZzY
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs ZzY
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs ZzY
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs ZzY
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs zXY
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs zXY
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs zXY
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs zXY
"${MONODOMAIN}" -f "${MESH_DIR}/Esfera3Border.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs zXY

