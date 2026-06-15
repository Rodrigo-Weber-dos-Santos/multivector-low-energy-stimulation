#!/usr/bin/env bash
set -e
MESH_DIR="${MESH_DIR:-../data/meshes}"

./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs X
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs X
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs X
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs X
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs X
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs x
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs x
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs x
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs x
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs x
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs Y
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs Y
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs Y
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs Y
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs Y
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs y
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs y
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs y
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs y
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs y
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs Z
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs Z
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs Z
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs Z
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs Z
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs z
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs z
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs z
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs z
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs z

