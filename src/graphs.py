from graphviz import Digraph
import os

# Configuration
CONFIG = {
    "output_dir": "./img",  # Directory to save diagrams
    "centralized_diagram_name": "Centralized_Repository_Structure",
    "decoupled_diagram_name": "Decoupled_Repository_Structure",
    "format": "png",  # Output format (e.g., png, svg)
}

# Ensure output directory exists
os.makedirs(CONFIG["output_dir"], exist_ok=True)

# Function to create and render the centralized repository structure diagram
def create_centralized_diagram():
    diagram = Digraph(name="Centralized Repository Structure", format=CONFIG["format"])
    diagram.attr(label="Option 1: Centralized Repository Structure", labelloc="t", fontsize="16", color="blue")

    # Nodes
    diagram.node("CentralRepo", "Central Repository")
    diagram.node("ChartsDir", "./charts/\n(Helm Charts)", shape="folder")
    diagram.node("ClustersDir", "./clusters/\n(Environment Configs)", shape="folder")
    diagram.node("BootstrapDir", "./bootstrap/\n(ApplicationSet Manifests)", shape="folder")
    diagram.node("ArgoCD", "ArgoCD", shape="ellipse")
    diagram.node("K8sCluster", "Kubernetes Cluster", shape="ellipse")

    # Edges
    diagram.edges([
        ("CentralRepo", "ChartsDir"),
        ("CentralRepo", "ClustersDir"),
        ("CentralRepo", "BootstrapDir"),
        ("BootstrapDir", "ArgoCD"),
        ("ArgoCD", "K8sCluster"),
    ])

    # Render diagram
    output_path = os.path.join(CONFIG["output_dir"], CONFIG["centralized_diagram_name"])
    diagram.render(output_path, cleanup=True)
    print(f"Centralized diagram saved at: {output_path}.{CONFIG['format']}")

# Function to create and render the decoupled repository structure diagram
def create_decoupled_diagram():
    diagram = Digraph(name="Decoupled Repository Structure", format=CONFIG["format"])
    diagram.attr(label="Option 2: Decoupled Repository Structure", labelloc="t", fontsize="16", color="green")

    # Nodes
    diagram.node("HelmRepo", "Repository A\n(Helm Charts)", shape="folder")
    diagram.node("GitOpsRepo", "Repository B\n(GitOps Configurations)", shape="folder")
    diagram.node("ChartReleaser", "Chart Releaser\n(Publish Charts)", shape="box")
    diagram.node("RemoteHelmRepo", "Remote Helm Repository", shape="cylinder")
    diagram.node("DecoupledArgoCD", "ArgoCD", shape="ellipse")
    diagram.node("DecoupledCluster", "Kubernetes Cluster", shape="ellipse")

    # Edges
    diagram.edges([
        ("HelmRepo", "ChartReleaser"),
        ("ChartReleaser", "RemoteHelmRepo"),
        ("GitOpsRepo", "DecoupledArgoCD"),
        ("RemoteHelmRepo", "DecoupledArgoCD"),
        ("DecoupledArgoCD", "DecoupledCluster"),
    ])

    # Render diagram
    output_path = os.path.join(CONFIG["output_dir"], CONFIG["decoupled_diagram_name"])
    diagram.render(output_path, cleanup=True)
    print(f"Decoupled diagram saved at: {output_path}.{CONFIG['format']}")

# Main function
if __name__ == "__main__":
    print("Generating diagrams...")
    create_centralized_diagram()
    create_decoupled_diagram()
    print("Diagrams generation complete.")

