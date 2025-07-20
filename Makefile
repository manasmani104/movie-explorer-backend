# Run auto-format (Black) + lint (Flake8) together
lint:
	docker compose run --rm web black .
	docker compose run --rm web flake8 .

# Run only Black (formatting)
format:
	docker compose run --rm web black .

# Run only Flake8
check:
	docker compose run --rm web flake8 .

# Run tests
test:
	docker compose run --rm web pytest
