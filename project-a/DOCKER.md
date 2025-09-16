# Docker Test

```bash
# Build and run the container
cd project-a
docker compose up -d

# Test the API
curl http://localhost:5001/
curl http://localhost:5001/utils/capitalize/hello%20world

# Stop the container
docker compose down
```
