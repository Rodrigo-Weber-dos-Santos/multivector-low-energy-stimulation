#include "box_mesh.hpp"

BoxMesh::BoxMesh(double x0, double x1, double y0, double y1, double z0, double z1, int n)
{
  xmin = x0; xmax = x1;
  ymin = y0; ymax = y1;
  zmin = z0; zmax = z1;

  nx = ny = nz = n;

  create_mesh();
}

BoxMesh::BoxMesh(double x0, double x1, double y0, double y1, double z0, double z1, int nnx, int nny, int nnz)
{
  xmin = x0; xmax = x1;
  ymin = y0; ymax = y1;
  zmin = z0; zmax = z1;

  nx = nnx;
  ny = nny;
  nz = nnz;

  create_mesh();
}

void BoxMesh::create_mesh()
{
  cout << "Creating BoxMesh\n";

  n_dim = 3;
  n_node = 8;

  double dx = (xmax-xmin)/nx;
  double dy = (ymax-ymin)/ny;
  double dz = (zmax-zmin)/nz;

  // create nodes
  for(int k=0; k<(nz+1); k++)
    for(int j=0; j<(ny+1); j++)
      for(int i=0; i<(nx+1); i++)
      {
        arma::vec3 p;
        p(0) = i*dx;
        p(1) = j*dy;
        p(2) = k*dz;
        add_point(p);
      }

  // create elements
  std::vector<int> edof(8);
  const int offsetxy = (nx+1)*(ny+1);
  for(int k=0; k<nz; k++)
    for(int j=0; j<ny; j++)
      for(int i=0; i<nx; i++)
      {
        int a = i + j*(nx+1) + k*(nx+1)*(ny+1);
        edof[0] = a;
        edof[1] = a + 1;
        edof[2] = a + (nx+1) + 1;
        edof[3] = a + (nx+1);
        edof[4] = offsetxy + a;
        edof[5] = offsetxy + a + 1;
        edof[6] = offsetxy + a + (nx+1) + 1;
        edof[7] = offsetxy + a + (nx+1);
        add_elem(Element(ELEM_HEXA,edof));
      }

}