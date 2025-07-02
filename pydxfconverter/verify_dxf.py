
import ezdxf

def verify_dxf(dxf_file_path):
    """
    Verifies that the DXF file contains a MESH entity.

    Args:
        dxf_file_path (str): The path to the DXF file.
    """
    try:
        doc = ezdxf.readfile(dxf_file_path)
        msp = doc.modelspace()
        
        # Find all MESH entities
        mesh_entities = msp.query('MESH')
        
        if len(mesh_entities) > 0:
            print(f"Verification successful: Found {len(mesh_entities)} MESH entity in {dxf_file_path}")
            # You could add more detailed checks here if needed
            # For example, check the number of vertices and faces
            mesh_entity = mesh_entities[0]
            print(f"  - Vertices: {len(mesh_entity.vertices)}")
            print(f"  - Faces: {len(mesh_entity.faces)}")
        else:
            print(f"Verification failed: No MESH entity found in {dxf_file_path}")

    except Exception as e:
        print(f"An error occurred during verification: {e}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Verify DXF files.')
    parser.add_argument('dxf_file', help='The DXF file path to verify.')
    args = parser.parse_args()
    verify_dxf(args.dxf_file)

if __name__ == '__main__':
    main()
