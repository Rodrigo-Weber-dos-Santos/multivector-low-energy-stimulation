#!/usr/bin/env bash
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs XxYy
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs XxYy
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs XxYy
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs xYzZ
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs xYzZ
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xYzZ
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs YyxX
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs YyxX
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs YyxX
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs yZxX
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs yZxX
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs yZxX
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs ZzYy
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs ZzYy
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs ZzYy
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs zXYy
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs zXYy
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs zXYy

