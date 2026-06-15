#ifndef MONODOMAIN_H
#define MONODOMAIN_H

#include "cardiacproblem.hpp"
#include "fem/fem.h"
#include <fstream>

/** 
    This class implements the Monodomain model.
    Conductivities are calculated as follows:
    sigma_k = (sigma_k_i * sigma_k_e)/(sigma_k_i + sigma_k_e)
    where k = l, t or n, denoting longitudinal, transverse and normal
*/

class Monodomain : public CardiacProblem
{
public:

  //! Constructor
  Monodomain();

  //! Destructor
  virtual ~Monodomain();

  //! Perform one time step
  void advance();

  //! Initialize solver (mats, vecs, ics, etc)
  void init();

  //! Set initial conditions on cells
  void initial_conditions();

  //! Set cell state variable value
  void set_stimulus_value(int index, double val);

  //! Solve the problem
  void solve();

  //! Update coordinates (for coupled problem)
  void update_coords(const arma::mat & um);

  //! Read parameters (boundary conditions, coefficients) from file
  void config(std::string optFile);

  void setup_field(double fa, string fs);
  void set_field_direction(char direction);

protected:
  double field_amplitude;
  double field_direction[3];
  string field_setup;
  int field_changes;

  //! Number of degrees of freedom 
  uint ndofs;

  //! Stimulus value
  double stim_val;

  //! Stimulus control
  bool stim_apply;

  //! Nodal stimulus control
  bool stim_apply_nodes;

  //! Nodes to apply stimulus
  std::set<uint> stim_nodes;

  //! Finite element space of the solution
  H1FESpace fespace;

  //! Vector previous transmembrane potential
  //arma::vec vm0;
  
  //! Vector current transmembrane potential
  arma::vec vm;
    

  //! Nodal stimuli values
  arma::vec stim_values;
   
  //! Assembled global mass matrix
  petsc::Matrix Mi;
  
  //! Assembled global stiffness matrix
  petsc::Matrix Ai;

  //! Vector of solutions
  petsc::Vector v0, v1, f;

  //! PETSc linear solver handler
  petsc::LinearSolver solver;

  ofstream fileout;
  bool *activate;

  //! Assemble mass and stiffness matrix for solving monodomain
  virtual void assemble_matrices();

  //! Compute element conductivity tensor
  void calc_cond_tensor(const int index, const int ndim, arma::mat & sigma);

  //! Compute element stiffness matrix
  virtual void calc_elmat_stiff(const int eindex, const FiniteElement & fe,
                                arma::mat & elmat);

  //! Compute element mass matrix
  void calc_elmat_mass(const int eindex, const FiniteElement & fe,
                       arma::mat & elmat);

  //! Get Robin boundary condition vector
  double coeff_robin_vec(int index, int ie);

  //! Computes the vector associated with boundary conditions
  void calc_robin_elvec (const int iel, const FiniteElement & fe,
												 const ScalarFunction<double> & gD, 
												 const ScalarFunction<double> & gN,
												 arma::vec & elvec);

  //! Neumann boundary conditions description
  std::map<int,double> neumann_map;

  //! Dirichlet boundary (edge or surface) conditions description
  std::map<int,double> dirichlet_map;

  //! Dirichlet boundary (at the nodes) conditions description
  std::map<int,double> fixed_nodes_map;

  
  //! Advance systems of ODEs in time
  void solve_odes();

  //! Solve parabolic problem 
  virtual void solve_parabolic();

};

#endif


