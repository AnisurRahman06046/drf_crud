from django.shortcuts import render
from .models import Blogs
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_404_NOT_FOUND
from .utils import custom_response

@api_view(['POST'])
def createBlog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def allBlogs(request):
    blogs = Blogs.objects.all().order_by("-created_at")
    result = BlogSerializer(blogs,many=True)
    # print(result)
    custom_response = {
        "message":"Fetched successfully",
        "success":True,
        "data":result.data
    }
    return Response(custom_response)


@api_view(['GET'])
def singleBlog(request,id):
    data = Blogs.objects.get(id=id)
    result = BlogSerializer(data,many=False)
    response = custom_response("fetched successfully",True,result.data)
    return Response(response)

@api_view(['PATCH'])
def updateBlog(request,id):
    isExist = Blogs.objects.get(id=id)
    if(not isExist):
        return Response({'message':"Not found"})
    datas = BlogSerializer(instance=isExist,data=request.data,partial=True)
    if datas.is_valid():
        datas.save()
    response = custom_response("updated successfully",True,datas.data)
    return Response(response)


@api_view(['DELETE'])
def deleteBlog(request,id):
    try:
        blogData = Blogs.objects.get(id=id)
        res = blogData.delete()
        return Response(res)
    except Blogs.DoesNotExist:
        return Response({'message':"Not found"},status=HTTP_404_NOT_FOUND)
    
    
    


