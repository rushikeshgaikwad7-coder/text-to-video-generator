from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from text_to_video_generator.api.routes import router

app = FastAPI(
    title="Text-to-Video Generator",
    description="Unified AI video generation platform",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Text-to-Video Generator API",
        "docs": "/docs",
        "health": "/api/v1/health",
        "generate": "/api/v1/generate"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
