#ifndef HYPERELASTIC_MATERIAL_HPP
#define HYPERELASTIC_MATERIAL_HPP

#include <string>
#include <stdexcept>
#include "util/util.hpp"
#include "linalg/tensor.hpp"
#include "pdes/elasticity.hpp"
#include "pdes/mech_utils.hpp"
#include "material_data.hpp"

class HyperelasticMaterial
{
public:

  //! Constructor
  HyperelasticMaterial() {};

  //! Constructor with material parameters
  HyperelasticMaterial(const std::vector<double> & prm);

  //! Destructor
  virtual ~HyperelasticMaterial(){};

  //! Is incompressible
  bool is_incompressible() const { return uncoupled; }

  //! Get the value of the parameter with index i
  double get_param(int i) const;

  //! Get name of the material
  string get_name() const { return name; }

  //! Set the number of dimensions
  void set_ndim(int nd) { ndim = nd; }

  //! Computes PK2 stress using finite difference
  void calc_fd_stress(MaterialData * md, arma::mat & S);

  //! Computes PK2 stress derivative (4th order tensor) using finite difference
  void calc_fd_elastensor(MaterialData * md, arma::mat & D);
    
  //! Computes PK2 stress derivative (4th order tensor) using finite difference
  void calc_fd_elastensor(MaterialData * md, Tensor4 & A);
  
  //! PENALTY TERM: Computes PK2 stress using finite difference
  void calc_fd_stress_penalty(MaterialData * md, arma::mat & S);

  //! PENALTY TERM: Computes PK2 stress derivative (4th order tensor) using finite difference
  void calc_fd_elastensor_penalty(MaterialData * md, arma::mat & D);
  
  //! PENALTY TERM:Computes PK2 stress derivative (4th order tensor) using finite difference
  void calc_fd_elastensor_penalty(MaterialData * md, Tensor4 & A);

  //! Factory method
  static HyperelasticMaterial * create(string name, ElasticityType & elastype,
                                       const std::vector<double> & matprop);

  //! Maps tensor2 to the deformed configuration 
  void push_forward(const arma::mat33 & F, const arma::mat33 & S,
                    arma::mat33 & sigma);

  //! Maps tensor4 to the deformed configuration
  void push_forward(const arma::mat33 & F, Tensor4 & Am, Tensor4 & As);
  
  //! Volumetric penalty term
  double penalty_term(MaterialData * md, const arma::mat &) const;

  // Interface -----------------------------------------------------------------

  //! Strain energy function
  virtual double strain_energy(MaterialData * md, const arma::mat &) const = 0;
   
  //! Cauchy stress tensor
  virtual void cauchy_stress(MaterialData * md, arma::mat & sigma) const = 0;

  //! Second Piola-Kirchhoff stress tensor
  virtual void piola2_stress(MaterialData * md, arma::mat & S) const = 0;

  //! Spatial elasticity (4th order) tensor
  virtual void sp_elastensor(MaterialData * md, arma::mat & D) const = 0;

  //! Material elasticity (4th order) tensor
  virtual void mt_elastensor(MaterialData * md, arma::mat & D) const = 0;

protected:

  //! Number of dimensions
  int ndim;

  //! Is incompressible/uncoupled
  bool uncoupled;

  //! Name of the material
  std::string name;

  //! Vector with material parameters
  std::vector<double> parameters;

};


#endif
