# -*- coding: utf-8 -*-
{
    "name": "NovaConsult Pro Theme",
    "summary": "High-conversion dark consulting theme (NovaConsult Pro)",
    "version": "18.0.1.0.0",
    "category": "Theme/Services",
    "license": "LGPL-3",
    "author": "ResilientByte",
    'price': 30,
'currency': 'EUR',
'license': 'LGPL-3',
'installable': True,
'application': False,
    "website": "https://apps.odoo.com",
    "depends": ["website"],
    "data": [
        # Layout
        "views/theme_layout.xml",

        # Snippet registry + options

        "views/snippets/options.xml",
        # "views/snippets/snippets.xml",

        # All snippet templates (exactly what you have in /views/snippets)
        "views/snippets/s_novaconsult_hero.xml",
        "views/snippets/s_novaconsult_services.xml",
        "views/snippets/s_novaconsult_pricing.xml",
        "views/snippets/s_novaconsult_contact.xml",

        "views/snippets/s_nova_topbar.xml",
        "views/snippets/s_nova_header.xml",

        "views/snippets/s_nova_hero.xml",
        "views/snippets/s_nova_hero_split.xml",
        "views/snippets/s_nova_hero_center.xml",

        "views/snippets/s_nova_logos.xml",
        "views/snippets/s_nova_stats.xml",
        "views/snippets/s_nova_features.xml",

        "views/snippets/s_nova_value_props.xml",
        "views/snippets/s_nova_services.xml",
        "views/snippets/s_nova_method.xml",
        "views/snippets/s_nova_case_studies.xml",
        "views/snippets/s_nova_testimonials.xml",
        "views/snippets/s_nova_pricing.xml",
        "views/snippets/s_nova_faq.xml",
        "views/snippets/s_nova_contact_cta.xml",
                "views/snippets/s_nova_footer.xml",

        # Full-page snippets (importable as blocks)
        "views/snippets/snip_consulting_home.xml",
        "views/snippets/snip_consulting_services.xml",
        "views/snippets/snip_consulting_pricing.xml",
        "views/snippets/snip_consulting_cases.xml",
        "views/snippets/snip_consulting_method.xml",
        "views/snippets/snip_consulting_contact.xml",
"views/header_templates.xml",
"views/footer_templates.xml",
    ],

    'images': [
    'static/description/theme_novaconsult_pro_cover.png',
    'static/description/screenshot.webp',
],

    "assets": {

        # ----------------------------------------------------
        # CSS Variables (before bootstrap)
        # ----------------------------------------------------
        "web._assets_primary_variables": [
            "theme_novaconsult_pro/static/src/scss/primary_variables.scss",
        ],

        # ----------------------------------------------------
        # Public Frontend
        # ----------------------------------------------------
        "web.assets_frontend": [
            "theme_novaconsult_pro/static/src/scss/theme.scss",
        ],

        # ----------------------------------------------------
        # Website Builder (critical for snippet styling)
        # ----------------------------------------------------
        "website.assets_wysiwyg": [
            "theme_novaconsult_pro/static/src/scss/theme.scss",
        ],
        "website.assets_wysiwyg_inside": [
            "theme_novaconsult_pro/static/src/scss/theme.scss",
        ],
    },

    "installable": True,
    "application": False,
}