#ifndef HOLZAPFEL_OGDEN_HPP
#define HOLZAPFEL_OGDEN_HPP

#include "hyperelastic_material.hpp"
#include "incompressible_material.hpp"

/*!
 * Holzapfel & Ogden model for passive myocardium
 * 
 * Ref: "Constitutive modelling of passive myocardium:
 *       a structurally based framework for material characterization"
 *       Philosophical Transactions of the Royal Society A, 367, 2009.
 *   
*/

class HolzapfelOgden : public IncompressibleMaterial
{
protected:

  //! Material constants (dimension of stress)
  double a, af, as, afs;

  //! Material constants (dimensionless)
  double b, bf, bs, bfs;     

  //! Auxiliary
  const arma::mat33 I;

public:

  HolzapfelOgden (const std::vector<double> & prm) :    
    IncompressibleMaterial(prm[8]), // kappa
    a(prm[0]), af(prm[1]),
    as(prm[2]), afs(prm[3]),
    b(prm[4]), bf(prm[5]), 
    bs(prm[6]), bfs(prm[7]),
    I(arma::eye<arma::mat>(3,3))
  {
    assert(a >= 0);
    assert(b >= 0);
    assert(af >= 0);
    assert(bf >= 0);
    assert(as >= 0);
    assert(bs >= 0);
    assert(afs >= 0);
    assert(bfs >= 0);
    assert(kappa >= 0);    
    name = "HolzapfelOgden";
    parameters = prm;
  }

  double strain_energy(MaterialData * md, const arma::mat &) const;
  void deviatoric_stress(MaterialData * md, arma::mat & stress) const;
  void deviatoric_elastensor(MaterialData * md, Tensor4 & A) const;
  
};

#endif
