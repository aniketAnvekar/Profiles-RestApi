from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    '''Test api view'''

    def get(self,request,format=None):
        '''Returns a list of API view features'''
        an_apiview = [
                'Is similar to traditional Django view',
                'Gives you the most control over application logic',
                'Uses HTTP methods as function (get,post,patch,put,delete)'
        ]
        return Response({'message':'hello','an_apiview':an_apiview})
