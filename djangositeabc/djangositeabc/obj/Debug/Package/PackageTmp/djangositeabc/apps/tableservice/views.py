from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import Context
from azure.storage import TableService      
from django.views.decorators.csrf import csrf_exempt
                  
account_name = 'demostorageabc'
account_key = 'AdIC+CU33zVWVDd8P6TSZgVODG8F5+hkyQuhKtuw9WrhaZqOxWbS8O9oFWcTCkLeu6x6gnjuMPepyENqhrLMOw=='

table_service = TableService(account_name=account_name, account_key=account_key)
table_service.create_table('mytasks')

@csrf_exempt
def list_tasks(request): 
    entities = table_service.query_entities('mytasks', '', 'name,category,date,complete')    
    html = render_to_string('tableservice/task.html', Context({'entities':entities}))
    return HttpResponse(html)

@csrf_exempt
def add_task(request):
    from datetime import date as d
    name = request.POST['name']
    category = request.POST['category']
    date = str(d.today())
    table_service.insert_entity('mytasks', {'PartitionKey':name+category, 'RowKey':date, 'name':name, 'category':category, 'date':date, 'complete':'No'}) 
    entities = table_service.query_entities('mytasks', '', 'name,category,date,complete')
    html = render_to_string('tableservice/task.html', Context({'entities':entities}))
    return HttpResponse(html)

@csrf_exempt
def update_task(request):
    name = request.POST['name']
    category = request.POST['category']
    date = request.POST['date']
    partition_key = name + category
    row_key = date
    table_service.update_entity('mytasks', partition_key, row_key, {'PartitionKey':partition_key, 'RowKey':row_key, 'name': name, 'category':category, 'date':date, 'complete':'Yes'})
    entities = table_service.query_entities('mytasks', '', 'name,category,date,complete')    
    html = render_to_string('tableservice/task.html', Context({'entities':entities}))
    return HttpResponse(html)
