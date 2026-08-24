from rest_framework import serializers

from .models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.email")

    class Meta:
        model = Organization
        fields = ["id", "name", "slug", "description", "owner", "created_at", "updated_at"]
        read_only_fields = ["id", "slug", "owner", "created_at", "updated_at"]

    # def create(self, validated_data):
    #     user = self.context["request"].user
    #     return Organization.objects.create(owner=user, **validated_data)
