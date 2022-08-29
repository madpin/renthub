
from fastapi.templating import Jinja2Templates
from fastapi.logger import logger
import requests


def send_tg_message(listing, templates=None):
    if(templates is None):
        templates = Jinja2Templates(directory="templates")
    template_str = str(templates.get_template("telegram_message.html").render({
        "listing": listing,
    }))
    
    logger.info("listing")
    logger.info("listing")
    logger.info("listing")
    logger.info("listing")
    logger.info("listing")
    logger.info(listing)
    logger.info(listing.images)
    
    message_payload = {
        "message": template_str,
        "chat_id": "870524250",
        "timeout": 10,
        "disable_web_page_preview": True,
        # TODO: solve the images problem
        # "images": [{'url': str(x.get("url_600", ""))} for x in listing.images]
    }
    try:
        response = requests.post(
            'http://notification:8000/send_telegram/', json=message_payload)
        response.raise_for_status()
        logger.info(response.json())

        # Additional code will only run if the request is successful
    except requests.exceptions.HTTPError as error:
        logger.warning(error)
        return 500
    return True
