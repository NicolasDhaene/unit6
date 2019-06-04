from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from minerals.models import Mineral
import json
import random


def add_json_to_db(request):
    csv_file = "minerals.json"
    with open(csv_file, encoding="utf-8") as csv_file:
        minerals = json.load(csv_file)
        for mineral in minerals:
            # create a blank dict
            full_mineral_dict = {
                "name": None,
                "image_filename": None,
                "image_caption": None,
                "category": None,
                "formula": None,
                "strunz_classification": None,
                "crystal_system": None,
                "unit_cell": None,
                "color": None,
                "crystal_symmetry": None,
                "cleavage": None,
                "mohs_scale_hardness": None,
                "luster": None,
                "streak": None,
                "diaphaneity": None,
                "optical_properties": None,
                "refractive_index": None,
                "crystal_habit": None,
                "specific_gravity": None}
            # populate blank dict when information available
            for key, value in mineral.items():
                full_mineral_dict[key] = value
            # check if mineral already outstanding, create if not
            try:
                Mineral.objects.get(name=full_mineral_dict["name"])
                continue
            except Mineral.DoesNotExist:
                Mineral(
                    name=full_mineral_dict["name"],
                    image_filename=full_mineral_dict["image_filename"],
                    image_caption=full_mineral_dict["image_caption"],
                    category=full_mineral_dict["category"],
                    formula=full_mineral_dict["formula"],
                    strunz_classification=full_mineral_dict["strunz_classification"],
                    crystal_system=full_mineral_dict["crystal_system"],
                    unit_cell=full_mineral_dict["unit_cell"],
                    color=full_mineral_dict["color"],
                    crystal_symmetry=full_mineral_dict["crystal_symmetry"],
                    cleavage=full_mineral_dict["cleavage"],
                    mohs_scale_hardness=full_mineral_dict["mohs_scale_hardness"],
                    luster=full_mineral_dict["luster"],
                    streak=full_mineral_dict["streak"],
                    diaphaneity=full_mineral_dict["diaphaneity"],
                    optical_properties=full_mineral_dict["optical_properties"],
                    refractive_index=full_mineral_dict["refractive_index"],
                    crystal_habit=full_mineral_dict["crystal_habit"],
                    specific_gravity=full_mineral_dict["specific_gravity"]
                ).save()
    return HttpResponse("It is done.")


def mineral_list(request):
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    return render(request, "minerals/index.html", {"minerals": minerals, "random_mineral": random_mineral})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    attributes_sorted_most_common = mineral.attributes_sorted_most_common()
    return render(request, "minerals/detail.html", {'mineral': mineral,
                                                    "attributes": attributes_sorted_most_common})
