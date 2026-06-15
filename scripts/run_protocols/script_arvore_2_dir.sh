#!/usr/bin/env bash
set -e
MESH_DIR="${MESH_DIR:-../data/meshes}"

./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs Xx
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs Xx
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs Xx
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs xY
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs xY
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs xY
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs Yy
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs Yy
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs Yy
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs yZ
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs yZ
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs yZ
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs Zz
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs Zz
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs Zz
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.03 -fs zX
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.04 -fs zX
./monodomain -f ${MESH_DIR}/EsferaTree.xml -dt 0.05 -t 100 -pr 1 -c TNNP -m ExplicitEuler -ep monodomain -fa 0.05 -fs zX

