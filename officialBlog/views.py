from django.shortcuts import render 
from django.http import JsonResponse
from rest_framework import serializers

from rest_framework .decorators import api_view
from rest_framework.response import Response

from .serializers import BlogSerializers
from .models import Blogs
# Create your views here.


@api_view(['GET'])
def apiOverView(request):
    All_Blogs = Blogs.objects.all()
    serializer = BlogSerializers(All_Blogs)
    api_urls = {
        'List': 'AllBlogs',
        'Detail-view': '/blogPost-detail/<str:pk/>',
        'update-view': 'blog-create/<str:pk/>',
        'create-view': 'blog-create/',
        'delete-view': 'blog-delete/',

    }
    
    return Response(serializers)

@api_view(['GET'])
def blogList(request):
    All_Blogs = Blogs.objects.all()
    serializer = BlogSerializers(All_Blogs, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def blogDetail(request, pk):
    All_Blogs = Blogs.objects.get(id=pk)
    serializer = BlogSerializers(All_Blogs, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def createBlog(request):
    serializer = BlogSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateBlog(request, pk):
    blog = Blogs.objects.get(id=pk)
    serializer = BlogSerializers(instance=blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteBlog(request, pk):
    blog = Blogs.objects.get(id=pk)
    blog.delete()
    
    return Response('Blog deleted')