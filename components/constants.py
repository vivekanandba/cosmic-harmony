# class_categories = {'Iron Meteorites': ['Iron, IVB',
#    'Iron, IIIAB',
#    'Iron, IAB-MG',
#    'Iron, IIIE',
#    'Iron, IVA',
#    'Iron, IAB-ung',
#    'Iron, IIAB',
#    'Iron, ungrouped',
#    'Iron, IC',
#    'Iron, IAB complex',
#    'Iron, IAB-sLL',
#    'Iron',
#    'Iron, IIIAB-an',
#    'Iron, IID',
#    'Iron, IIE',
#    'Iron, IIE-an',
#    'Iron, IIIF',
#    'Iron, IVA-an',
#    'Iron, IAB-sHL',
#    'Iron, IAB-sLM',
#    'Iron, IIC',
#    'Iron, IIIE-an',
#    'Iron, IC-an'],
#   'Stony Meteorites - Chondrites': ['H5',
#    'L5',
#    'L6',
#    'H4',
#    'L/LL5',
#    'LL5',
#    'L/LL4',
#    'L5-6',
#    'H6',
#    'H3.6',
#    'LL6',
#    'L4',
#    'H4/5',
#    'L/LL6',
#    'H3.7',
#    'L4-5',
#    'H3-6',
#    'H5-6',
#    'L5/6',
#    'H3',
#    'EH4',
#    'H3-4',
#    'LL4',
#    'LL3.6',
#    'L3.6',
#    'L3',
#    'H3.8-4',
#    'LL3.2',
#    'H3.8'],
#   'Stony Meteorites - Achondrites': ['Aubrite',
#    'CV3',
#    'Eucrite-mmict',
#    'CO3.2',
#    'Stone-uncl',
#    'CBa',
#    'CR-an',
#    'CM2',
#    'CO3',
#    'CO3.5'],
#   'Stony-Iron Meteorites - Pallasites': ['Pallasite, PMG-an',
#    'Pallasite, PMG'],
#   'Stony-Iron Meteorites - Mesosiderites': ['Mesosiderite-A1',
#    'Mesosiderite-B4',
#    'Mesosiderite-A3/4',
#    'Mesosiderite-C',
#    'Mesosiderite',
#    'Mesosiderite-A3',
#    'Mesosiderite-B2',
#    'Mesosiderite-C2']}


#  {'Iron Meteorites': 23,
#   'Stony Meteorites - Chondrites': 29,
#   'Stony Meteorites - Achondrites': 10,
#   'Stony-Iron Meteorites - Pallasites': 2,
#   'Stony-Iron Meteorites - Mesosiderites': 8})

# class_categories = {
#     "Iron Meteorites - Category I": {
#         "IA": [
#             "Iron, IIIAB",
#             "Iron, IAB-MG",
#             "Iron, IAB-ung",
#             "Iron, IIAB",
#             "Iron, IAB complex",
#             "Iron, IAB-sLL",
#             "Iron, IIIAB-an",
#             "Iron, IAB-sHL",
#             "Iron, IAB-sLM"
#         ],
#         "IB": []
#     },
#     "Iron Meteorites - Category II": {
#         "IIA": [],
#         "IIB": [],
#         "IIC": [
#             "Iron, IIC"
#         ],
#         "IID": [
#             "Iron, IID"
#         ],
#         "IIE": [
#             "Iron, IIIE",
#             "Iron, IIE",
#             "Iron, IIE-an",
#             "Iron, IIIE-an"
#         ]
#     },
#     "Iron Meteorites - Category III": {
#         "IIIA & IIIB": [],
#         "IIIC & IIID": [],
#         "IIIE": []
#     },
#     "Iron Meteorites - Category IV": {
#         "IVA": [
#             "Iron, IVA",
#             "Iron, IVA-an"
#         ],
#         "IVB": [
#             "Iron, IVB"
#         ]
#     },
#     "Iron Meteorites - Category U (Uncategorized)": {
#         "Uncategorized": [
#             "Iron, ungrouped"
#         ]
#     },
#     "Stony Meteorites - Chondrites": [
#         "H5",
#         "L5",
#         "L6",
#         "H4",
#         "L/LL5",
#         "LL5",
#         "L/LL4",
#         "L5-6",
#         "H6",
#         "H3.6",
#         "LL6",
#         "L4",
#         "H4/5",
#         "L/LL6",
#         "H3.7",
#         "L4-5",
#         "H3-6",
#         "H5-6",
#         "L5/6",
#         "H3",
#         "EH4",
#         "H3-4",
#         "LL4",
#         "LL3.6",
#         "L3.6",
#         "L3",
#         "H3.8-4",
#         "LL3.2",
#         "H3.8"
#     ],
#     "Stony Meteorites - Achondrites": [
#         "Aubrite",
#         "CV3",
#         "Eucrite-mmict",
#         "CO3.2",
#         "Stone-uncl",
#         "CBa",
#         "CR-an",
#         "CM2",
#         "CO3",
#         "CO3.5"
#     ],
#     "Stony-Iron Meteorites - Pallasites": [
#         "Pallasite, PMG-an",
#         "Pallasite, PMG"
#     ],
#     "Stony-Iron Meteorites - Mesosiderites": [
#         "Mesosiderite-A1",
#         "Mesosiderite-B4",
#         "Mesosiderite-A3/4",
#         "Mesosiderite-C",
#         "Mesosiderite",
#         "Mesosiderite-A3",
#         "Mesosiderite-B2",
#         "Mesosiderite-C2"
#     ],
#     "Other Categories": {
#         "Other": [
#             "Iron, IC",
#             "Iron",
#             "Iron, IIIF",
#             "Iron, IC-an"
#         ]
#     }
# }

class_categories = {
    "Iron Meteorites - Category I": [
        "Iron, IIIAB",
        "Iron, IAB-MG",
        "Iron, IAB-ung",
        "Iron, IIAB",
        "Iron, IAB complex",
        "Iron, IAB-sLL",
        "Iron, IIIAB-an",
        "Iron, IAB-sHL",
        "Iron, IAB-sLM"
    ],
    "Iron Meteorites - Category II": [
        "Iron, IIC",
        "Iron, IID",
        "Iron, IIIE",
        "Iron, IIE",
        "Iron, IIE-an",
        "Iron, IIIE-an"
    ],
    "Iron Meteorites - Category III": [],
    "Iron Meteorites - Category IV": [
        "Iron, IVA",
        "Iron, IVA-an",
        "Iron, IVB"
    ],
    "Iron Meteorites - Category U (Uncategorized)": [
        "Iron, ungrouped"
    ],
    "Stony Meteorites - Chondrites": [
        "H5",
        "L5",
        "L6",
        "H4",
        "L/LL5",
        "LL5",
        "L/LL4",
        "L5-6",
        "H6",
        "H3.6",
        "LL6",
        "L4",
        "H4/5",
        "L/LL6",
        "H3.7",
        "L4-5",
        "H3-6",
        "H5-6",
        "L5/6",
        "H3",
        "EH4",
        "H3-4",
        "LL4",
        "LL3.6",
        "L3.6",
        "L3",
        "H3.8-4",
        "LL3.2",
        "H3.8"
    ],
    "Stony Meteorites - Achondrites": [
        "Aubrite",
        "CV3",
        "Eucrite-mmict",
        "CO3.2",
        "Stone-uncl",
        "CBa",
        "CR-an",
        "CM2",
        "CO3",
        "CO3.5"
    ],
    "Stony-Iron Meteorites - Pallasites": [
        "Pallasite, PMG-an",
        "Pallasite, PMG"
    ],
    "Stony-Iron Meteorites - Mesosiderites": [
        "Mesosiderite-A1",
        "Mesosiderite-B4",
        "Mesosiderite-A3/4",
        "Mesosiderite-C",
        "Mesosiderite",
        "Mesosiderite-A3",
        "Mesosiderite-B2",
        "Mesosiderite-C2"
    ],
    "Other Categories": [
        "Iron, IC",
        "Iron",
        "Iron, IIIF",
        "Iron, IC-an"
    ]
}

class_colors = {
    "Iron Meteorites - Category I": "#1f77b4",
    "Iron Meteorites - Category II": "#ff7f0e",
    "Iron Meteorites - Category III": "#2ca02c",
    "Iron Meteorites - Category IV": "#d62728",
    "Iron Meteorites - Category U (Uncategorized)": "#9467bd",
    "Stony Meteorites - Chondrites": "#8c564b",
    "Stony Meteorites - Achondrites": "#e377c2",
    "Stony-Iron Meteorites - Pallasites": "#7f7f7f",
    "Stony-Iron Meteorites - Mesosiderites": "#bcbd22",
    "Other Categories": "#17becf"
}