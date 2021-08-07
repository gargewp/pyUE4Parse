from typing import Tuple, Union, Optional

from UE4Parse.BinaryReader import BinaryStream
from UE4Parse.Assets.Exports.UObjects import UObject
from UE4Parse.Versions.EUEVersion import EUEVersion
from UE4Parse.Assets.Objects.FObjectExport import FObjectExport
from UE4Parse.Assets.Objects.FObjectImport import FObjectImport
from UE4Parse.Assets.Exports.ExportRegistry import register_export
from UE4Parse.Assets.Objects.URL import FURL


@register_export
class ULevel(UObject):
    URL: FURL
    Actors: Tuple[Optional[Union[FObjectExport, FObjectImport]]]
    Model: Tuple[Optional[Union[FObjectExport, FObjectImport]]]
    ModelComponents: Tuple[Optional[Union[FObjectExport, FObjectImport]]]
    LevelScriptActor: Optional[Union[FObjectExport, FObjectImport]]
    NavListStart: Optional[Union[FObjectExport, FObjectImport]]
    NavListEnd: Optional[Union[FObjectExport, FObjectImport]]

    def __init__(self, reader: BinaryStream):
        super().__init__(reader)

    def deserialize(self, validpos):
        super().deserialize(validpos)
        reader = self.reader
        if reader.game == EUEVersion.GAME_VALORANT: return # prevent crash

        self.Actors = reader.readTArray(reader.readObject)
        self.URL = FURL(reader)
        self.Model = reader.readObject()
        self.ModelComponents = reader.readTArray(reader.readObject)
        self.LevelScriptActor = reader.readObject()
        self.NavListStart = reader.readObject()
        self.NavListEnd = reader.readObject()
        # rest later
