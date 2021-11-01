# RentHub
Notification Service to send message as soon as someone create an ad on renting websites.


## Main

### Alembic:

```docker-compose run --rm rentcrud alembic init -t async alembic```
Prepare the changes:
```bash
docker-compose build && docker-compose run --rm rentcrud alembic revision --autogenerate -m "first tables"
```

Deploy the changes:
```bash
docker-compose build && docker-compose run --rm main alembic upgrade head
```