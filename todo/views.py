from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializer import TodoSerilizer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class TodoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        todos = Todo.objects.filter(user = user)
        serializer = TodoSerilizer(todos, many=True)
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message': 'todo fetch sucessfully'
        })

    def post(self, request):
        try:
            user = request.user
            data = request.data
            data['user'] = user.id
            serializer = TodoSerilizer(data = data)

            if not serializer.is_valid():
                return Response({
                    'status' : False,
                    'data' : serializer.errors,
                    'message': 'invalid fields'
                })

            serializer.save()

            return Response({
                'status' : True,
                'data' : serializer.data,
                'message': 'todo created sucessfully'
            })
        except Exception as e:
            print(e)
            return Response({
                'status' : True,
                'data' : {},
                'message': 'Something went wrong'
            })


    def patch(self, request):
            try:
                data = request.data

                if not data.get('uid'):
                    return Response({
                        'status' : False,
                        'data' : {},
                        'message': 'uid required'
                    })

                obj = Todo.objects.filter(uid = data.get('uid'))

                if not obj.exists():
                    return Response({
                        'status' : False,
                        'data' : {},
                        'message': 'Data not available'
                    })

                serializer = TodoSerilizer(obj[0],data=data, partial = True)

                if not serializer.is_valid():
                    return Response({
                        'status' : False,
                        'data' : serializer.errors,
                        'message': 'invalid fields'
                    })

                serializer.save()

                return Response({
                    'status' : True,
                    'data' : serializer.data,
                    'message': 'todo created sucessfully'
                })
            except Exception as e:
                print(e)
                return Response({
                    'status' : True,
                    'data' : {},
                    'message': 'Something went wrong'
                })


