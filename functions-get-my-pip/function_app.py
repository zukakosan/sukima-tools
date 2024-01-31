import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="pip")
def pip(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Request method: %s', req.method)
    logging.info('Request URL: %s', req.url)
    logging.info('Request headers: %s', req.headers)
    logging.info('Request params: %s', req.params)
    # source_ip = req.headers.get('x-forwarded-for')
    iplist = req.headers.get('x-forwarded-for').split(':')[0].split(',')

    # index -2(not -1) is because Azure API Management IP is added to the end of the iplist
    source_ip = iplist[len(iplist) - 2]

    # source_ip = req.headers.get('x-forwarded-for').split(':')[0].split(',')[0]

    return source_ip