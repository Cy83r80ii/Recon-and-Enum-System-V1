from fastapi import APIRouter
from pydantic import BaseModel
from engine import run_scan
from utils import state

router = APIRouter()

class ScanRequest(BaseModel):
    target: str
    mode: str = "quick"

@router.post("/scan")
async def scan(req: ScanRequest):

    state.SCAN_STATUS = "running"

    findings = run_scan(req.target, req.mode)

    state.SCAN_RESULTS = findings

    state.SCAN_STATUS = "complete"

    return {
        "status": "completed",
        "total_findings": len(findings)
    }