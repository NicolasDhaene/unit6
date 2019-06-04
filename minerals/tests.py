from django.urls import reverse
from django.test import TestCase

from .models import Mineral


test_mineral = {
    "name": "Thortveitite",
    "image_filename": "thortveitite.jpg",
    "image_caption": "thortveitite",
    "formula": "(Sc,Y)<sub>2</sub>Si<sub>2</sub>O<sub>7</sub>",
    "crystal_system": "orthorhombic",
    "mohs_scale_hardness": "5–6",
    "luster": "vitreous",
    "streak": "gray",
    "specific_gravity": "3.3-3.8",
}

class MineralViewTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(**test_mineral)

    def test_index_view(self):
        resp = self.client.get(reverse("index"))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context["minerals"])
        self.assertTemplateUsed(resp, "minerals/index.html")
        self.assertContains(resp, self.mineral.name)


    def test_detail_view(self):
        resp = self.client.get(reverse("detail",
                                        kwargs={"pk": self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context["mineral"])