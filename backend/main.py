from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Absolute path to the frontend directory (one level up, then 'fortex')
# We use abspath to ensure it works regardless of where the app is run from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(os.path.dirname(BASE_DIR), "fortex")

# 1. Serve the specific entry point (hack1.html) at the root URL
@app.get("/")
async def read_root():
    return FileResponse(os.path.join(FRONTEND_DIR, "hack1.html"))

# 2. Mount the entire 'fortex' directory to serve all other files 
# (hack7.html, css, generated images likely needed here)
# We mount it at the root "/" so that relative links in your HTML 
# (like <a href="hack7.html">) work automatically.
app.mount("/", StaticFiles(directory=FRONTEND_DIR), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
