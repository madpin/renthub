import os
import uvicorn
from typing import List, Optional
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse


import telegram
import schemas

app = FastAPI()


@app.post("/send_telegram/")
async def sent_telegram(message: schemas.TelegramMessage):
    bot = telegram.Bot(token=os.getenv('TG_BOT_TOKEN'))
    # bot_all = telegram.Bot(token=os.getenv('TG_BOT_TOKEN_ALL'))
    ret_ = []

    main_msg = bot.send_message(
        chat_id=message.chat_id,
        text=message.message,
        parse_mode=telegram.ParseMode.HTML,
        timeout=message.timeout,
        disable_web_page_preview=message.disable_web_page_preview,
    )
    ret_.append(main_msg.to_dict())
    if(message.images):
        media_array = []
        for image in message.images:
            media_array.append(telegram.InputMediaPhoto(
                image.url,
                caption=image.caption
            ))

        media_array_split = [media_array[i:i + 10]
                            for i in range(0, len(media_array), 10)]

        for small_array in media_array_split:
            media_msg = bot.send_media_group(
                reply_to_message_id=main_msg['message_id'],
                chat_id=message.chat_id,
                media=small_array,
                timeout=message.timeout,
            )
            ret_.append([x.to_dict() for x in media_msg])

    return ret_


# @app.post("/uploadfiles/")
# async def create_upload_files(files: Optional[List[UploadFile]] = File(None)):
#     return {"filenames": [file.filename for file in files]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
