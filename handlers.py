def process_request(request):
    try:
        return {'status': 'ok', 'result': request['data'] * 2}
    except:
        return {'status': 'error'}