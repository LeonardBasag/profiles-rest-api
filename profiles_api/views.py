from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View"""
    def get(self, request, format=None):
        """Returns a list of ApiView features"""
        an_apiview = [
            'Uses HTTP methods as functions(get, post, put, patch, delete)',
            'Is simlar to a traditional Django View',
            'Gives you the most control over application logic',
            'Is mappep manually to URLs'
        ]
        return Response({'message':'Hello!', 'an_apiview': an_apiview})
