"""
Serializers for use in the support app.
"""
from rest_framework import serializers

from entitlements.api.v1.serializers import CourseEntitlementSerializer
from entitlements.models import CourseEntitlement, CourseEntitlementSupportDetail
from student.models import ManualEnrollmentAudit


class ManualEnrollmentSerializer(serializers.ModelSerializer):
    """Serializes a manual enrollment audit object."""
    enrolled_by = serializers.SlugRelatedField(slug_field='email', read_only=True, default='')

    class Meta(object):
        model = ManualEnrollmentAudit
        fields = ('enrolled_by', 'time_stamp', 'reason')
