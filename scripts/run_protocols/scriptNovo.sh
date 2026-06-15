#!/usr/bin/env bash
set -e
MESH_DIR="${MESH_DIR:-../data/meshes}"

./monodomain -f ${MESH_DIR}/CBG2_100/CBG2B_100.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs x
./monodomain -f ${MESH_DIR}/CBG2_100/CBG2B_100.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xXzZ
./monodomain -f ${MESH_DIR}/CBG3_100/CBG3B_100.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs x
./monodomain -f ${MESH_DIR}/CBG3_100/CBG3B_100.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xXzZ
./monodomain -f ${MESH_DIR}/CBG4_100/CBG4B_100.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs x
./monodomain -f ${MESH_DIR}/CBG4_100/CBG4B_100.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xXzZ
