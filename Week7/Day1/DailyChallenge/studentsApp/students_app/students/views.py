from .models import Student
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError


@csrf_exempt
def student_list(request):
    if request.method == "GET":
        if "date_joined" in request.GET:
            queryset = Student.objects.filter(date_joined=request.GET.get('date_joined'))
        else:
            queryset = Student.objects.all()

        serializer = StudentSerializer(queryset, many=True)
        return JsonResponse(data=serializer.data, safe=False)

    if request.method == "POST":
        student_data = JSONParser().parse(request)
        serializer = StudentSerializer(data=student_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)  # successfully created
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(data=serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(instance=student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)
