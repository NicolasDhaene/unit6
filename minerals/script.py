from minerals.models import Mineral

import json

csv_file = "minerals.json"

with open(csv_file, encoding='utf-8') as csv_file:
    minerals = json.load(csv_file)
    for mineral in minerals:
        Mineral(
            name = mineral['name'],
            img_filename = mineral['image_filename'],
            img_caption = mineral['image_caption'],
            category = mineral['category'],
            formula = mineral['formula'],
            strunz_classification = mineral['strunz_classification'],
            crystal_system = mineral['crystal_system'],
            unit_cell = mineral['unit_cell'],
            color = mineral['color'],
            crystal_symmetry = mineral['crystal_symmetry'],
            cleavage = mineral['cleavage'],
            mohs_hardness = mineral['mohs_scale_hardness'],
            luster = mineral['luster'],
            streak = mineral['streak'],
            diaphaneity = mineral['diaphaneity'],
            optical_properties = mineral['optical_properties'],
            refractive_index = mineral['refractive_index'],
            crystal_habit = mineral['crystal_habit'],
            specific_gravity = mineral['specific_gravity']
        ).save()