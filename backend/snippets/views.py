from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import URLList, Database
from snippets.serializers import URLListSerializer, DatabaseSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def db_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        database = Database.objects.all()
        serializer = DatabaseSerializer(database, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        '''
        data = JSONParser().parse(request)
        serializer = URLListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)'''
        return HttpResponse(status=403)

@csrf_exempt
def db_detail(request, pk):
    print(pk)
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        database = Database.objects.get(pk=pk)
    except Database.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DatabaseSerializer(database)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        '''
        data = JSONParser().parse(request)
        serializer = URLListSerializer(database, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
        '''
        return HttpResponse(status=403)
    elif request.method == 'DELETE':
        # database.delete()
        return HttpResponse(status=403)


@csrf_exempt
def url_list(request, db, ct):
    print(db, ct)
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        try:
            database = Database.objects.get(name=db, correct="incorrect" not in ct)
        except Database.DoesNotExist:
            return HttpResponse(status=404)
        try:
            urllist = URLList.objects.filter(db=database)
            urllist = urllist[:12]
            serializer = URLListSerializer(urllist, many=True)
            return JSONResponse(serializer.data)
        except URLList.DoesNotExist:
            return HttpResponse(status=404)

    elif request.method == 'POST':
        '''
        data = JSONParser().parse(request)
        serializer = URLListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
        '''
        return HttpResponse(status=403)

data_memory = {'db_name': None, 'incorrect': {'db': None, 'slice': []}, 'correct': {'db': None, 'slice': []}}

@csrf_exempt
def url_list_by_page(request, db, ct, page, rows='3'):
    global data_memory
    print(db, ct, page, rows)

    """
    Retrieve, update or delete a code snippet.
    """
    try:
        if data_memory['db_name'] is None or data_memory['db_name'] != db:
            data_memory['db_name'] = db
            data_memory['incorrect']['db'] = Database.objects.get(name=db, correct=False).pk
            data_memory['correct']['db'] = Database.objects.get(name=db, correct=True).pk
    except Database.DoesNotExist:
        return HttpResponse(status=404)

    try:
        page = int(page)
        rows = int(rows)
        if len(data_memory['incorrect']['slice']) == 0:
            data_memory['incorrect']['slice'] = URLList.objects.filter(db=data_memory['incorrect']['db'])
            data_memory['correct']['slice'] = URLList.objects.filter(db=data_memory['correct']['db'])

        if page < 0:
            resp_url = '/db/' + db + '/' + ct + '/' + str(len(data_memory[ct]['slice'])//rows) + '/'
            return HttpResponseRedirect(resp_url)
        elif (page * rows) > len(data_memory[ct]['slice']):
            resp_url = '/db/' + db + '/' + ct + '/' + str(0) + '/'
            return HttpResponseRedirect(resp_url)
        if ((1+page) * rows) > len(data_memory[ct]['slice']):
            end = len(data_memory[ct]['slice'])
        else:
            end = (page+1)*rows
        urldetail = data_memory[ct]['slice'][page*rows:end]
    except URLList.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = URLListSerializer(urldetail, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        '''
        data = JSONParser().parse(request)
        serializer = URLListSerializer(urldetail, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
        '''
        return HttpResponse(status=404)

    elif request.method == 'DELETE':
        #urldetail.delete()
        return HttpResponse(status=404)
