from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from backend.utils.email_sender import send_email_with_template
from backend.models import MessageLog, AdEarning, GiftTransaction, Wallet, User

def generate_campaign_report(db: Session, user: User):
    today = datetime.utcnow()
    past = today - timedelta(days=1)

    messages_sent = db.query(MessageLog).filter(
        MessageLog.user_id == user.id,
        MessageLog.created_at >= past
    ).count()

    smartcoins_used = sum([
        msg.cost for msg in db.query(MessageLog)
        .filter(MessageLog.user_id == user.id, MessageLog.created_at >= past)
        if hasattr(msg, 'cost')
    ])

    smartcoins_earned = db.query(AdEarning).filter(
        AdEarning.user_id == user.id,
        AdEarning.created_at >= past
    ).with_entities(AdEarning.smartcoins_earned).all()
    total_earned = sum([e[0] for e in smartcoins_earned])

    replies = 0  # if reply system is tracked

    send_email_with_template(
        db=db,
        to_email=user.email,
        template_name="campaign_report",
        data={
            "user_name": user.full_name,
            "report_date": today.strftime("%Y-%m-%d"),
            "messages_sent": messages_sent,
            "smartcoins_used": smartcoins_used,
            "smartcoins_earned": total_earned,
            "replies": replies
        }
    )
