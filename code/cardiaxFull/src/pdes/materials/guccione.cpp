#include "guccione.hpp"

double Guccione::strain_energy(MaterialData * md, const arma::mat & E) const
{
    // Right Cauchy-Green deformation tensor and its trace
    arma::mat C = 2*E + arma::eye<arma::mat>(3,3);

    // Jacobian
    double J = sqrt(arma::det(C));

    // local Lagrangian strain tensor
    arma::mat33 El, R;
    R  = I;
    El = R.t() * E * R;

    double Q = bf*El(0,0)*El(0,0)
             + bt*( El(1,1)*El(1,1) + El(2,2)*El(2,2) + El(1,2)*El(1,2) + El(2,1)*El(2,1) )
             + bfs*( El(0,1)*El(0,1) + El(1,0)*El(1,0) + El(0,2)*El(0,2) + El(2,0)*El(2,0) );

    const double K = parameters[4];
    double term1 = (Cg/2.)*( exp(Q) - 1. );
    double term2 = (K/2.0)*((J-1)*(J-1));
    return term1 + term2;
}

void Guccione::cauchy_stress(MaterialData * md, arma::mat & sigma)  const
{
    throw runtime_error("Guccione: not implemented");
}

void Guccione::piola2_stress(MaterialData * md, arma::mat & S) const
{
    throw runtime_error("Guccione: not implemented");
}

void Guccione::sp_elastensor(MaterialData * md, arma::mat & D) const
{
    throw runtime_error("Guccione: not implemented");
}

void Guccione::mt_elastensor(MaterialData * md, arma::mat & D) const
{
    throw runtime_error("Guccione: not implemented");
}

void Guccione::deviatoric_stress(MaterialData * md, arma::mat & stress) const
{
    throw runtime_error("Guccione: not implemented");
}

void Guccione::deviatoric_elastensor(MaterialData * md, Tensor4 & A) const
{
    throw runtime_error("Guccione: not implemented");
}
