import logging
import sys
import asyncio
from config import *
from tg.bot import main


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
