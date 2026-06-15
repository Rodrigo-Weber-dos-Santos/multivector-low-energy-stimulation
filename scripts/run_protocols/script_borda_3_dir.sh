#!/usr/bin/env bash
set -e
MESH_DIR="${MESH_DIR:-../data/meshes}"

./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs XxY
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs XxY
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs XxY
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs XxY
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs XxY
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs xYz
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs xYz
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs xYz
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs xYz
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xYz
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs Yyx
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs Yyx
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs Yyx
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs Yyx
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs Yyx
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs yZx
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs yZx
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs yZx
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs yZx
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs yZx
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs ZzY
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs ZzY
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs ZzY
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs ZzY
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs ZzY
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.01 -fs zXY
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.02 -fs zXY
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs zXY
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs zXY
./monodomain -f ${MESH_DIR}/Esfera3Border.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs zXY

