"""This is a simple HTML Server API"""

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class WebsiteInfo(BaseModel):
    """Pydantic Model designed to hold webpage info"""

    Title: str
    Error: int
    Quote: str


@app.get("/")
def root_website(web_title: str, web_error: int, web_quote: str):
    """Simple Website Example

    Args:
        web_title (str): This is the string that will go into Website Header
        web_error (int): This will be outtputted as an exaple error
        web_quote (str): shown underneath Title

    Returns:
        Dict: Webpage base on info given
    """
    return {"Title": web_title, "Error": web_error, "Quote": web_quote}


if __name__ == "__main__":
    uvicorn.run(app)
