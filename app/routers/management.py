from fastapi import status, HTTPException, APIRouter, Depends

router = APIRouter(
    prefix='/management',
    tags=['Management']
)

@router.get('/')
async def get_management():
    return {'message': 'management'}