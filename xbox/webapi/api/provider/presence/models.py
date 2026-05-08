from enum import Enum
from typing import List, Optional

from pydantic import RootModel

from xbox.webapi.common.models import CamelCaseModel


class PresenceLevel(str, Enum):
    USER = "user"
    DEVICE = "device"
    TITLE = "title"
    ALL = "all"


class PresenceState(str, Enum):
    ACTIVE = "Active"
    CLOAKED = "Cloaked"


class LastSeen(CamelCaseModel):
    device_type: Optional[str] = None
    title_id: Optional[str] = None
    title_name: Optional[str] = None
    timestamp: Optional[str] = None


class ActivityRecord(CamelCaseModel):
    richPresence: Optional[str] = None
    media: Optional[str] = None


class TitleRecord(CamelCaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    activity: Optional[ActivityRecord] = None
    lastModified: Optional[str] = None
    placement: Optional[str] = None
    state: Optional[str] = None


class DeviceRecord(CamelCaseModel):
    titles: Optional[List[TitleRecord]] = None
    type: Optional[str] = None


class PresenceItem(CamelCaseModel):
    xuid: str
    state: str
    last_seen: Optional[LastSeen] = None
    devices: Optional[List[DeviceRecord]] = None


class PresenceBatchResponse(RootModel[List[PresenceItem]], CamelCaseModel):
    root: List[PresenceItem]
