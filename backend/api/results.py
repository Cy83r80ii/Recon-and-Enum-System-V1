from fastapi import APIRouter
from utils import state

router = APIRouter()


@router.get("/results")
def results():

    return {
        "total": len(state.SCAN_RESULTS),
        "findings": state.SCAN_RESULTS
    }
