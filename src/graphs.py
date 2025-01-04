from graphviz import Digraph

# Create a new Digraph for the diagram
diagram = Digraph(name="GitOps Repository Structure", format="png")

# Option 1: Centralized Repository Structure
with diagram.subgraph(name="cluster_centralized") as centralized:
    centralized.attr(label="Option 1: Centralized Repository Structure", fontsize="16", color="blue")
    
    # Nodes for centralized structure
    centralized.node("CentralRepo", "Central Repository")
    centralized.node("ChartsDir", "./charts/\\n(Helm Charts)", shape="folder")
    centralized.node("ClustersDir", "./clusters/\\n(Environment Configs)", shape="folder")
    centralized.node("BootstrapDir", "./bootstrap/\\n(ApplicationSet Manifests)", shape="folder")
    centralized.node("ArgoCD", "ArgoCD", shape="ellipse")
    centralized.node("K8sCluster", "Kubernetes Cluster", shape="ellipse")

    # Edges for centralized structure
    centralized.edges([
        ("CentralRepo", "ChartsDir"),
        ("CentralRepo", "ClustersDir"),
        ("CentralRepo", "BootstrapDir"),
        ("BootstrapDir", "ArgoCD"),
        ("ArgoCD", "K8sCluster")
    ])

# Option 2: Decoupled Repository Structure
with diagram.subgraph(name="cluster_decoupled") as decoupled:
    decoupled.attr(label="Option 2: Decoupled Repository Structure", fontsize="16", color="green")
    
    # Nodes for decoupled structure
    decoupled.node("HelmRepo", "Repository A\\n(Helm Charts)", shape="folder")
    decoupled.node("GitOpsRepo", "Repository B\\n(GitOps Configurations)", shape="folder")
    decoupled.node("ChartReleaser", "Chart Releaser\\n(Publish Charts)", shape="box")
    decoupled.node("RemoteHelmRepo", "Remote Helm Repository", shape="cylinder")
    decoupled.node("DecoupledArgoCD", "ArgoCD", shape="ellipse")
    decoupled.node("DecoupledCluster", "Kubernetes Cluster", shape="ellipse")

    # Edges for decoupled structure
    decoupled.edges([
        ("HelmRepo", "ChartReleaser"),
        ("ChartReleaser", "RemoteHelmRepo"),
        ("GitOpsRepo", "DecoupledArgoCD"),
        ("RemoteHelmRepo", "DecoupledArgoCD"),
        ("DecoupledArgoCD", "DecoupledCluster")
    ])

# Render the diagram to a file
diagram_path = "GitOps_Repository_Structure"
diagram.render(diagram_path, cleanup=True)
EOF

# Step 5: Upload the rendered diagram
