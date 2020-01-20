from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import CVE, CPE, CWE
from .serializers import CVESerializer, CPESerializer, CWESerializer
# from .utils import _refresh_metadata_cve
from common.utils import cvesearch
from .tasks import sync_cwes_task, sync_cpes_task, sync_cves_task


class CVESet(viewsets.ModelViewSet):
    """API endpoint that allows CVE to be viewed or edited."""

    queryset = CVE.objects.all().order_by('cve_id')
    serializer_class = CVESerializer


class CPESet(viewsets.ModelViewSet):
    """API endpoint that allows CPE to be viewed or edited."""

    queryset = CPE.objects.all().order_by('id')
    serializer_class = CPESerializer


class CWESet(viewsets.ModelViewSet):
    """API endpoint that allows CWE to be viewed or edited."""

    queryset = CWE.objects.all().order_by('id')
    serializer_class = CWESerializer


@api_view(['GET'])
def sync_cwes(self):
    cvesearch.sync_cwe_fromdb()
    return JsonResponse("done.", safe=False)


@api_view(['GET'])
def sync_cwes_async(self):
    sync_cwes_task.apply_async(args=[], queue='default', retry=False)
    return JsonResponse("enqueued.", safe=False)


@api_view(['GET'])
def sync_cpes(self):
    cvesearch.sync_cpe_fromdb()
    return JsonResponse("done.", safe=False)


@api_view(['GET'])
def sync_cpes_async(self):
    sync_cpes_task.apply_async(args=[], queue='default', retry=False)
    return JsonResponse("enqueued.", safe=False)


@api_view(['GET'])
def sync_cves(self):
    cvesearch.sync_cve_fromdb()
    return JsonResponse("done.", safe=False)


@api_view(['GET'])
def sync_cves_async(self):
    sync_cves_task.apply_async(args=[], queue='default', retry=False)
    return JsonResponse("enqueued.", safe=False)
