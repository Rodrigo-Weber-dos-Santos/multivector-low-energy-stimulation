#include "petsc_linear_solver.hpp"

namespace petsc
{

void LinearSolver::init()
{
  ierr = KSPCreate(PETSC_COMM_WORLD, &_ksp);
  CHKERRABORT(PETSC_COMM_WORLD, ierr);

  set_solver_type();

  // Set runtime options, e.g.,
  // -ksp_type <type> -pc_type <type> -ksp_monitor -ksp_rtol <rtol>
  //
  // These options will override those specified above as long as
  // KSPSetFromOptions() is called _after_ any other customization
  // routines.

  ierr = KSPSetFromOptions (_ksp);
  CHKERRABORT(PETSC_COMM_WORLD,ierr);
}

void LinearSolver::converged_reason()
{
  KSPConvergedReason kr;
  ierr = KSPGetConvergedReason(_ksp, &kr);
  CHKERRABORT(PETSC_COMM_WORLD,ierr);

  cout << endl;
  cout << "PETSc KSP Converged Reason = " << kr << endl;
  cout << endl;
}

void LinearSolver::set_solver_type()
{
//  ierr = KSPSetType(_ksp, KSPCG);
//  ierr = KSPSetType(_ksp, KSPGMRES);

  ierr = KSPGetPC(_ksp, &_pc);
  CHKERRABORT(PETSC_COMM_WORLD,ierr);

//  ierr = PCSetType(_pc, PCJACOBI);
//  CHKERRABORT(PETSC_COMM_WORLD,ierr);
}

void LinearSolver::set_solver_type(const char * type)
{
  string ksptype(type);
  set_solver_type(ksptype);
}

void LinearSolver::set_solver_type(std::string & type)
{
  if(type == "cg")
  {
    ierr = KSPSetType(_ksp, KSPCG);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }
  else if(type == "bicg")
  {
    ierr = KSPSetType(_ksp, KSPBICG);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }
  else if(type == "gmres")
  {
    ierr = KSPSetType(_ksp, KSPGMRES);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }
  else if(type == "bcgs")
  {
    ierr = KSPSetType(_ksp, KSPBCGS);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }
  else if(type == "tfqmr")
  {
    ierr = KSPSetType(_ksp, KSPTFQMR);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }
  else if(type == "richardson")
  {
    ierr = KSPSetType(_ksp, KSPRICHARDSON);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }

}
  
void LinearSolver::set_preconditioner(const char * type)
{
  string pctype(type);
  set_preconditioner(type);
}

void LinearSolver::set_preconditioner(std::string & type)
{
  ierr = KSPGetPC(_ksp, &_pc);
  CHKERRABORT(PETSC_COMM_WORLD,ierr);

  if(type == "none")
  {
    ierr = PCSetType(_pc, PCNONE);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }
  else if(type == "jacobi")
  {
    ierr = PCSetType(_pc, PCJACOBI);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }
  else if(type == "bjacobi")
  {
    ierr = PCSetType(_pc, PCBJACOBI);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }
  else if(type == "sor")
  {
    ierr = PCSetType(_pc, PCSOR);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }
  else if(type == "eisenstat")
  {
    ierr = PCSetType(_pc, PCEISENSTAT);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }
  else if(type == "icc")
  {
    ierr = PCSetType(_pc, PCICC);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  } 
  else if(type == "ilu")
  {
    ierr = PCSetType(_pc, PCILU);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  } 
  else if(type == "asm")
  {
    ierr = PCSetType(_pc, PCASM);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }   
  else if(type == "lu")      // direct solver
  {
    ierr = PCSetType(_pc, PCLU);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }
  else if(type == "cholesky") // direct solver
  {
    ierr = PCSetType(_pc, PCCHOLESKY);
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }
}

void LinearSolver::set_ordering(const char * otype)
{
  string type(otype);

  if (type == "rcm")
  
{    ierr = PCFactorSetMatOrderingType(_pc,"rcm");
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }
  else if (type == "amd")
  {
    ierr = PCFactorSetMatOrderingType(_pc,"amd");
    CHKERRABORT(PETSC_COMM_WORLD,ierr);
  }
}

std::pair<PetscInt, PetscReal> LinearSolver::solve (petsc::Matrix & A,
                                                    petsc::Vector & x,
                                                    petsc::Vector & b,
                                                    const double tol)
{
  PetscInt its;
  PetscReal rnorm;
  KSPConvergedReason reason;

  // old code
  //ierr = KSPSetOperators(_ksp, A.mat(), A.mat(), SAME_NONZERO_PATTERN);

  ierr = KSPSetOperators(_ksp, A.mat(), A.mat());
  CHKERRABORT(PETSC_COMM_WORLD,ierr);

  ierr = KSPSetTolerances(_ksp, tol, PETSC_DEFAULT, PETSC_DEFAULT, PETSC_DEFAULT);
  CHKERRABORT(PETSC_COMM_WORLD,ierr);

  //ierr = KSPSetInitialGuessNonzero(_ksp, PETSC_TRUE);
  //CHKERRABORT(PETSC_COMM_WORLD,ierr);

  ierr = KSPSetFromOptions(_ksp);
  CHKERRABORT(PETSC_COMM_WORLD,ierr);

  ierr = KSPSolve(_ksp,b.vec(),x.vec());
  CHKERRABORT(PETSC_COMM_WORLD,ierr);

  ierr = KSPGetIterationNumber(_ksp,&its);
  CHKERRABORT(PETSC_COMM_WORLD,ierr);

  ierr = KSPGetResidualNorm(_ksp, &rnorm);
  CHKERRABORT(PETSC_COMM_WORLD,ierr);

  ierr = KSPGetConvergedReason(_ksp, &reason);
  CHKERRABORT(PETSC_COMM_WORLD,ierr);

  if (reason < 0)
  {
    cout << "PETSC Converged Reason = " << reason << endl;
    print_error("petsc_linear_solver.cpp", "solve", "KSP not converged");    
  }
  
  std::pair<PetscInt,PetscReal> ir(its,rnorm);
  return ir;
}
  
void LinearSolver::use_umfpack()
{
  // command line arguments
  //     -ksp_type preonly -pc_type lu -pc_factor_mat_solver_package umfpack

  // -ksp_type preonly
  ierr = KSPSetType(_ksp, KSPPREONLY);
  CHKERRABORT(PETSC_COMM_WORLD, ierr);

  // -pc_type lu
  ierr = PCSetType(_pc, PCLU);
  CHKERRABORT(PETSC_COMM_WORLD, ierr);

  // -pc_factor_mat_solver_package umfpack
  ierr = PCFactorSetMatSolverPackage(_pc, "umfpack");
  CHKERRABORT(PETSC_COMM_WORLD, ierr);
}

void LinearSolver::use_mumps()
{
  // command line arguments
  //     -ksp_type preonly -pc_type lu -pc_factor_mat_solver_package mumps

  // -ksp_type preonly
  ierr = KSPSetType(_ksp, KSPPREONLY);
  CHKERRABORT(PETSC_COMM_WORLD, ierr);

  // -pc_type lu
  ierr = PCSetType(_pc, PCLU);
  CHKERRABORT(PETSC_COMM_WORLD, ierr);

  ierr = PCFactorSetMatSolverPackage(_pc, "mumps");
  CHKERRABORT(PETSC_COMM_WORLD, ierr);
}

void LinearSolver::use_hypre()
{
  // cmdline: 

  // -ksp_type preonly
  //ierr = KSPSetType(_ksp, KSPGMRES);
  //CHKERRABORT(PETSC_COMM_WORLD, ierr);

  // -pc_type lu
  //ierr = PCSetType(_pc, PCHYPRE);
  // CHKERRABORT(PETSC_COMM_WORLD, ierr);
}

void LinearSolver::view()
{
  ierr = KSPView(_ksp,PETSC_VIEWER_STDOUT_WORLD);
  CHKERRABORT(PETSC_COMM_WORLD,ierr);
}

} // namespace PETSc
