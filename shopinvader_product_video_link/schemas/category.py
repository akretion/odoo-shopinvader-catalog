# Copyright 2023 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.addons.shopinvader_product.schemas import (
    ProductCategory as BaseProductCategory,
)

from . import VideoVideo


class ProductCategory(BaseProductCategory, extends=True):
    videos: list[VideoVideo] = []

    @classmethod
    def from_product_category(cls, odoo_rec):
        obj = super().from_product_category(odoo_rec)
        obj.videos = [
            VideoVideo.from_video_video(video) for video in odoo_rec.video_ids
        ]
        return obj
