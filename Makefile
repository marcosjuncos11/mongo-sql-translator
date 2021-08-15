.PHONY : build
build:
	docker-compose -f ./docker-compose-test.yml build

.PHONY : test
test:
	docker-compose -f ./docker-compose-test.yml up
