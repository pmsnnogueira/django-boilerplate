docker-command:
	docker-compose -f ./docker-compose.yml $(cmd)

docker-run:
	$(MAKE) docker-command cmd="run --rm backend $(cmd)"
	