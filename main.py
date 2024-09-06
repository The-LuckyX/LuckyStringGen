import config
import time
import logging
from pyrogram import Client, idle
from pyromod import listen  
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger("pymongo").setLevel(logging.ERROR)

# Initialize start time
StartTime = time.time()

# Initialize the Client
app = Client(
    "LUCKY",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="LuckyStringGen"),
)

if __name__ == "__main__":
    print("𝙻𝚄𝙲𝙺𝚈 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝙶𝙴𝙽 𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...")
    try:
        app.start()
    except ApiIdInvalid:
        raise Exception("Your API_ID is not valid.")
    except ApiIdPublishedFlood:
        raise Exception("Your API_ID/API_HASH is flood banned.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

    uname = app.get_me().username
    print(f"@{uname} NOW LUCKY SESSION GEN IS READY TO GEN SESSION")
    
    idle()
    
    app.stop()
    print("𝐒𝙴𝚂𝚂𝙸𝙾𝙽 𝐆𝙴𝙽 𝐒𝚃𝙾𝙿𝙿𝙴𝙳...")
