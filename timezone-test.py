from datetime import datetime
import locale
from zoneinfo import ZoneInfo

brightZoneInfo = ZoneInfo('GB')
parisZoneInfo = ZoneInfo('Europe/Paris')

brightTime = datetime(2022, 10, 30, 0, 30, 0, 0, tzinfo=brightZoneInfo)
parisTime = datetime(2022, 10, 30, 2, 30, 0, 0, tzinfo=parisZoneInfo)

print(f'Brighton Time: {brightTime}')
print(f'Paris Time   : {parisTime}')

print(abs(parisTime - brightTime))

print(f'Time now in Brighton: {datetime.now(tz=brightZoneInfo)}')
print(f'Time now in Paris   : {datetime.now(tz=parisZoneInfo)}')

print(brightTime.tzinfo.utcoffset(brightTime) if brightTime.tzinfo is not None else '')
print(parisTime.tzinfo.utcoffset(parisTime) if parisTime.tzinfo is not None else '')

print(locale.getlocale())

print(datetime.now(ZoneInfo('UTC')))

pT = datetime.now(tz=ZoneInfo('Europe/Paris'))

print(pT)
print(pT.astimezone())
