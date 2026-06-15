#!/usr/bin/env bash
set -e
MESH_DIR="${MESH_DIR:-../data/meshes}"

./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs xXyY
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs yYxX
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xXyY
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs yYxX
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs xXy
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs yYx
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs xXy
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs yYx
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs xXy
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs yYx
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs xXy
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs yYx
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xXy
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs yYx


