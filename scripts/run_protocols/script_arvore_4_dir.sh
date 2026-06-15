#!/usr/bin/env bash
set -e
MESH_DIR="${MESH_DIR:-../data/meshes}"

./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs XxYy
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs XxYy
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs XxYy
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs xYzZ
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs xYzZ
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xYzZ
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs YyxX
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs YyxX
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs YyxX
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs yZxX
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs yZxX
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs yZxX
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs ZzYy
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs ZzYy
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs ZzYy
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs zXYy
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs zXYy
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs zXYy

