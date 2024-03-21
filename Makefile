DC = docker-compose

start:
	@echo "Starting services..."
	@$(DC) up -d

stop:
	@echo "Stopping services..."
	@$(DC) down