import sys
import uvicorn
from main import graphql_app

if __name__ == "__main__":
    try:
        uvicorn.run(graphql_app, host="0.0.0.0", port=8080)
    except KeyboardInterrupt:
        sys.exit(0)