import vtk
reader = vtk.vtkDataSetReader()
reader.SetFileName("TreeNterm_2.vtk")
pontosFile = open("pontos_tree2.txt", 'w+')
linhasFile = open("linhas_tree2.txt", 'w+')
reader.ReadAllScalarsOn()  # Activate the reading of all scalars
reader.Update()
data=reader.GetOutput()
nPoints = data.GetNumberOfPoints()
for x in range(0, nPoints):
	pontosFile.write(str(data.GetPoint(x)[0]))
	pontosFile.write("\t")
	pontosFile.write(str(data.GetPoint(x)[1]))
	pontosFile.write("\t")
	pontosFile.write(str(data.GetPoint(x)[2]))
	pontosFile.write("\n")
nLines = data.GetNumberOfLines()
lines = data.GetLines()
raios = data.GetCellData().GetArray(reader.GetScalarsNameInFile(1))
for x in range(0, nLines):
    linhasFile.write(str(lines.GetData().GetValue(x*3+1)))
    linhasFile.write("\t")
    linhasFile.write(str(lines.GetData().GetValue(x*3+2)))
    linhasFile.write("\t")
    linhasFile.write(str(raios.GetValue(x)/2))
    linhasFile.write("\n")

pontosFile.close
linhasFile.close
