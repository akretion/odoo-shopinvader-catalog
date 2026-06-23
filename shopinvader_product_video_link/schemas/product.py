# Copyright 2023 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.addons.shopinvader_product.schemas import ProductProduct as BaseProductProduct

from . import VideoVideo


class ProductProduct(BaseProductProduct, extends=True):
    videos: list[VideoVideo] = []

    @classmethod
    def from_product_product(cls, odoo_rec):
        obj = super().from_product_product(odoo_rec)
        obj.videos = [
            VideoVideo.from_video_video(video) for video in odoo_rec.video_ids
        ]
        return obj
