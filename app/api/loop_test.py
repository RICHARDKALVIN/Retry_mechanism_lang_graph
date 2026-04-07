from fastapi import APIRouter
from app.service import test_service
from schema import State

router = APIRouter(prefix="/loop_test", tags=["loop_test"])



@router.get("/")
async def loop_test( temp :str):
    return  await test_service.loop_test(State(query=temp,loop_count=0,metadata={},answer="",retry_count=0,url=""))