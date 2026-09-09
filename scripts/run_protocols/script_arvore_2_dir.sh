#!/usr/bin/env bash
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs Xx
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs Xx
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs Xx
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs xY
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs xY
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xY
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs Yy
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs Yy
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs Yy
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs yZ
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs yZ
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs yZ
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs Zz
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs Zz
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs Zz
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs zX
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs zX
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs zX

