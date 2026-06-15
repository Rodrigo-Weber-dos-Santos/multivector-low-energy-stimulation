#!/usr/bin/env bash
set -e
MESH_DIR="${MESH_DIR:-../data/meshes}"

./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs x
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs y
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs x
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs y
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs x
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs y
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs x
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs y
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs x
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs y
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs xX
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs yY
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs xX
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs yY
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs xX
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs yY
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs xX
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs yY
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xX
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs yY
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs xXyY
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs yYxX
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs xXyY
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs yYxX
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs xXyY
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs yYxX
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs xXyY
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs yYxX
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xXyY
./monodomain -f ${MESH_DIR}/testeH1.xml -dt 0.05 -t 50 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs yYxX


