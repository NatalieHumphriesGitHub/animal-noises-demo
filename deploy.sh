export MYSQL_ROOT_PASSWORD
export SECRET_KEY
docker stack deploy --compose-file docker-compose.yaml animal-stack
docker service update --replicas 3 animal-stack_front-end