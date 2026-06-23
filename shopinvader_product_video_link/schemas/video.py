# Copyright 2023 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from extendable_pydantic import StrictExtendableBaseModel

from . import VideoProvider


class VideoVideo(StrictExtendableBaseModel):
    id: int
    name: str
    sequence: int | None = None
    identifier: str | None = None
    provider: VideoProvider
    thumbnail_url: str | None = None
    url: str | None = None

    @classmethod
    def from_video_video(cls, odoo_rec):
        return cls.model_construct(
            id=odoo_rec.id,
            name=odoo_rec.name,
            sequence=odoo_rec.sequence or None,
            identifier=odoo_rec.identifier or None,
            provider=VideoProvider.from_video_provider(odoo_rec.provider_id),
            thumbnail_url=odoo_rec.thumbnail_url or None,
            url=odoo_rec.url or None,
        )
