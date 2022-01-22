from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from configs import templates


html_router = APIRouter()

@html_router.get("/main", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@html_router.get("/messanger", response_class=HTMLResponse)
async def get_messanger(request: Request):
    return templates.TemplateResponse("messanger.html", {"request": request})
