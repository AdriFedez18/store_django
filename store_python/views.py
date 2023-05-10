from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html',{
        'message':'Listado de productos',
        'title':'Productos',
        'products':[
        {
            'id':1,
            'title':'Producto 1',
            'description':'Descripción del producto 1',
            'stock':True
        },
        {
            'id':2,
            'title':'Producto 2',
            'description':'Descripción del producto 2',
            'stock':False
        },
        {
            'id':3,
            'title':'Producto 3',
            'description':'Descripción del producto 3',
            'stock':True
        }
        ]
    })

