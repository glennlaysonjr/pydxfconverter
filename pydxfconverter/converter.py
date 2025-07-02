import numpy
from stl import mesh
import ezdxf

def stl_to_dxf(stl_file_path, dxf_file_path):
    """
    Converts an STL file to a DXF file using MESH entities for better 3D representation.

    Args:
        stl_file_path (str): The path to the input STL file.
        dxf_file_path (str): The path to the output DXF file.
    """
    try:
        # Load the STL mesh
        your_mesh = mesh.Mesh.from_file(stl_file_path)

        # Create a new DXF document
        doc = ezdxf.new()
        msp = doc.modelspace()

        # Get unique vertices and faces
        vectors = your_mesh.vectors
        unique_vertices, face_indices = numpy.unique(vectors.reshape(-1, 3), axis=0, return_inverse=True)
        faces = face_indices.reshape(-1, 3)

        # Add the mesh to the modelspace
        mesh_entity = msp.add_mesh()
        with mesh_entity.edit_data() as mesh_data:
            mesh_data.vertices = unique_vertices.tolist()
            mesh_data.faces = faces.tolist()

        # Save the DXF document
        doc.saveas(dxf_file_path)
        print(f"Successfully converted {stl_file_path} to {dxf_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Convert STL files to DXF.')
    parser.add_argument('stl_file', help='The input STL file path.')
    parser.add_argument('dxf_file', help='The output DXF file path.')
    args = parser.parse_args()
    stl_to_dxf(args.stl_file, args.dxf_file)

if __name__ == '__main__':
    main()