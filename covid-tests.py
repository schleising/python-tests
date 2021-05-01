from uk_covid19 import Cov19API
from uk_covid19.api_interface import StructureType

all_nations = [
    "areaType=utla",
]

cases_and_deaths: StructureType = {
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeathsByDeathDate": "newDeathsByDeathDate",
    "cumDeathsByDeathDate": "cumDeathsByDeathDate"
}

def uk_cumulative_cases():
    print(1)

    api = Cov19API(
        filters=all_nations,
        structure=cases_and_deaths,
        latest_by="newCasesByPublishDate"
    )

    print(2)

    df = api.get_dataframe()

    print(df)

uk_cumulative_cases()
