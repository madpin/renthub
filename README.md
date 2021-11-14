# RentHub
Notification Service to send message as soon as someone create an ad on renting websites.


## Main

### Alembic:

```
docker-compose run --rm rentcrud alembic init alembic
```

Alternatively, you can save the alembic.ini into the same mounted folder:
```
docker-compose run --rm main alembic -c /app/alembic/alembic.ini init alembic
```
But don't forget to move to the right place!
--- 
Prepare the changes:
```bash
docker-compose build && docker-compose run --rm main alembic -c /app/alembic.ini revision --autogenerate -m "images 2"
```

Deploy the changes:
```bash
docker-compose build && docker-compose run --rm main alembic -c /app/alembic.ini upgrade head
```

Best Practices:
https://sqlmodel.tiangolo.com/tutorial/fastapi/relationships/

Docker-compose in VSCode:
https://code.visualstudio.com/docs/containers/docker-compose

# Main Loop Script

- Read the daft search
- For each:
  - Check the db it that's already there:
    - 👍 
      - Check if the telegram message was sent
      - Continue
    - 👎
      - Read the full details
      - 🔮 Save the images
        - ML to tag them
      - Send the telegram message
        - 👍 Save to the DB
        - 👎 That's ok, will try next time