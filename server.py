import uvicorn



if __name__ == '__main__':
    config = uvicorn.Config('app.base:app', port=5000, reload=True,  log_level='info')
    server = uvicorn.Server(config)
    server.run()