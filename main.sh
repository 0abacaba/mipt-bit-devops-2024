docker build -t fastapi1 -f app/Dockerfile app/
docker build -t script1 -f script/Dockerfile script/

docker push fastapi1:latest
docker push script1:latest

kubectl apply -f deploy.yml

minikube tunnel
