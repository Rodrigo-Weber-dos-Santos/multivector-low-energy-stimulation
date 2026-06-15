#!/usr/bin/env bash
set -e
MESH_DIR="${MESH_DIR:-../data/meshes}"

./monodomain -f ${MESH_DIR}/testeNo2.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs x
./monodomain -f ${MESH_DIR}/testeNo2.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs y
./monodomain -f ${MESH_DIR}/testeNo2.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs X
./monodomain -f ${MESH_DIR}/testeNo2.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs Y


