from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok", "app": settings.APP_NAME}

# Include API Routers
from app.api.v1.endpoints import auth, data_sources, quality_rules, ws
app.include_router(auth.router, prefix=f"{settings.API_V1_PREFIX}/auth", tags=["Authentication"])
app.include_router(data_sources.router, prefix=f"{settings.API_V1_PREFIX}/data-sources", tags=["Data Sources"])
app.include_router(quality_rules.router, prefix=f"{settings.API_V1_PREFIX}/quality-rules", tags=["Quality Rules"])
app.include_router(ws.router, prefix="/ws", tags=["WebSockets"])