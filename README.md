# StudentApp-server

.env config
```.env

SECRET_KEY=supersecret!
DEBUG=1

POSTGRES_USER=postgres
POSTGRES_PASSWORD=123456p
POSTGRES_SERVER=127.0.0.1
POSTGRES_PORT=5432
POSTGRES_DB=postgres

```

run 

```bash
uvicorn main:app --reload

```
