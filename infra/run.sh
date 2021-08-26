# Create and push Docker images to kind-registry
python3 /app/infra/docker.py
# Reset Kubernetes cluster
kind delete cluster
kind create cluster --config=/app/infra/kind.yaml
# Set Kubectl context
SERVER=$(kind get kubeconfig --internal | yq e .clusters[0].cluster.server -)
CERT=$(kind get kubeconfig --internal | yq e .clusters[0].cluster.\"certificate-authority-data\" -)
kubectl config set clusters.infra.server ${SERVER}
kubectl config set clusters.infra.certificate-authority-data ${CERT}
kubectl config set contexts.infra.cluster infra
kubectl config set contexts.infra.user kind-kind
kubectl config use infra
# Start Pulumi
cd /app/infra
pulumi login --local
pulumi stack init infra
pulumi up --yes
# Watch Pods
watch kubectl get pods --all-namespaces
