### Build Docker image

```
docker-compose build web
```

### Run migrations

```
make migrate
```

### Run project

```
docker-compose up web worker clock
```

### Django Admin URL

```
open http://0.0.0.0:8000/admin/
```

### API URL

```
open http://0.0.0.0:8000/api/
```