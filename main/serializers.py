from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Experience, Education


class ExperienceSerializer(serializers.ModelSerializer):
    is_ongoing = serializers.ReadOnlyField()
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id", "title", "organization", "description", "category",
            "thumbnail", "started_at", "ended_at", "is_ongoing",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_organization(self, value):
        return strip_tags(value).strip()

    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Description cannot be empty.")
        return value

    def validate(self, attrs):
        super().validate(attrs)
        started_at = attrs.get("started_at", getattr(self.instance, "started_at", None))
        ended_at = attrs.get("ended_at", getattr(self.instance, "ended_at", None))
        if started_at is not None and ended_at is not None and ended_at < started_at:
            raise serializers.ValidationError({
                "ended_at": "End date cannot be earlier than start date.",
            })
        return attrs

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())

class EducationSerializer(serializers.ModelSerializer):
    is_ongoing = serializers.ReadOnlyField()
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Education
        fields = [
            "id",
            "degree",
            "gpa",
            "school",
            "thumbnail",
            "started_at",
            "ended_at",
            "is_ongoing",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_degree(self, value):
        value = strip_tags(value).strip()

        if not value:
            raise serializers.ValidationError(
                "Degree cannot be empty."
            )

        return value

    def validate_school(self, value):
        value = strip_tags(value).strip()

        if not value:
            raise serializers.ValidationError(
                "School cannot be empty."
            )

        return value

    def validate(self, attrs):
        attrs = super().validate(attrs)

        started_at = attrs.get(
            "started_at",
            getattr(self.instance, "started_at", None)
        )
        ended_at = attrs.get(
            "ended_at",
            getattr(self.instance, "ended_at", None)
        )

        if (
            started_at is not None
            and ended_at is not None
            and ended_at < started_at
        ):
            raise serializers.ValidationError({
                "ended_at": "End date cannot be earlier than start date."
            })

        return attrs

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")

        if request is None or not request.user.is_authenticated:
            return False

        return obj.starred_by.filter(
            pk=request.user.pk
        ).exists()

    def get_starred_by_names(self, obj):
        return ", ".join(
            user.username for user in obj.starred_by.all()
        )