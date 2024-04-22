from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    """
    注册一个根路径
    :return:
    """
    return {"message": "Hello World"}


@app.get("/info")
async def info():
    """
    项目信息
    :return:
    """
    return {
        "app_name": "FastAPI框架学习",
        "app_version": "v0.0.1"
    }
if __name__ == "__main__":
    print("Starting webserver...")
    uvicorn.run(
        api, 
        host="0.0.0.0",
        port=int(os.getenv("PORT", 9000)),
        debug=os.getenv("DEBUG", False),
        log_level=os.getenv('LOG_LEVEL', "info"),
        proxy_headers=True
    )
