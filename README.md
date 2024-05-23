Задание 2
Перевести приложение из предыдущего задания для работы через Istio. Для этого:

написать скрипт для запуска Istio в вашем кластере, и настройки добавления лейблов для того, чтобы Istio начал автоматически внедрят sidecat контейнеры к вашим приложениям в Kubernetes. Также, в этом скрипте, при запуске Istio в вашем кластере, необходимо указать настройку, которая запрещает внешний трафик по умолчанию, если нет необходимых манифестов.
написать все необходимые манифесты, чтобы теперь весь входящий трафик шел через Ingress Gateway
теперь при обращении на endpoint GET /time вашего приложения, оно должно делать запрос на http://worldtimeapi.org/api/timezone/Europe/Moscow и возвращать пользователю значение поля datetime из запроса выше.
создать манифейсты, которые разрешают внешний трафик на worldtimeapi.org
в readme проекта опишите куда надо сделать запрос, чтобы получить результат(оставить с предыдущего задания, если ничего не поменялось).

Решение

- Запускаем minikube

minikube start

- Устанавливаем Istio

curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.22.0 TARGET_ARCH=x86_64 sh - && cd istio-1.21.0 && export PATH=$PWD/bin:$PATH

- Применяем настройки 

istioctl install --set profile=demo -y --set meshConfig.outboundTrafficPolicy.mode=REGISTRY_ONLY

- Добавляем метку

kubectl label namespace default istio-injection=enabled


- Запускаем приложение 

./main.sh


- Для проверки делаем запросы по


curl http://127.0.0.1:8000/time

curl http://127.0.0.1:8000/statistics
