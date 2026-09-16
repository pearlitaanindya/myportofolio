from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateInput

from main.models import Experience

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "organization",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Position",
            "organization" : "Company/Organization",
            "description": "Experience Description",
            "category": "Experience Category",
            "thumbnail": "Company Logo",
            "started_at": "Start Date",
            "ended_at" : "End Date",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Experience Position",
                    "maxlength": 255,
                }
            ),
            "organization": TextInput(
                            attrs={
                                "placeholder": "Enter your organization/company",
                                "maxlength": 255,
                            }
                        ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your experience",
                    "rows": 3,
                }
            ),
            "category": Select(),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "Image URL",
                }
            ),
            "started_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "ended_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }