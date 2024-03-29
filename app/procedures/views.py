# Create your views here.
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from procedures.models import Procedure, Simulation
from procedures.serializer import ProcedureSerializer


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def procedure_computation(request, id_procedure):
    try:
        procedure = Procedure.objects.get(id=id_procedure)
        simulation_id = procedure.compute()
        if simulation_id is not None:
            return Response({
                'error': 'procedure completed',
                'simulation_id': simulation_id
            },
                status=status.HTTP_202_ACCEPTED)
        return Response({'error': 'error when processing the procedure'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    except ObjectDoesNotExist:
        return Response({'error': 'procedure does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def simulation_apply(request, id_simulation):
    try:
        simulation = Simulation.objects.get(id=id_simulation)
        if simulation.apply():
            return Response({
                'error': 'simulation applied',
            },
                status=status.HTTP_202_ACCEPTED)
        return Response({'error': 'error when processing the simulation'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    except ObjectDoesNotExist:
        return Response({'error': 'simulation does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_active_procedures(request):
    procedures = Procedure.objects.filter(active=True)
    serializer = ProcedureSerializer(procedures, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def post_procedure(request):
    serializer = ProcedureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
