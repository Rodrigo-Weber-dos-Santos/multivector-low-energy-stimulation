#include "quadrature.hpp"

// 1D quadrature points
static double quad1d_o1_pt0[3] = {0.0, 0.0, 0.0};
static double quad1d_o2_pt0[3] = {-1.0/sqrt(3), 0.0, 0.0};
static double quad1d_o2_pt1[3] = {1.0/sqrt(3), 0.0, 0.0};

static double quad1d_n3_pt0[3] = {0.0, 0.0, 0.0};
static double quad1d_n3_pt1[3] = {-sqrt(3.0/5.0), 0.0, 0.0};
static double quad1d_n3_pt2[3] = { sqrt(3.0/5.0), 0.0, 0.0};


// 2D quadrature points - tri
static double quadtri_o0_pt0[3] = {1./3., 1./3., 0.};

static double quadtri_o2_pt0[3] = {2./3., 1./6., 1./6.};
static double quadtri_o2_pt1[3] = {1./6., 2./3., 1./6.};
static double quadtri_o2_pt2[3] = {1./6., 1./6., 2./3.};

//static double quadtri_o2_pt0[3] = {0.5, 0.0, 0.0};
//static double quadtri_o2_pt1[3] = {0.0, 0.5, 0.0};
//static double quadtri_o2_pt2[3] = {0.5, 0.5, 0.0};

static double quadtri_o3_pt0[3] = {1.5505102572168219018027159252941e-01,
				   1.7855872826361642311703513337422e-01,
				   0.0};
static double quadtri_o3_pt1[3] = {6.4494897427831780981972840747059e-01,
				   7.5031110222608118177475598324603e-02,
				   0.0};
static double quadtri_o3_pt2[3] = {1.5505102572168219018027159252941e-01,
				   6.6639024601470138670269327409637e-01,
				   0.0};
static double quadtri_o3_pt3[3] = {6.4494897427831780981972840747059e-01,
				   2.8001991549907407200279599420481e-01,
				   0.0};

// 2D quadrature points - quad
static double quadqd_o0_pt0[3] = {-1.0/sqrt(3), -1.0/sqrt(3), 0.0};
static double quadqd_o0_pt1[3] = { 1.0/sqrt(3), -1.0/sqrt(3), 0.0};
static double quadqd_o0_pt2[3] = { 1.0/sqrt(3),  1.0/sqrt(3), 0.0};
static double quadqd_o0_pt3[3] = {-1.0/sqrt(3),  1.0/sqrt(3), 0.0};

// 3D quadrature points - tet
static double quadtet_o0_pt0[3] = {1./3., 1./3., 1./3.};
static double quadtet_o2_pt0[3] = {0.5854101966249685, 
				   0.1381966011250105,
				   0.1381966011250105};
static double quadtet_o2_pt1[3] = {0.1381966011250105, 
				   0.5854101966249685, 
				   0.1381966011250105};
static double quadtet_o2_pt2[3] = {0.1381966011250105, 
				   0.1381966011250105, 
				   0.5854101966249685};
static double quadtet_o2_pt3[3] = {0.1381966011250105, 
				   0.1381966011250105, 
				   0.1381966011250105};

// 3D quadrature points - hex
static double quadhx_o0_pt0[3] = {-1.0/sqrt(3), -1.0/sqrt(3), -1.0/sqrt(3)};
static double quadhx_o0_pt1[3] = { 1.0/sqrt(3), -1.0/sqrt(3), -1.0/sqrt(3)};
static double quadhx_o0_pt2[3] = { 1.0/sqrt(3),  1.0/sqrt(3), -1.0/sqrt(3)};
static double quadhx_o0_pt3[3] = {-1.0/sqrt(3),  1.0/sqrt(3), -1.0/sqrt(3)};
static double quadhx_o0_pt4[3] = {-1.0/sqrt(3), -1.0/sqrt(3),  1.0/sqrt(3)};
static double quadhx_o0_pt5[3] = { 1.0/sqrt(3), -1.0/sqrt(3),  1.0/sqrt(3)};
static double quadhx_o0_pt6[3] = { 1.0/sqrt(3),  1.0/sqrt(3),  1.0/sqrt(3)};
static double quadhx_o0_pt7[3] = {-1.0/sqrt(3),  1.0/sqrt(3),  1.0/sqrt(3)};

static double quadhx_center[3] = {0,0,0};

// Implementations ------------------------------------------------------------

Quadrature * Quadrature::create(int order, ElementType etype)
{
  if (etype == ELEM_SEGM)
  {
    Quadrature1d * q1d = new Quadrature1d(order);
    return q1d;
  }
  else if (etype == ELEM_TRIG)
  {
    QuadratureTri * qtr = new QuadratureTri(order);
    return qtr;
  }
  else if (etype == ELEM_QUAD)
  {
    QuadratureQuad * qqd = new QuadratureQuad(order);
    return qqd;
  }
  else if (etype == ELEM_TETRA)
  {
    QuadratureTetra * qqd = new QuadratureTetra(order);
    return qqd;
  }
  else if (etype == ELEM_HEXA)
  {
    QuadratureHexa * qqd = new QuadratureHexa(order);
    return qqd;
  }
  else
    throw std::runtime_error("quadrature rule not found");

  return NULL;
}

Quadrature1d::Quadrature1d(int order) : Quadrature(order)
{
  switch(order)
  {
  case 0:
  case 1:
    weights.push_back(2.0);
    ipoints.resize(1);
    ipoints[0] = arma::vec3(quad1d_o1_pt0);
    break;
  case 2:
  case 3:
    weights.push_back(1.0);
    weights.push_back(1.0);
    ipoints.resize(2);
    ipoints[0] = arma::vec3(quad1d_o2_pt0);
    ipoints[1] = arma::vec3(quad1d_o2_pt1);
    break;
  case 4:
  case 5:
  case 6:
  case 7:
    weights.push_back(8.0/9.0);
    weights.push_back(5.0/9.0);
    weights.push_back(5.0/9.0);
    ipoints.resize(3);
    ipoints[0] = arma::vec3(quad1d_n3_pt0);
    ipoints[1] = arma::vec3(quad1d_n3_pt1);
    ipoints[2] = arma::vec3(quad1d_n3_pt2);
    break;
  default:
    throw std::runtime_error("invalid 1d integration order");
    break;
  }   
}

QuadratureTri::QuadratureTri(int order) : Quadrature(order)
{

  //! TODO: need to carefully check these rules for triangles
  //! found some different values in the literature
  //! some weights are the half of the values we are using

  switch(order)
  {
  case 0:
  case 1:
    // weights
    for(int i=0; i<4; i++)
      weights.push_back(1.0);
    // points
    ipoints.resize(1);
    ipoints[0] = arma::vec3(quadtri_o0_pt0);
    break;

  case 2:
    // weights
    for(int i=0; i<3; i++)
      weights.push_back(1.0/3.0);
    // points
    ipoints.resize(3);
    ipoints[0] = arma::vec3(quadtri_o2_pt0);
    ipoints[1] = arma::vec3(quadtri_o2_pt1);
    ipoints[2] = arma::vec3(quadtri_o2_pt2);
    break;
  case 3:
    // weights
    weights.resize(4);
    weights[0] = 1.5902069087198858469718450103758e-01;
    weights[1] = 9.0979309128011415302815498962418e-02;
    weights[2] = 1.5902069087198858469718450103758e-01;
    weights[3] = 9.0979309128011415302815498962418e-02;
    // points
    ipoints.resize(4);
    ipoints[0] = arma::vec3(quadtri_o3_pt0);
    ipoints[1] = arma::vec3(quadtri_o3_pt1);
    ipoints[2] = arma::vec3(quadtri_o3_pt2);
    ipoints[3] = arma::vec3(quadtri_o3_pt3);
    break;
  default:
    throw std::runtime_error("invalid tri integration order");
    break;
  }
}

QuadratureQuad::QuadratureQuad(int order) : Quadrature(order)
{
  switch(order)
  {
  case 0: case 1: case 2:
    // weights
    for(int i=0; i<4; i++)
      weights.push_back(1.0);
    // points
    ipoints.resize(4);
    ipoints[0] = arma::vec3(quadqd_o0_pt0);
    ipoints[1] = arma::vec3(quadqd_o0_pt1);
    ipoints[2] = arma::vec3(quadqd_o0_pt2);
    ipoints[3] = arma::vec3(quadqd_o0_pt3);
    break;
  default:
    throw std::runtime_error("invalid quad integration order");
    break;
  }
}

QuadratureTetra::QuadratureTetra(int order) : Quadrature(order)
{
  const double c = 0.0416666666666666666;

  switch(order)
  {
  case 0: case 1:
    // weights
    weights.push_back(2./6.);
    // points
    ipoints.resize(1);
    ipoints[0] = arma::vec3(quadtet_o0_pt0);
    break;

  case 2: case 3: case 4:
    // weights
    // TODO: need to re-check this
    for(int i=0; i<4; i++)
      weights.push_back(c);

    // points
    ipoints.resize(4);
    ipoints[0] = arma::vec3(quadtet_o2_pt0);
    ipoints[1] = arma::vec3(quadtet_o2_pt1);
    ipoints[2] = arma::vec3(quadtet_o2_pt2);
    ipoints[3] = arma::vec3(quadtet_o2_pt3);
    break;

  default:
    throw std::runtime_error("invalid tetra integration order");
    break;
  }
}

QuadratureHexa::QuadratureHexa(int order) : Quadrature(order)
{
  switch(order)
  {
    case -1:
      weights.push_back(8.0);
      ipoints.resize(1);
      ipoints[0] = arma::vec3(quadhx_center);
      break;  
      
    case 0: 
    case 1:
    case 2:
      // weights
      for(int i=0; i<8; i++)
        weights.push_back(1.0);

      // points    
      ipoints.resize(8);
      ipoints[0] = arma::vec3(quadhx_o0_pt0);
      ipoints[1] = arma::vec3(quadhx_o0_pt1);
      ipoints[2] = arma::vec3(quadhx_o0_pt2);
      ipoints[3] = arma::vec3(quadhx_o0_pt3);
      ipoints[4] = arma::vec3(quadhx_o0_pt4);
      ipoints[5] = arma::vec3(quadhx_o0_pt5);
      ipoints[6] = arma::vec3(quadhx_o0_pt6);
      ipoints[7] = arma::vec3(quadhx_o0_pt7);
      break;      
    default:
      throw std::runtime_error("invalid hex integration order");
      break;
  }
}

