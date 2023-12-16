from fastapi import APIRouter
from .manga import MangaParser

router = APIRouter()


@router.get("/manga/{query}")
async def manga(query: str):
    manga_parser = MangaParser(query)
    return manga_parser.build_dict()