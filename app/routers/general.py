from fastapi import status, HTTPException, APIRouter, Depends

router = APIRouter(
    prefix='/general',
    tags=['General']
)

@router.get('/')
async def get_general():
    return {'message': 'general'}