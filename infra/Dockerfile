FROM ubuntu:18.04

RUN apt-get update -y && \
	apt-get install -y \
		curl \
		lsb-release \
		python3.7 \
		python3-pip

# Install Docker
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get update -y && \
	apt-get install -y \
		docker-ce

# Clean apt cache
RUN rm -rf /var/lib/apt/lists/*

# Install Kind
RUN curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-linux-amd64 && \
	chmod +x ./kind && \
	mv ./kind /usr/local/bin/kind

# Install Kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
RUN install kubectl /usr/local/bin/kubectl

# Install Pulumi
RUN curl -fsSL https://get.pulumi.com | sh
ENV PATH=/root/.pulumi/bin:$PATH

# Install Python dependencies
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r /tmp/requirements.txt

COPY . /app
WORKDIR /app
