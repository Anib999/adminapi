from fastapi import status, HTTPException, APIRouter, Depends

router = APIRouter(
    prefix='/sales',
    tags=['Sales']
)

@router.get('/')
async def get_sales():
    return {'message': 'Sales'}