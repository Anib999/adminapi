from fastapi import status, HTTPException, APIRouter, Depends

router = APIRouter(
    prefix='/client',
    tags=['Client']
)

@router.get('/')
async def get_client():
    return {'message': 'Client'}