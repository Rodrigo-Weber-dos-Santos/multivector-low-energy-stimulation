# CARDIAX
# author: Bernardo Martins Rocha
# mail: bernardomartinsrocha@gmail.com

cmake_minimum_required (VERSION 2.8)
project (Cardiax)

# Configure PETSc dir and arch
set (ENV{PETSC_DIR} "/home/bruno/petsc-3.10.3")
set (ENV{PETSC_ARCH} "arch-linux2-c-debug")
find_path (PETSC_DIR include/petsc.h
  HINTS ENV PETSC_DIR
  PATHS
  ${CMAKE_SYSTEM_PREFIX_PATH}
  DOC "PETSc Directory")
#set(PETSC_ARCH 'arch-linux2-c-debug')

# Configure cmake modules dir
set (CMAKE_C_FLAGS "-O3 -Wall -Wno-deprecated")
set (CMAKE_CXX_FLAGS "-O3 -Wall -Wno-deprecated")
set (CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${PROJECT_SOURCE_DIR}/cmake/Modules)

set (MPI_C_LIBRARIES /home/bruno/petsc-3.10.3/arch-linux2-c-debug/lib)
set (MPI_C_INCLUDE_PATH /home/bruno/petsc-3.10.3/arch-linux2-c-debug/include)
set (MPI_CXX_LIBRARIES /home/bruno/petsc-3.10.3/arch-linux2-c-debug/lib)
set (MPI_CXX_INCLUDE_PATH /home/bruno/petsc-3.10.3/arch-linux2-c-debug/include)

# Find external packages
#find_package(MPI REQUIRED)
find_package(PETSc REQUIRED)
find_package(HDF5 REQUIRED)
find_package(Boost REQUIRED)
find_package(Armadillo REQUIRED)

# Includes and libraries for external packages
#set (PARDISO_LIB /usr/lib/pardiso)

# OLD VTK stuff
#include (${CMAKE_ROOT}/Modules/FindVTK.cmake)
#include (${PROJECT_SOURCE_DIR}/cmake/Modules/FindVTK.cmake)
###if (USE_VTK_FILE)
###   include(${USE_VTK_FILE})
###endif (USE_VTK_FILE)
###find_package(VTK COMPONENTS REQUIRED)


# Directories where the linker should look for library files
link_directories(
  ${MPI_C_LIBRARIES}
  ${MPI_CXX_LIBRARIES}
  ${PETSC_LIBRARIES} 
  ${ARMADILLO_LIBRARIES} 
  ${OPENBLAS_LIB}
  ${HDF5_LIBRARIES}
  )

include_directories (
  ${PROJECT_SOURCE_DIR}/src/  
  ${PROJECT_SOURCE_DIR}/src/util/ 
  ${PROJECT_SOURCE_DIR}/src/linalg/ 
  ${PROJECT_SOURCE_DIR}/src/odes/
  ${PROJECT_SOURCE_DIR}/src/fem/
  ${PROJECT_SOURCE_DIR}/src/pde/
  ${Boost_INCLUDE_DIRS}
  ${PETSC_INCLUDES}
  ${HDF5_INCLUDE_DIR}
  ${ARMADILLO_INCLUDE_DIRS}
  ${MPI_C_INCLUDE_PATH}
  ${MPI_CXX_INCLUDE_PATH}
  )

# Configure some options for compiling or not extra packages, etc... 
option(BUILD_TESTS "Build tests" OFF)     
option(USE_AGOS "Use AGOS for ODE solvers" OFF)
  
add_definitions(${PETSC_DEFINITIONS})
add_subdirectory(src/util)
add_subdirectory(src/linalg)
add_subdirectory(src/mesh)
add_subdirectory(src/fem)
add_subdirectory(src/odes)
add_subdirectory(src/pdes)
add_subdirectory(src/cardiac)
add_subdirectory(src/nls)
add_subdirectory(app)

set(CORELIBS blas hdf5 armadillo mpich Util LinAlg ODE NLS Mesh FEM Cardiac PDE)

if(BUILD_TESTS)
  add_subdirectory(test)   
endif(BUILD_TESTS)

#
#message(STATUS "OK Listing all include directories ")
#get_property(dirs DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY INCLUDE_DIRECTORIES)
#foreach(dir ${dirs})
#  message(STATUS " dir=${dir}")
#endforeach()  

#message(STATUS "OK Listing all library directories ")
#get_property(dirs DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY LINK_DIRECTORIES)
#foreach(dir ${dirs})
#  message(STATUS " dir=${dir}")
#endforeach()  

