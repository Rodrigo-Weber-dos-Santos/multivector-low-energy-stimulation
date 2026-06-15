#ifndef ELEMENT_H
#define ELEMENT_H

#include <vector>
#include <map>
#include <armadillo>
//#include "util/util.hpp"

enum ElementType 
{
  ELEM_SEGM=1,  // line
  ELEM_TRIG=2,  // triangle
  ELEM_QUAD=3,  // quadrangle
  ELEM_TETRA=4, // tetrahedron
  ELEM_HEXA=5,  // hexahedron
};


/** Geometric element class.
    Holds information about the geometrical elements: points, region, local
    coordinate system (for cardiac electrophysiology problems).
    
    *** Not to be confused with FiniteElement class. ***
*/
class Element
{
public:
    
  //! Constructor (inlined) 
  Element(ElementType et, std::vector<int> pnums, int indx = 1) 
    : eltype(et), pt_nums(pnums), index(indx),
      fiber(), trans(), normal() { }

  //! Constructor with fibers (inlined) 
  Element(ElementType et, std::vector<int> pnums, 
	  arma::vec3 f, arma::vec3 t, arma::vec3 n, int indx = 1)
    : eltype(et), pt_nums(pnums), index(indx),
      fiber(f), trans(t), normal(n) { }

  //! Get element type 
  ElementType get_type() { return eltype; }

  //! Get region index 
  int get_index() const {return index;}

  //! Get reference to pt_nums 
  const std::vector<int>& get_pt_nums() const { return pt_nums; }

  //! Get reference to fiber vector f
  const arma::vec3 & get_fiber() const { return fiber; }

  //! Get reference to transverse vector s
  const arma::vec3 & get_trans() const { return trans; }

  //! Get reference to normal vector n
  const arma::vec3 & get_normal() const { return normal; }  

  //! Set element type 
  void set_eltype(ElementType et) { eltype=et; }

  //! Set index of element's region 
  void set_index(int i) {index = i;}

  //! Set point numbers 
  void set_pt_nums(std::vector<int> pnums) { pt_nums=pnums; }

  //! Set fiber vector f
  void set_fiber(arma::vec3 & f) { fiber = f; }

  //! Set transverse vector s
  void set_trans(arma::vec3 & s) { trans = s; }

  //! Set normal vector n
  void set_normal(arma::vec3 & n) { normal = n; }  

  //! Swap node the order of nodes A and B
  void swap_nums(int a, int b)
  {
    int aux = pt_nums[a];
    pt_nums[a] = pt_nums[b];
    pt_nums[b] = aux;
  }

private:

  //! The element Type 
  ElementType eltype;

  //! Global node numbers
  std::vector<int> pt_nums;

  //! Element index (for domain/region number) 
  int index;

  //! Local material orientation (fiber, transverse and normal) 
  arma::vec3 fiber, trans, normal;  

};


#endif
