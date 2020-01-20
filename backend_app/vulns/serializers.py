from rest_framework import serializers
from .models import VulnMetadata, ExploitMetadata


class VulnMetadataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VulnMetadata
        fields = [
            'cve_id', 'summary', 'published', 'modified', 'assigner',
            'cvss', 'cvss_time', 'cvss_vector',
            'cwe', 'access', 'impact', 'vulnerable_products',
            'is_exploitable', 'exploit_ref', 'exploit_info',
            'raw',
            'created_at', 'updated_at']


class ExploitMetadataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExploitMetadata
        fields = [
            'vuln', 'links', 'notes',
            'trust_level', 'tlp_level', 'source',
            'availability', 'type', 'maturity',
            'created_at', 'updated_at']
