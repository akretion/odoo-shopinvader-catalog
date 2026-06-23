# Copyright 2023 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from extendable_pydantic import StrictExtendableBaseModel


class VideoProvider(StrictExtendableBaseModel):
    code: str

    @classmethod
    def from_video_provider(cls, odoo_rec):
        return cls.model_construct(
            code=odoo_rec.code,
        )
