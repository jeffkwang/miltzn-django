from square import client
import os
# from .secrets import square_api_token

square_client = client.Client(
    access_token=os.getenv('SQUARE_API_KEY'),
    environment='production'  # Change to 'production' in a live environment
)

if __name__ == "__main__":
    # result = square_client.locations.list_locations()

    # if result.is_success():
    #     for location in result.body['locations']:
    #         print(f"{location['id']}: ", end="")
    #         print(f"{location['name']}, ", end="")
    #         print(f"{location['address']['address_line_1']}, ", end="")
    #         print(f"{location['address']['locality']}")

    # elif result.is_error():
    #     for error in result.errors:
    #         print(error['category'])
    #         print(error['code'])
    #         print(error['detail'])

    result = client.catalog.batch_upsert_catalog_objects(
    body = {
        "idempotency_key": "91529edd-a731-43de-8f40-bcafcd9498df",
        "batches": [
            {
                "objects": [
                    {
                    "type": "CATEGORY",
                    "id": "REOANBFLTGQF3MVSCFMVZKAZ",
                    "updated_at": "2024-02-14T00:19:16.542Z",
                    "created_at": "2024-02-13T22:04:22.898Z",
                    "version": 1707869956542,
                    "is_deleted": false,
                    "present_at_all_locations": true,
                    "category_data": {
                        "name": "Pillows",
                        "image_ids": [
                        "36R55TQJVIVUQN4UGD3UPNHH"
                        ],
                        "category_type": "REGULAR_CATEGORY",
                        "parent_category": {
                        "ordinal": -2251731094208512
                        },
                        "is_top_level": true,
                        "channels": [
                        "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                        ],
                        "online_visibility": true,
                        "ecom_seo_data": {
                        "page_title": "",
                        "page_description": "",
                        "permalink": ""
                        }
                    }
                    },
                    {
                    "type": "CUSTOM_ATTRIBUTE_DEFINITION",
                    "id": "M4UFH6GML7VWMPSPGGUW7M42",
                    "updated_at": "2024-02-13T22:05:12.88Z",
                    "created_at": "2024-02-13T22:05:12.88Z",
                    "version": 1707861912880,
                    "is_deleted": false,
                    "present_at_all_locations": true,
                    "custom_attribute_definition_data": {
                        "type": "BOOLEAN",
                        "name": "Is Alcoholic",
                        "description": "Enabling this toggle on an item indicates that it contains alcohol.",
                        "source_application": {
                        "application_id": "sq0idp-w46nJ_NCNDMSOywaCY0mwA",
                        "name": "Square Online Store"
                        },
                        "allowed_object_types": [
                        "ITEM"
                        ],
                        "seller_visibility": "SELLER_VISIBILITY_HIDDEN",
                        "app_visibility": "APP_VISIBILITY_HIDDEN",
                        "key": "is_alcoholic"
                    }
                    },
                    {
                    "type": "CUSTOM_ATTRIBUTE_DEFINITION",
                    "id": "ZBLNMNKYCGYKP6DAE6CEE436",
                    "updated_at": "2024-02-13T22:05:13.099Z",
                    "created_at": "2024-02-13T22:05:13.099Z",
                    "version": 1707861913099,
                    "is_deleted": false,
                    "present_at_all_locations": true,
                    "custom_attribute_definition_data": {
                        "type": "STRING",
                        "name": "Ecom Storefront Classic Site ID",
                        "description": "Ecommerce bridge target storefront classic site ID. Used to create site-item associations after copying items.",
                        "source_application": {
                        "application_id": "sq0idp-w46nJ_NCNDMSOywaCY0mwA",
                        "name": "Square Online Store"
                        },
                        "allowed_object_types": [
                        "ITEM"
                        ],
                        "seller_visibility": "SELLER_VISIBILITY_HIDDEN",
                        "app_visibility": "APP_VISIBILITY_HIDDEN",
                        "string_config": {
                        "enforce_uniqueness": false
                        },
                        "key": "ecom_target_classic_site_id"
                    }
                    },
                    {
                    "type": "ITEM",
                    "id": "J7PMV33TQ3BJ4KGFOAHKYGKA",
                    "updated_at": "2024-02-14T00:37:22.349Z",
                    "created_at": "2024-02-13T22:05:31.033Z",
                    "version": 1707871042349,
                    "is_deleted": false,
                    "present_at_all_locations": true,
                    "item_data": {
                        "name": "Primordial Sun - Tufted Square Pillow",
                        "description": "One-sided - Acrylic / Cotton & Polyester construction \nPillow insert included with purchase \nZipped back \nMade in the USA with imported and domestic materials \n\nContains latex",
                        "is_taxable": true,
                        "visibility": "PRIVATE",
                        "variations": [
                        {
                            "type": "ITEM_VARIATION",
                            "id": "TMFHYEABUA2NSSNGUE55RU5Q",
                            "updated_at": "2024-02-14T00:28:14.173Z",
                            "created_at": "2024-02-13T22:05:31.033Z",
                            "version": 1707870494173,
                            "is_deleted": false,
                            "present_at_all_locations": true,
                            "item_variation_data": {
                            "item_id": "J7PMV33TQ3BJ4KGFOAHKYGKA",
                            "name": "Regular",
                            "ordinal": 1,
                            "pricing_type": "FIXED_PRICING",
                            "price_money": {
                                "amount": 3399,
                                "currency": "USD"
                            },
                            "location_overrides": [
                                {
                                "location_id": "LR94XVQK1SCP6",
                                "track_inventory": true
                                }
                            ],
                            "track_inventory": true,
                            "inventory_alert_type": "NONE",
                            "sellable": true,
                            "stockable": true,
                            "image_ids": [
                                "OSYYH3XYSEEW5CKEYRMUCDQU"
                            ],
                            "channels": [
                                "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                            ]
                            }
                        },
                        {
                            "type": "ITEM_VARIATION",
                            "id": "COG3B3GQB5RDJBYHGZCSFKED",
                            "updated_at": "2024-02-14T00:28:52.453Z",
                            "created_at": "2024-02-14T00:28:14.173Z",
                            "version": 1707870532453,
                            "is_deleted": false,
                            "present_at_all_locations": true,
                            "item_variation_data": {
                            "item_id": "J7PMV33TQ3BJ4KGFOAHKYGKA",
                            "name": "Large Tufted Pillow",
                            "ordinal": 2,
                            "pricing_type": "FIXED_PRICING",
                            "price_money": {
                                "amount": 4500,
                                "currency": "USD"
                            },
                            "location_overrides": [
                                {
                                "location_id": "LR94XVQK1SCP6",
                                "track_inventory": true
                                }
                            ],
                            "track_inventory": false,
                            "sellable": true,
                            "stockable": true,
                            "channels": [
                                "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                            ]
                            }
                        }
                        ],
                        "product_type": "REGULAR",
                        "skip_modifier_screen": false,
                        "ecom_uri": "https://miltzn.square.site/product/primordial-sun-pillow/1",
                        "ecom_image_uris": [
                        "https://miltzn.square.site/uploads/1/4/8/7/148703844/s833352963451389956_p1_i1_w1000.png"
                        ],
                        "ecom_available": true,
                        "ecom_visibility": "VISIBLE",
                        "image_ids": [
                        "OSYYH3XYSEEW5CKEYRMUCDQU"
                        ],
                        "categories": [
                        {
                            "id": "REOANBFLTGQF3MVSCFMVZKAZ",
                            "ordinal": -2251799813685248
                        }
                        ],
                        "pickup_fulfillment_preferences_id": "fprefs_127wzwe6dqlnzq8koidhoi1pa",
                        "delivery_fulfillment_preferences_id": "fprefs_127wzwe6d73pswxr5uqn4ukv2",
                        "description_html": "<ul><li>One-sided - Acrylic / Cotton &amp; Polyester construction </li><li>Pillow insert included with purchase </li><li>Zipped back </li><li>Made in the USA with imported and domestic materials </li></ul><p><br/></p><p><strong>Contains latex</strong></p>",
                        "description_plaintext": "One-sided - Acrylic / Cotton & Polyester construction \nPillow insert included with purchase \nZipped back \nMade in the USA with imported and domestic materials \n\nContains latex",
                        "channels": [
                        "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                        ],
                        "shipping_fulfillment_preferences_id": "fprefs_127wzwe6e0bcldvfg9w58t0ri",
                        "dine_in_fulfillment_preferences_id": "fprefs_127wzwe6dh698h2h1z0i6s7xa",
                        "is_archived": false,
                        "ecom_seo_data": {
                        "page_title": "Primordial Sun Square Pillow",
                        "page_description": "Acrylic 12\" x 12\" square throw pillow with primordial sun tufted design.",
                        "permalink": "primordial-sun-pillow"
                        },
                        "reporting_category": {
                        "id": "REOANBFLTGQF3MVSCFMVZKAZ",
                        "ordinal": -2251799813685248
                        }
                    }
                    },
                    {
                    "type": "CATEGORY",
                    "id": "INBOTX6EO6KJZXMUOXW26WVS",
                    "updated_at": "2024-02-14T00:20:00.882Z",
                    "created_at": "2024-02-14T00:19:04.705Z",
                    "version": 1707870000882,
                    "is_deleted": false,
                    "present_at_all_locations": true,
                    "category_data": {
                        "name": "Floor Cushions",
                        "image_ids": [
                        "55RSHCVIAJAA3XOKYQCISTLZ"
                        ],
                        "category_type": "REGULAR_CATEGORY",
                        "parent_category": {
                        "ordinal": -2251662374731776
                        },
                        "is_top_level": true,
                        "channels": [
                        "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                        ],
                        "online_visibility": true,
                        "ecom_seo_data": {
                        "page_title": "",
                        "page_description": "",
                        "permalink": ""
                        }
                    }
                    },
                    {
                    "type": "ITEM",
                    "id": "Z2VJD7LVOIXEFWGSRKWGC2NA",
                    "updated_at": "2024-02-14T00:37:22.15Z",
                    "created_at": "2024-02-14T00:27:02.843Z",
                    "version": 1707871042150,
                    "is_deleted": false,
                    "present_at_all_locations": false,
                    "present_at_location_ids": [
                        "LR94XVQK1SCP6"
                    ],
                    "item_data": {
                        "name": "Sausage Dog - Tufted Square Throw Pillow",
                        "description": "One-sided - Acrylic / Cotton & Polyester construction \nPillow insert included with purchase \nZipped back \nMade in the USA with imported and domestic materials \n\nContains latex",
                        "is_taxable": true,
                        "visibility": "PRIVATE",
                        "variations": [
                        {
                            "type": "ITEM_VARIATION",
                            "id": "EFEMIP72TBVDV5TZ5427TDJ6",
                            "updated_at": "2024-02-14T00:27:22.188Z",
                            "created_at": "2024-02-14T00:27:02.843Z",
                            "version": 1707870442188,
                            "is_deleted": false,
                            "present_at_all_locations": false,
                            "present_at_location_ids": [
                            "LR94XVQK1SCP6"
                            ],
                            "item_variation_data": {
                            "item_id": "Z2VJD7LVOIXEFWGSRKWGC2NA",
                            "name": "Regular",
                            "ordinal": 1,
                            "pricing_type": "FIXED_PRICING",
                            "price_money": {
                                "amount": 3399,
                                "currency": "USD"
                            },
                            "location_overrides": [
                                {
                                "location_id": "LR94XVQK1SCP6",
                                "track_inventory": true
                                }
                            ],
                            "track_inventory": true,
                            "inventory_alert_type": "NONE",
                            "sellable": true,
                            "stockable": true,
                            "image_ids": [
                                "MQEMAHCNYMRK4PWPFLVNAYRK"
                            ],
                            "channels": [
                                "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                            ]
                            }
                        },
                        {
                            "type": "ITEM_VARIATION",
                            "id": "WECQIOOZTLNPHWN75TPAIEQ7",
                            "updated_at": "2024-02-14T00:27:40.213Z",
                            "created_at": "2024-02-14T00:27:02.843Z",
                            "version": 1707870460213,
                            "is_deleted": false,
                            "present_at_all_locations": false,
                            "present_at_location_ids": [
                            "LR94XVQK1SCP6"
                            ],
                            "item_variation_data": {
                            "item_id": "Z2VJD7LVOIXEFWGSRKWGC2NA",
                            "name": "Large Tufted Throw PIllow",
                            "ordinal": 2,
                            "pricing_type": "FIXED_PRICING",
                            "price_money": {
                                "amount": 4500,
                                "currency": "USD"
                            },
                            "location_overrides": [
                                {
                                "location_id": "LR94XVQK1SCP6",
                                "track_inventory": true
                                }
                            ],
                            "track_inventory": false,
                            "sellable": true,
                            "stockable": true,
                            "image_ids": [
                                "MQEMAHCNYMRK4PWPFLVNAYRK"
                            ],
                            "channels": [
                                "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                            ]
                            }
                        }
                        ],
                        "product_type": "REGULAR",
                        "skip_modifier_screen": false,
                        "ecom_uri": "https://miltzn.square.site/product/primordial-sun-pillow/2",
                        "ecom_image_uris": [
                        "https://miltzn.square.site/uploads/1/4/8/7/148703844/s833352963451389956_p2_i1_w1000.png"
                        ],
                        "ecom_available": true,
                        "ecom_visibility": "VISIBLE",
                        "image_ids": [
                        "MQEMAHCNYMRK4PWPFLVNAYRK"
                        ],
                        "categories": [
                        {
                            "id": "REOANBFLTGQF3MVSCFMVZKAZ",
                            "ordinal": -2251731094208512
                        }
                        ],
                        "pickup_fulfillment_preferences_id": "fprefs_127x00n15srmlnqaieood71r4",
                        "delivery_fulfillment_preferences_id": "fprefs_127x00n14u9wolta3imvwatuo",
                        "description_html": "<ul><li>One-sided - Acrylic / Cotton &amp; Polyester construction </li><li>Pillow insert included with purchase </li><li>Zipped back </li><li>Made in the USA with imported and domestic materials </li></ul><p><br/></p><p><strong>Contains latex</strong></p>",
                        "description_plaintext": "One-sided - Acrylic / Cotton & Polyester construction \nPillow insert included with purchase \nZipped back \nMade in the USA with imported and domestic materials \n\nContains latex",
                        "channels": [
                        "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                        ],
                        "shipping_fulfillment_preferences_id": "fprefs_127x00n169ccobnd83r2w81i8",
                        "dine_in_fulfillment_preferences_id": "fprefs_127x00n15bqpofqh2wixs3s80",
                        "is_archived": false,
                        "ecom_seo_data": {
                        "page_title": "Primordial Sun Square Pillow",
                        "page_description": "Acrylic 12\" x 12\" square throw pillow with primordial sun tufted design.",
                        "permalink": "primordial-sun-pillow"
                        },
                        "reporting_category": {
                        "id": "REOANBFLTGQF3MVSCFMVZKAZ",
                        "ordinal": -2251731094208512
                        }
                    }
                    },
                    {
                    "type": "ITEM",
                    "id": "GI4AQIQ5LGBN4ZULGFY5DQ24",
                    "updated_at": "2024-02-14T00:37:21.941Z",
                    "created_at": "2024-02-14T00:29:24.79Z",
                    "version": 1707871041941,
                    "is_deleted": false,
                    "present_at_all_locations": false,
                    "present_at_location_ids": [
                        "LR94XVQK1SCP6"
                    ],
                    "item_data": {
                        "name": "Button Mushrooms - Tufted Square Pillow",
                        "description": "One-sided - Acrylic / Cotton & Polyester construction \nPillow insert included with purchase \nZipped back \nMade in the USA with imported and domestic materials \n\nContains latex",
                        "is_taxable": true,
                        "visibility": "PRIVATE",
                        "variations": [
                        {
                            "type": "ITEM_VARIATION",
                            "id": "2M4IUM3QK26XMWT62UAXRONI",
                            "updated_at": "2024-02-14T00:29:57.25Z",
                            "created_at": "2024-02-14T00:29:24.79Z",
                            "version": 1707870597250,
                            "is_deleted": false,
                            "present_at_all_locations": false,
                            "present_at_location_ids": [
                            "LR94XVQK1SCP6"
                            ],
                            "item_variation_data": {
                            "item_id": "GI4AQIQ5LGBN4ZULGFY5DQ24",
                            "name": "Regular",
                            "ordinal": 1,
                            "pricing_type": "FIXED_PRICING",
                            "price_money": {
                                "amount": 3399,
                                "currency": "USD"
                            },
                            "location_overrides": [
                                {
                                "location_id": "LR94XVQK1SCP6",
                                "track_inventory": true
                                }
                            ],
                            "track_inventory": true,
                            "inventory_alert_type": "NONE",
                            "sellable": true,
                            "stockable": true,
                            "image_ids": [
                                "5RY5BNSXI5RCQEWISZNK3PFR"
                            ],
                            "channels": [
                                "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                            ]
                            }
                        },
                        {
                            "type": "ITEM_VARIATION",
                            "id": "GN5ZPBNVP2P5UXTLN54GAX6B",
                            "updated_at": "2024-02-14T00:37:21.941Z",
                            "created_at": "2024-02-14T00:29:24.79Z",
                            "version": 1707871041941,
                            "is_deleted": false,
                            "present_at_all_locations": false,
                            "present_at_location_ids": [
                            "LR94XVQK1SCP6"
                            ],
                            "item_variation_data": {
                            "item_id": "GI4AQIQ5LGBN4ZULGFY5DQ24",
                            "name": "Large Tufted Throw PIllow",
                            "ordinal": 2,
                            "pricing_type": "FIXED_PRICING",
                            "price_money": {
                                "amount": 4500,
                                "currency": "USD"
                            },
                            "location_overrides": [
                                {
                                "location_id": "LR94XVQK1SCP6",
                                "track_inventory": true
                                }
                            ],
                            "track_inventory": false,
                            "sellable": true,
                            "stockable": true,
                            "image_ids": [
                                "5RY5BNSXI5RCQEWISZNK3PFR"
                            ],
                            "channels": [
                                "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                            ]
                            }
                        }
                        ],
                        "product_type": "REGULAR",
                        "skip_modifier_screen": false,
                        "ecom_uri": "https://miltzn.square.site/product/primordial-sun-pillow/3",
                        "ecom_image_uris": [
                        "https://miltzn.square.site/uploads/1/4/8/7/148703844/s833352963451389956_p3_i1_w1000.png"
                        ],
                        "ecom_available": true,
                        "ecom_visibility": "VISIBLE",
                        "image_ids": [
                        "5RY5BNSXI5RCQEWISZNK3PFR"
                        ],
                        "categories": [
                        {
                            "id": "REOANBFLTGQF3MVSCFMVZKAZ",
                            "ordinal": -2251662374731776
                        }
                        ],
                        "pickup_fulfillment_preferences_id": "fprefs_127x00pk98e7f787ambpxsnz3",
                        "delivery_fulfillment_preferences_id": "fprefs_127x00pk8984gm3q5554ym9un",
                        "description_html": "<ul><li>One-sided - Acrylic / Cotton &amp; Polyester construction </li><li>Pillow insert included with purchase </li><li>Zipped back </li><li>Made in the USA with imported and domestic materials </li></ul><p><br/></p><p><strong>Contains latex</strong></p>",
                        "description_plaintext": "One-sided - Acrylic / Cotton & Polyester construction \nPillow insert included with purchase \nZipped back \nMade in the USA with imported and domestic materials \n\nContains latex",
                        "channels": [
                        "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                        ],
                        "shipping_fulfillment_preferences_id": "fprefs_127x00pk9rhhw99pdrs5ps09r",
                        "dine_in_fulfillment_preferences_id": "fprefs_127x00pk8qnb2pk1bcjgioqcf",
                        "is_archived": false,
                        "ecom_seo_data": {
                        "page_title": "Primordial Sun Square Pillow",
                        "page_description": "Acrylic 12\" x 12\" square throw pillow with primordial sun tufted design.",
                        "permalink": "primordial-sun-pillow"
                        },
                        "reporting_category": {
                        "id": "REOANBFLTGQF3MVSCFMVZKAZ",
                        "ordinal": -2251662374731776
                        }
                    }
                    },
                    {
                    "type": "ITEM",
                    "id": "2XUPTTYDMMOIWUESI2LSBJ6M",
                    "updated_at": "2024-02-14T00:37:24.627Z",
                    "created_at": "2024-02-14T00:31:01.557Z",
                    "version": 1707871044627,
                    "is_deleted": false,
                    "present_at_all_locations": false,
                    "present_at_location_ids": [
                        "LR94XVQK1SCP6"
                    ],
                    "item_data": {
                        "name": "Mushroom Mania - Tufted Square Pillow",
                        "description": "One-sided - Acrylic / Cotton & Polyester construction \nPillow insert included with purchase \nZipped back \nMade in the USA with imported and domestic materials \n\nContains latex",
                        "is_taxable": true,
                        "visibility": "PRIVATE",
                        "variations": [
                        {
                            "type": "ITEM_VARIATION",
                            "id": "2WF32K6ABQOORYEIWF5V6XFV",
                            "updated_at": "2024-02-14T00:31:03.069Z",
                            "created_at": "2024-02-14T00:31:01.557Z",
                            "version": 1707870663069,
                            "is_deleted": false,
                            "present_at_all_locations": false,
                            "present_at_location_ids": [
                            "LR94XVQK1SCP6"
                            ],
                            "item_variation_data": {
                            "item_id": "2XUPTTYDMMOIWUESI2LSBJ6M",
                            "name": "Regular",
                            "ordinal": 1,
                            "pricing_type": "FIXED_PRICING",
                            "price_money": {
                                "amount": 3399,
                                "currency": "USD"
                            },
                            "location_overrides": [
                                {
                                "location_id": "LR94XVQK1SCP6",
                                "track_inventory": true
                                }
                            ],
                            "track_inventory": true,
                            "inventory_alert_type": "NONE",
                            "sellable": true,
                            "stockable": true,
                            "image_ids": [
                                "2RQQUUF76XIBGEZDZUKAKDKT"
                            ],
                            "channels": [
                                "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                            ]
                            }
                        },
                        {
                            "type": "ITEM_VARIATION",
                            "id": "4MMFPDVOGIIOQJEEHU5OATVN",
                            "updated_at": "2024-02-14T00:31:30.423Z",
                            "created_at": "2024-02-14T00:31:01.557Z",
                            "version": 1707870690423,
                            "is_deleted": false,
                            "present_at_all_locations": false,
                            "present_at_location_ids": [
                            "LR94XVQK1SCP6"
                            ],
                            "item_variation_data": {
                            "item_id": "2XUPTTYDMMOIWUESI2LSBJ6M",
                            "name": "Large Tufted Throw PIllow",
                            "ordinal": 2,
                            "pricing_type": "FIXED_PRICING",
                            "price_money": {
                                "amount": 4500,
                                "currency": "USD"
                            },
                            "location_overrides": [
                                {
                                "location_id": "LR94XVQK1SCP6",
                                "track_inventory": true
                                }
                            ],
                            "track_inventory": false,
                            "sellable": true,
                            "stockable": true,
                            "image_ids": [
                                "2RQQUUF76XIBGEZDZUKAKDKT"
                            ],
                            "channels": [
                                "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                            ]
                            }
                        }
                        ],
                        "product_type": "REGULAR",
                        "skip_modifier_screen": false,
                        "ecom_uri": "https://miltzn.square.site/product/primordial-sun-pillow/4",
                        "ecom_image_uris": [
                        "https://miltzn.square.site/uploads/1/4/8/7/148703844/s833352963451389956_p4_i1_w1000.png"
                        ],
                        "ecom_available": true,
                        "ecom_visibility": "VISIBLE",
                        "image_ids": [
                        "2RQQUUF76XIBGEZDZUKAKDKT"
                        ],
                        "categories": [
                        {
                            "id": "REOANBFLTGQF3MVSCFMVZKAZ",
                            "ordinal": -2251593655255040
                        }
                        ],
                        "pickup_fulfillment_preferences_id": "fprefs_127x00ratfj86kin01uegkdy8",
                        "delivery_fulfillment_preferences_id": "fprefs_127x00rashouj4xm0zym597kw",
                        "description_html": "<ul><li>One-sided - Acrylic / Cotton &amp; Polyester construction </li><li>Pillow insert included with purchase </li><li>Zipped back </li><li>Made in the USA with imported and domestic materials </li></ul><p><br/></p><p><strong>Contains latex</strong></p>",
                        "description_plaintext": "One-sided - Acrylic / Cotton & Polyester construction \nPillow insert included with purchase \nZipped back \nMade in the USA with imported and domestic materials \n\nContains latex",
                        "channels": [
                        "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                        ],
                        "shipping_fulfillment_preferences_id": "fprefs_127x00ratve7hnrkshsiif734",
                        "dine_in_fulfillment_preferences_id": "fprefs_127x00rasyw3m9zu3wll1r2qo",
                        "is_archived": false,
                        "ecom_seo_data": {
                        "page_title": "Primordial Sun Square Pillow",
                        "page_description": "Acrylic 12\" x 12\" square throw pillow with primordial sun tufted design.",
                        "permalink": "primordial-sun-pillow"
                        },
                        "reporting_category": {
                        "id": "REOANBFLTGQF3MVSCFMVZKAZ",
                        "ordinal": -2251593655255040
                        }
                    }
                    },
                    {
                    "type": "ITEM",
                    "id": "7HILAIA3V7WP5SYGXZXDDTFG",
                    "updated_at": "2024-02-14T00:37:22.055Z",
                    "created_at": "2024-02-14T00:34:05.39Z",
                    "version": 1707871042055,
                    "is_deleted": false,
                    "present_at_all_locations": false,
                    "present_at_location_ids": [
                        "LR94XVQK1SCP6"
                    ],
                    "item_data": {
                        "name": "Still Life - Tufted Square Pillow",
                        "description": "One-sided - Acrylic / Cotton & Polyester construction \nPillow insert included with purchase \nZipped back \nMade in the USA with imported and domestic materials \n\nContains latex",
                        "is_taxable": true,
                        "visibility": "PRIVATE",
                        "variations": [
                        {
                            "type": "ITEM_VARIATION",
                            "id": "IZ2MEDBNXW6ERXXAZUUAXCV2",
                            "updated_at": "2024-02-14T00:34:06.649Z",
                            "created_at": "2024-02-14T00:34:05.39Z",
                            "version": 1707870846649,
                            "is_deleted": false,
                            "present_at_all_locations": false,
                            "present_at_location_ids": [
                            "LR94XVQK1SCP6"
                            ],
                            "item_variation_data": {
                            "item_id": "7HILAIA3V7WP5SYGXZXDDTFG",
                            "name": "Regular",
                            "ordinal": 1,
                            "pricing_type": "FIXED_PRICING",
                            "price_money": {
                                "amount": 3399,
                                "currency": "USD"
                            },
                            "location_overrides": [
                                {
                                "location_id": "LR94XVQK1SCP6",
                                "track_inventory": true
                                }
                            ],
                            "track_inventory": true,
                            "inventory_alert_type": "NONE",
                            "sellable": true,
                            "stockable": true,
                            "image_ids": [
                                "TDAQECABEFFE7DCH2YGR7CKS"
                            ],
                            "channels": [
                                "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                            ]
                            }
                        },
                        {
                            "type": "ITEM_VARIATION",
                            "id": "QUO3LRP6DRKGLGGYGQ4LBIRS",
                            "updated_at": "2024-02-14T00:37:22.055Z",
                            "created_at": "2024-02-14T00:34:05.39Z",
                            "version": 1707871042055,
                            "is_deleted": false,
                            "present_at_all_locations": false,
                            "present_at_location_ids": [
                            "LR94XVQK1SCP6"
                            ],
                            "item_variation_data": {
                            "item_id": "7HILAIA3V7WP5SYGXZXDDTFG",
                            "name": "Large Tufted Throw PIllow",
                            "ordinal": 2,
                            "pricing_type": "FIXED_PRICING",
                            "price_money": {
                                "amount": 4500,
                                "currency": "USD"
                            },
                            "location_overrides": [
                                {
                                "location_id": "LR94XVQK1SCP6",
                                "track_inventory": true
                                }
                            ],
                            "track_inventory": false,
                            "sellable": true,
                            "stockable": true,
                            "image_ids": [
                                "TDAQECABEFFE7DCH2YGR7CKS"
                            ],
                            "channels": [
                                "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                            ]
                            }
                        }
                        ],
                        "product_type": "REGULAR",
                        "skip_modifier_screen": false,
                        "ecom_uri": "https://miltzn.square.site/product/primordial-sun-pillow/5",
                        "ecom_image_uris": [
                        "https://miltzn.square.site/uploads/1/4/8/7/148703844/s833352963451389956_p5_i1_w1000.png"
                        ],
                        "ecom_available": true,
                        "ecom_visibility": "VISIBLE",
                        "image_ids": [
                        "TDAQECABEFFE7DCH2YGR7CKS"
                        ],
                        "categories": [
                        {
                            "id": "REOANBFLTGQF3MVSCFMVZKAZ",
                            "ordinal": -2251524935778304
                        }
                        ],
                        "pickup_fulfillment_preferences_id": "fprefs_127x00ul02pkuxu5s20i6vz4w",
                        "delivery_fulfillment_preferences_id": "fprefs_127x00ukz3s49uhmnxlp35rj4",
                        "description_html": "<ul><li>One-sided - Acrylic / Cotton &amp; Polyester construction </li><li>Pillow insert included with purchase </li><li>Zipped back </li><li>Made in the USA with imported and domestic materials </li></ul><p><br/></p><p><strong>Contains latex</strong></p>",
                        "description_plaintext": "One-sided - Acrylic / Cotton & Polyester construction \nPillow insert included with purchase \nZipped back \nMade in the USA with imported and domestic materials \n\nContains latex",
                        "channels": [
                        "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                        ],
                        "shipping_fulfillment_preferences_id": "fprefs_127x00ul0izseqbqxiqyyefts",
                        "dine_in_fulfillment_preferences_id": "fprefs_127x00ukzlrebu0fp6mqjfkps",
                        "is_archived": false,
                        "ecom_seo_data": {
                        "page_title": "Primordial Sun Square Pillow",
                        "page_description": "Acrylic 12\" x 12\" square throw pillow with primordial sun tufted design.",
                        "permalink": "primordial-sun-pillow"
                        },
                        "reporting_category": {
                        "id": "REOANBFLTGQF3MVSCFMVZKAZ",
                        "ordinal": -2251524935778304
                        }
                    }
                    },
                    {
                    "type": "ITEM",
                    "id": "5TY6RX2Y7AEH7OWTK4HMOY7X",
                    "updated_at": "2024-02-14T00:37:22.494Z",
                    "created_at": "2024-02-14T00:35:32.935Z",
                    "version": 1707871042494,
                    "is_deleted": false,
                    "present_at_all_locations": true,
                    "item_data": {
                        "name": "Primordial Sun - Tufted Square Pillow (1)",
                        "description": "One-sided - Acrylic / Cotton & Polyester construction \nPillow insert included with purchase \nZipped back \nMade in the USA with imported and domestic materials \n\nContains latex",
                        "is_taxable": true,
                        "visibility": "PRIVATE",
                        "variations": [
                        {
                            "type": "ITEM_VARIATION",
                            "id": "N4MOQFKZKVAIGITPTKMWYNWW",
                            "updated_at": "2024-02-14T00:35:33.312Z",
                            "created_at": "2024-02-14T00:35:32.935Z",
                            "version": 1707870933312,
                            "is_deleted": false,
                            "present_at_all_locations": true,
                            "item_variation_data": {
                            "item_id": "5TY6RX2Y7AEH7OWTK4HMOY7X",
                            "name": "Regular",
                            "ordinal": 1,
                            "pricing_type": "FIXED_PRICING",
                            "price_money": {
                                "amount": 3399,
                                "currency": "USD"
                            },
                            "location_overrides": [
                                {
                                "location_id": "LR94XVQK1SCP6",
                                "track_inventory": true,
                                "sold_out": true
                                }
                            ],
                            "track_inventory": true,
                            "inventory_alert_type": "NONE",
                            "sellable": true,
                            "stockable": true,
                            "image_ids": [
                                "OSYYH3XYSEEW5CKEYRMUCDQU"
                            ],
                            "channels": [
                                "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                            ]
                            }
                        },
                        {
                            "type": "ITEM_VARIATION",
                            "id": "Q4D5KQZHHHQ23VDGM7M4DRID",
                            "updated_at": "2024-02-14T00:37:22.494Z",
                            "created_at": "2024-02-14T00:35:32.935Z",
                            "version": 1707871042494,
                            "is_deleted": false,
                            "present_at_all_locations": true,
                            "item_variation_data": {
                            "item_id": "5TY6RX2Y7AEH7OWTK4HMOY7X",
                            "name": "Large Tufted Pillow",
                            "ordinal": 2,
                            "pricing_type": "FIXED_PRICING",
                            "price_money": {
                                "amount": 4500,
                                "currency": "USD"
                            },
                            "location_overrides": [
                                {
                                "location_id": "LR94XVQK1SCP6",
                                "track_inventory": true,
                                "sold_out": true
                                }
                            ],
                            "track_inventory": false,
                            "sellable": true,
                            "stockable": true,
                            "image_ids": [
                                "M5Z5ABO5WUPHK5O4AQCPQHSC"
                            ],
                            "channels": [
                                "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                            ]
                            }
                        }
                        ],
                        "product_type": "REGULAR",
                        "skip_modifier_screen": false,
                        "ecom_uri": "https://miltzn.square.site/product/primordial-sun-pillow/6",
                        "ecom_image_uris": [
                        "https://miltzn.square.site/uploads/1/4/8/7/148703844/s833352963451389956_p6_i1_w1000.png",
                        "https://miltzn.square.site/uploads/1/4/8/7/148703844/s833352963451389956_p6_i2_w1000.png"
                        ],
                        "ecom_available": true,
                        "ecom_visibility": "VISIBLE",
                        "image_ids": [
                        "OSYYH3XYSEEW5CKEYRMUCDQU"
                        ],
                        "categories": [
                        {
                            "id": "REOANBFLTGQF3MVSCFMVZKAZ",
                            "ordinal": -2251456216301568
                        }
                        ],
                        "pickup_fulfillment_preferences_id": "fprefs_127x00w55qak2guaof8cde3a6",
                        "delivery_fulfillment_preferences_id": "fprefs_127x00w54ydiinxghsdsqibku",
                        "description_html": "<ul><li>One-sided - Acrylic / Cotton &amp; Polyester construction </li><li>Pillow insert included with purchase </li><li>Zipped back </li><li>Made in the USA with imported and domestic materials </li></ul><p><br/></p><p><strong>Contains latex</strong></p>",
                        "description_plaintext": "One-sided - Acrylic / Cotton & Polyester construction \nPillow insert included with purchase \nZipped back \nMade in the USA with imported and domestic materials \n\nContains latex",
                        "channels": [
                        "CH_fH63uHJ05ZlzOPiSf4BEnovi3PCZqgwPk8vfYRlQuYC"
                        ],
                        "shipping_fulfillment_preferences_id": "fprefs_127x00w563jfc55z9wne7tyxq",
                        "dine_in_fulfillment_preferences_id": "fprefs_127x00w55cort845ymva0y4v2",
                        "is_archived": false,
                        "ecom_seo_data": {
                        "page_title": "Primordial Sun Square Pillow",
                        "page_description": "Acrylic 12\" x 12\" square throw pillow with primordial sun tufted design.",
                        "permalink": "primordial-sun-pillow"
                        },
                        "reporting_category": {
                        "id": "REOANBFLTGQF3MVSCFMVZKAZ",
                        "ordinal": -2251456216301568
                        }
                    }
                    }
                ]
            }
        ]
    }
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)