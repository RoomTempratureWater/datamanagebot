TOKEN = '5076017527:AAGxIorWO7dn-fJ46JKnLs8SoN2OwqsLSxc'
HEROKU = 'https://telegram-managment-bot.herokuapp.com/'
BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)
WEBHOOK_ENDPOINT = '{}/webhook'.format(HEROKU)
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'
TELEGRAM_SEND_PHOTO_URL = BASE_TELEGRAM_URL + '/sendphoto?chat_id={}&photo={}&caption={}'

HERE_API_KEY = 'udHoDiTwUXuHj9B-oXqPe07HkvmHbFQoC6FzwT1nNXw'

HERE_BASE_URL = 'https://places.ls.hereapi.com'

PLACES_URL = HERE_BASE_URL+'/places/v1/discover/explore?at={}%2C{}&cat={}&apiKey='+HERE_API_KEY

NASA_APOD_KEY = 'dO6xx7NNMaUUY1gQP1RtkE8Svll7DogtK2kNpTFT'
NASA_APOD_URL = 'https://api.nasa.gov/planetary/apod?api_key='+NASA_APOD_KEY


TELEGRAM_PIC_jURL = 'https://api.telegram.org/bot{}/getFile?file_id='.format(TOKEN)

TELEGRAM_PIC_URL = 'https://api.telegram.org/file/bot{}/'.format(TOKEN)
