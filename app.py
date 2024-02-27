import logging
import bot.main as tg_bot

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
    tg_bot.run_bot()