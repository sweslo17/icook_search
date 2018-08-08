import icook_query
import logging
from aiohttp import web

logger = logging.getLogger(__name__)

async def handle(request):
    logger.info(request)
    query = request.query.get("query", "")
    ingredients = request.query.get("ingredients", "")
    result = icook_query.query(query=query, ingredients=ingredients)
    return web.json_response(result)

app = web.Application()
app.add_routes([web.get('/icook_query', handle)])

web.run_app(app)
