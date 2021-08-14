docker exec infra bash -c "
	# Install Kubernetes Dashboard
	cd /tmp
	wget https://raw.githubusercontent.com/kubernetes/dashboard/v2.2.0/aio/deploy/recommended.yaml
	kubectl apply -f .
	python3 /app/infra/splityaml.py recommended.yaml .
	# Skip login
	yq e -i '.spec.template.spec.containers[0].args[0] = \"--enable-skip-login\"' \
		kubernetes-dashboard.deployment.yaml
	yq e -i '.spec.template.spec.containers[0].args[1] = \"--disable-settings-authorizer\"' \
		kubernetes-dashboard.deployment.yaml
	yq e -i '.spec.template.spec.containers[0].args[2] = \"--auto-generate-certificates\"' \
		kubernetes-dashboard.deployment.yaml
	yq e -i '.spec.template.spec.containers[0].args[3] = \"--namespace=kubernetes-dashboard\"' \
		kubernetes-dashboard.deployment.yaml
	kubectl apply -f kubernetes-dashboard.deployment.yaml
	# Grant cluster admin role
	kubectl delete clusterrolebinding kubernetes-dashboard
	yq e -i '.roleRef.name = \"cluster-admin\"' \
		kubernetes-dashboard.clusterrolebinding.yaml
	kubectl apply -f kubernetes-dashboard.clusterrolebinding.yaml
	# Start dashboard
	echo /////////////////////////////////////////////////////
	echo Dashboard URL:
	echo http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/error?namespace=default
	echo /////////////////////////////////////////////////////
	kubectl proxy --address=0.0.0.0 --port=8001 --accept-hosts=.*
"
