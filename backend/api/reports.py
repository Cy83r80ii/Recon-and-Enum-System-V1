from fastapi import APIRouter
from fastapi.responses import FileResponse
from utils.pdf_report import generate_pdf

router = APIRouter()

@router.get("/report")
def report():

    file = generate_pdf()

    return FileResponse(file, filename="aresx_report.pdf")
