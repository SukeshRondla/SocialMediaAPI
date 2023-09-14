from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from .routers import post, user, auth, vote
from .config import settings

app = FastAPI()

# Load CORS origins from environment variables or configure it as needed.
origins = ["*"]  # You can replace this with settings.CORS_ORIGINS or an environment variable.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World pushing out to ubuntu"}
