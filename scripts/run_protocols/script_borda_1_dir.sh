#!/usr/bin/env bash
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs X
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs X
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs X
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs X
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs X
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs x
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs x
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs x
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs x
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs x
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs Y
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs Y
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs Y
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs Y
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs Y
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs y
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs y
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs y
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs y
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs y
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs Z
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs Z
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs Z
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs Z
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs Z
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs z
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs z
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs z
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs z
"${MONODOMAIN}" -f "${MESH_DIR}/EsferaTree.xml" -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs z

