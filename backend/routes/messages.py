from fastapi import APIRouter
from fastapi.responses import JSONResponse
from gettext import gettext as _  # i18n translation function

router = APIRouter(prefix="/public", tags=["Greetings"])


@router.get("/greet", summary="👋 Greet user in preferred language")
def greet():
    """
    Returns a welcome message in the user's preferred language.
    Works with backend i18n using gettext.
    """
    return JSONResponse(content={"message": _("Hello, welcome to our platform!")})
