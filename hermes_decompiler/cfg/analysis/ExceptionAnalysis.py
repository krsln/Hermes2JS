from __future__ import annotations

from hermes_decompiler.cfg.ExceptionRegion import ExceptionRegion


class ExceptionAnalysis:
    """
    Extract exception regions from Hermes metadata.
    """

    @classmethod
    def build(
            cls,
            metadata: dict,
    ) -> list[ExceptionRegion]:
        handlers = metadata.get(
            "exception_handlers",
            [],
        )

        return [
            ExceptionRegion(
                start=h["start"],
                end=h["end"],
                handler=h["target"],
            )
            for h in handlers
        ]
