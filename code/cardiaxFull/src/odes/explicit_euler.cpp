#include "explicit_euler.hpp"

ExplicitEuler::ExplicitEuler(CellModel *model) 
  : ODESolver(model), dydt(model->get_num_state_vars())
{
  cout << "ODE solver: Explicit Euler" << endl;
}

void ExplicitEuler::advance(double * y, double & t, double & dt)
{
  const int n = ode->get_num_state_vars();
  
  //t = t  * 12.9;
  //y[0] = (y[0] + 80)/100;
  

 //   

  // Evaluate ODE rhs equations
  //if(y[0] <= 50 && y[0] >= -100){
      ode->equation(t, y, dydt.memptr());
  
      // Advance
      for (int i=0; i<n; i++)
      {  
        // RL GAMB
        if(ode->rlvars.find(i) != ode->rlvars.end()){
          y[i] = dydt(i);
        }else
          y[i] += dt * dydt(i);
      }
    if(y[0] > 50) y[0] = 50;
    if(y[0] < -120) y[0] = -120;
  //} 
  

  //y[0] = 100*y[0] - 80;
  
}

