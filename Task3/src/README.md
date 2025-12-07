При выполнении немного отошол от задания
делал через docker compose
думаю это не критично

запуск сервисов и наполнения данными jeager 

docker compose up -d --build

Ждем

Проверка

docker ps
CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS          PORTS                                                                                                                                                                                 NAMES
00da2c080634   src-service-a                   "flask run --port 80…"   30 seconds ago   Up 29 seconds   0.0.0.0:8081->8080/tcp, [::]:8081->8080/tcp                                                                                                                                           service-a
9408a6080f58   jaegertracing/all-in-one:1.57   "/go/bin/all-in-one-…"   30 seconds ago   Up 29 seconds   5775/udp, 5778/tcp, 9411/tcp, 14250/tcp, 0.0.0.0:4317-4318->4317-4318/tcp, [::]:4317-4318->4317-4318/tcp, 0.0.0.0:16686->16686/tcp, [::]:16686->16686/tcp, 6831-6832/udp, 14268/tcp   jaeger
7978fdfe47fe   src-service-b                   "flask run --port 80…"   30 seconds ago   Up 29 seconds   0.0.0.0:8082->8080/tcp, [::]:8082->8080/tcp                                                                                                                                           service-b


Наполняем 
curl http://localhost:8082/
curl http://localhost:8081/
curl http://localhost:8082/
curl http://localhost:8081/
curl http://localhost:8081/
curl http://localhost:8081/

логи в директории /jager_log