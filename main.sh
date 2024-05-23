docker build -t fastapi1 -f app/Dockerfile app/
docker build -t script1 -f script/Dockerfile script/

kubectl apply -f deploy.yml

minikube tunnel
