#ifndef GUCCIONE_HPP
#define GUCCIONE_HPP

#include "hyperelastic_material.hpp"
#include "incompressible_material.hpp"

/**
 * Guccione et al model
 */

class Guccione : public IncompressibleMaterial
{
protected:

    //! Material constants (dimension of stress)
    double Cg;

    //! Material constants (dimensionless)
    double bf, bt, bfs;

    //! Auxiliary
    const arma::mat33 I;

public:
    Guccione (const std::vector<double> & prm) :
            IncompressibleMaterial(prm[4]),
            Cg(prm[0]), bf(prm[1]),
            bt(prm[2]), bfs(prm[3]),
            I(arma::eye<arma::mat>(3,3))
    {
        assert(Cg >= 0);
        assert(bf >= 0);
        assert(bt >= 0);
        assert(bfs >= 0);
        name = "Guccione";
        parameters = prm;
    }

    double strain_energy(MaterialData * md, const arma::mat &) const;

    void piola2_stress(MaterialData * md, arma::mat & S) const;

    void cauchy_stress(MaterialData * md, arma::mat & sigma) const;

    void sp_elastensor(MaterialData * md, arma::mat & D) const;

    void mt_elastensor(MaterialData * md, arma::mat & D) const;

    void deviatoric_stress(MaterialData * md, arma::mat & stress) const;

    void deviatoric_elastensor(MaterialData * md, Tensor4 & A) const;

};


#endif /* GUCCIONE_HPP */
