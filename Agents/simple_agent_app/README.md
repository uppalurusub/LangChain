#🤖 Simple AI Agent — Streamlit App

A lightweight Streamlit application that wraps a modular AI agent architecture.

It cleanly separates:

agent logic

configuration

UI rendering

So you can extend, debug, and maintain it easily.

⭐ Features

🧩 Modular Python structure

🤖 Plug-and-play AI agent wrapper

🎛️ Custom response style + verbosity controls

⚙️ Environment-based configuration

🧪 Easy to extend with tools, memory, logging, etc.

📁 Project Structure
simple_agent_app/
│
├── app.py
├── core/
│   ├── __init__.py
│   ├── config.py
│   ├── agent.py
│   └── utils.py
│
├── requirements.txt
└── README.md


app.py – Streamlit UI

config.py – environment + API config

agent.py – agent creation + execution logic

utils.py – optional helper utilities

.env file for keys

🔐 Prerequisites

Python 3.9+

An API key compatible with your chosen model (e.g., OpenAI-style)

Create a .env file in the project root:

OPENAI_API_KEY=your_key_here


🚨 The app will raise an error if the key is missing — by design.

pip install -r requirements.txt

▶️ Run the App
streamlit run app.py


Then open the URL shown in the terminal (usually http://localhost:8501).

🧭 How to Use

Enter your question or prompt

Choose Response Style

Choose Verbosity

Click Run Agent

The agent executes and streams the formatted output.

🛠️ Customize / Extend
Add tools or capabilities

Edit:

core/agent.py


You can plug in:

web search

calculator

retrieval / RAG

tool-calling workflows

conversation memory

Change UI

Modify:

app.py


Add inputs, tabs, or layout changes.

🧰 Environment Tips

Create a virtual environment:

python -m venv .venv
source .venv/bin/activate      # macOS / Linux

or

.\.venv\Scripts\activate       # Windows

❓ Troubleshooting

App says API key missing

Ensure .env exists and is correctly named.

Import errors

Re-install requirements:

pip install -r requirements.txt

Run the App
streamlit run app.py

Then open the URL shown in the terminal (usually http://localhost:8501).

Streamlit doesn’t refresh
Press R in the Streamlit UI or restart the app.


#🐳 Docker Setup

You can run this Streamlit app fully containerized using Docker.

This setup:

builds a lightweight image

avoids leaking API keys

runs Streamlit in headless mode

Docker Login 
docker login -u <<user-name>>

Build the Docker image for Local
docker build -t <<image-name>> .

Example:
docker build -t simple-agent-app .


Run the container
Pass your API key securely using environment variables:
docker run -p 8501:8501 \
  -e OPENAI_API_KEY=your_key_here \
  simple-agent-app

Open the app in your browser:
http://localhost:8501


✅ API keys are NOT stored in the image — they’re injected at runtime.

Build the Docker image for Dockerhub
docker build -t <<your-docker-user>>/<<image-name>>:version .
docker push <<your-docker-user>>/<<image-name>>:version

Example:
docker build -t subuppaluru71/simple-agent-app:latest .
docker push subuppaluru71/simple-agent-app:latest


Run the container
Pass your API key securely using environment variables:
docker run -p 8501:8501 \
  -e OPENAI_API_KEY=your_key_here \
  subuppaluru71/simple-agent-app:latest


🐳 Docker Compose setup
create a docker-compose.yml file

docker-compose building using below command.
docker compose up --build


🐳 Kubernetes Setup

Folder structure (recommended)
k8s/
  ├── deployment.yaml
  ├── service.yaml
  ├── secret.yaml
  └── ingress.yaml   (optional)


Kubernetes Secret — API Key
File: k8s/secret.yaml

Generate base64 value for the openai api key using following powershell command: 
powershell "[Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes('<<openai_api_key>>'))"
Paste the encoded string in the manifest file k8s/secret.yaml as plain text.

Deployment File to run the Streamlit app
File: k8s/deployment.yaml

Service — expose the app inside the cluster
File: k8s/service.yaml


(Optional) Ingress — expose publicly
Requires an ingress controller (Nginx, Cloud provider, etc.)
File: k8s/ingress.yaml

Enable or start Kubernetes Cluster from docker desktop

Install kubernetes client kubectl on windows using below powershell command.
inget install -e --id Kubernetes.kubectl


Apply kubernetes files in the folder k8s folder
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml   # optional

Verify pods:
kubectl get pods

Verify Logs:
kubectl logs -l app=simple-agent-app

Verify Service:
kubectl get svc simple-agent-service


Verify Ingress:
kubectl get ingress


open the app using kubernetes using below:
kubectl port-forward svc/simple-agent-service 8501:80
Browse: http://localhost:8501/



📄 License

Use freely for learning, demos, and internal projects.
Add your preferred license here if publishing.
