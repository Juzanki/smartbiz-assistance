from fastapi import APIRouter, Request, HTTPException
from backend.utils.telegram_bot import send_telegram_message

router = APIRouter(prefix="/telegram", tags=["Telegram Bot"])


@router.post("/webhook", summary="🎯 Telegram Bot Webhook (SmartBiz)")
async def telegram_webhook(request: Request):
    """
    Webhook handler for Telegram Bot messages.
    Processes incoming messages and replies based on simple logic.
    """

    try:
        data = await request.json()

        # Step 1: Safely extract message info
        message = data.get("message")
        if not message:
            raise ValueError("No message payload.")

        chat = message.get("chat")
        if not chat or not chat.get("id"):
            raise ValueError("Chat ID missing.")

        chat_id = str(chat["id"])
        text = message.get("text", "").strip()

        if not text:
            raise ValueError("Message text is missing.")

        text_lower = text.lower()

        # Step 2: SmartBot logic
        if text_lower == "/start":
            reply = (
                "👋 *Karibu kwenye SmartBiz Bot!*\n\n"
                "Tuma ujumbe wowote na tutakujibu haraka.\n"
                "_Pia unaweza kutumia huduma ya AI kwa kutuma swali lolote kuhusu biashara._"
            )
        elif "asante" in text_lower:
            reply = "🙏 Karibu sana! Ikiwa una swali lingine, uliza tu."
        elif text_lower.startswith("/ai"):
            query = text[3:].strip()
            reply = "🤖 AI huduma bado haijawashwa kwenye webhook hii. (Tuma `/start` kuanza)"
            # Optional: Unganisha na AI later
        else:
            reply = f"📩 *Umesema:* `{text}`\n\n_Tutakujibu haraka._"

        # Step 3: Send response via bot
        await send_telegram_message(chat_id=chat_id, message=reply)

        return {"status": "✅ Webhook received", "chat_id": chat_id}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"❌ Webhook error: {str(e)}")
