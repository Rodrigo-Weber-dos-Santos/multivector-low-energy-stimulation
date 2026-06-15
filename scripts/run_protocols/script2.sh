#!/usr/bin/env bash
set -e
MESH_DIR="${MESH_DIR:-../data/meshes}"

./monodomain -f ${MESH_DIR}/CBG3/CBG3B.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fdx 1.0 -fdy 0.0 -fdz 0.0
./monodomain -f ${MESH_DIR}/CBG3/CBG3B.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fdy 1.0 -fdz 0.0 -fdx 0.0
./monodomain -f ${MESH_DIR}/CBG3/CBG3B.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fdz 1.0 -fdy 0.0 -fdx 0.0
./monodomain -f ${MESH_DIR}/CBG3/CBG3B.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fdx -1.0 -fdy 0.0 -fdz 0.0
./monodomain -f ${MESH_DIR}/CBG3/CBG3B.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fdy -1.0 -fdz 0.0 -fdx 0.0
./monodomain -f ${MESH_DIR}/CBG3/CBG3B.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fdz -1.0 -fdy 0.0 -fdx 0.0
