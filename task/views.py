from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TaskTable
from .serializers import TaskSerializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.renderers import JSONRenderer
import json


def validation(func):
    def inner(self, request, *args, **kwargs):
        print("REQUEST DATA", request.data)
        priority = ['P1','P2','P3','P4']
        task_status = ['Not Completed','In Progress','Completed']
        print(request.data)
        print(request.data['priority'])

        if request.data['priority'] in priority and request.data['status'] in task_status:
            return func(self, request, *args, **kwargs)
        response_data = {
                'module': 'Task',
                'code': 'ValueError',
                'message': 'Invalid Value Status/ Priority'
            }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    return inner


class task_api(APIView):
    def get(self, request, pk=None, format=None):
        try:
            id = pk
            if id is not None:
                stu = TaskTable.objects.get(id=id)
                serializer = TaskSerializers(stu)

                return Response(serializer.data)

            stu = TaskTable.objects.all()
            serializer = TaskSerializers(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            # print(json_data)
            return Response(serializer.data)

        except KeyError as e:
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Key Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except ValueError as e:
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Value Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            print(type(e))
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Validation Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Value Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    @validation
    def post(self, request, format=None):
        try:
            serializer = TaskSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except KeyError as e:
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Key Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except ValueError as e:
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Value Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            print(type(e))
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Validation Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Value Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    @validation
    def put(self, request, pk=None, format=None):
        try:
            id = pk
            stu = TaskTable.objects.get(pk=id)
            serializer = TaskSerializers(stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Complete Data Updated'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except KeyError as e:
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Key Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except ValueError as e:
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Value Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            print(type(e))
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Validation Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Value Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        try:
            id = pk
            stu = TaskTable.objects.get(pk=id)
            serializer = TaskSerializers(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Partial Data Updated'})
            return Response(serializer.errors)

        except KeyError as e:
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Key Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except ValueError as e:
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Value Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            print(type(e))
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Validation Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Value Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        try:
            id = pk
            stu = TaskTable.objects.get(pk=id)
            stu.delete()
            return Response({'msg': 'Data Deleted'})

        except KeyError as e:
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Key Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except ValueError as e:
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Value Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            print(type(e))
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Validation Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            response_data = {
                'module': "TASK",
                'code': "Error 400",
                'message': "Value Error" + str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
