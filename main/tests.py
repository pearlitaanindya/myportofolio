
from django.test import TestCase
from django.urls import reverse

from main.models import Experience, Education


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
            started_at="2026-08-06"
        )

        self.education = Education.objects.create(
            degree="Bachelor of Computer Science",
            school="Universitas Indonesia",
            gpa=3.62,
            started_at="2025-08-25"
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(
            response,
            f'href="{reverse("main:show_experience")}"'
        )

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")
        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")

        self.assertContains(response, 'id="experience-search-form"')
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, reverse("api:experience-list"))
        self.assertContains(
            response,
            f'href="{reverse("main:show_main")}"'
        )

        api_response = self.client.get(
            reverse("api:experience-list")
        )

        self.assertEqual(api_response.status_code, 200)

        experiences = api_response.json()

        self.assertEqual(len(experiences), 1)
        self.assertEqual(
            experiences[0]["title"],
            self.experience.title
        )
        self.assertEqual(
            experiences[0]["description"],
            self.experience.description
        )
        self.assertEqual(
            experiences[0]["category"],
            "part-time"
        )
        self.assertEqual(
            experiences[0]["started_at"],
            "2026-08-06"
        )
        self.assertIsNone(experiences[0]["ended_at"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()

        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No experiences found.")

        api_response = self.client.get(
            reverse("api:experience-list")
        )

        self.assertEqual(api_response.status_code, 200)
        self.assertEqual(api_response.json(), [])

    def test_completed_experience(self):
        self.experience.ended_at = "2026-09-10"
        self.experience.save()

        self.assertFalse(self.experience.is_ongoing)

        api_response = self.client.get(
            reverse(
                "api:experience-detail",
                args=[self.experience.id]
            )
        )

        self.assertEqual(api_response.status_code, 200)

        experience_data = api_response.json()

        self.assertEqual(
            experience_data["ended_at"],
            "2026-09-10"
        )
        self.assertFalse(experience_data["is_ongoing"])

        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")

    # unit test  Education model
    def test_education_model(self):
        self.assertEqual(
            str(self.education),
            "Bachelor of Computer Science"
        )
        self.assertEqual(self.education.gpa, 3.62)
        self.assertEqual(
            self.education.school,
            "Universitas Indonesia"
        )
        self.assertTrue(self.education.is_ongoing)

    # unit test Education page
    def test_education_page(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")

        self.assertContains(response, 'id="education-search-form"')
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, reverse("api:education-list"))

        self.assertContains(
            response,
            f'href="{reverse("main:show_main")}"'
        )

        self.assertTrue(
            Education.objects.filter(
                pk=self.education.pk,
                degree="Bachelor of Computer Science",
                school="Universitas Indonesia"
            ).exists()
        )

    # unit test empty Education page
    def test_empty_education_page(self):
        Education.objects.all().delete()

        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "No education has been added or found."
        )

        self.assertFalse(Education.objects.exists())

    # unit test Education yang sudah completed
    def test_completed_education(self):
        self.education.ended_at = "2026-10-01"
        self.education.save()

        self.education.refresh_from_db()

        self.assertFalse(self.education.is_ongoing)
        self.assertEqual(
            self.education.ended_at.isoformat(),
            "2026-10-01"
        )

        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, 'id="grid"')