from apscheduler.schedulers.background import BackgroundScheduler
from backend.cronjobs.auto_end_live import auto_end_inactive_streams

def start_background_tasks():
    scheduler = BackgroundScheduler()
    scheduler.add_job(auto_end_inactive_streams, "interval", minutes=1)
    scheduler.start()
