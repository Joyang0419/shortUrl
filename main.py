import uvicorn
from src.configs.app_config import DEBUG


if __name__ == '__main__':
    uvicorn.run("src.application:app", host="0.0.0.0", port=9000, reload=DEBUG)
