import datetime
import io
import logging
import os
import tempfile
import uuid
import zipfile
from typing import *

import pandas as pd
import pytz
import requests

import TemporaryExposureKeyExport_pb2
import radar_covid_exceptions

_radar_covid_api_endpoint_base_url = "https://radarcovid.covid19.gob.es/"
_radar_covid_api_endpoint_exposed_tokens_url = _radar_covid_api_endpoint_base_url + "dp3t/v1/gaen/exposed/"

_unix_epoch_datetime = datetime.datetime(year=1970, month=1, day=1, tzinfo=pytz.utc)


def download_radar_covid_exposure_keys(date: datetime.datetime) -> pd.DataFrame:
    sample_datetime = datetime.datetime(
        year=date.year,
        month=date.month,
        day=date.day,
        tzinfo=pytz.utc)
    sample_date_string = sample_datetime.strftime("%Y-%m-%d")

    temporary_directory = tempfile.gettempdir()
    temporary_directory_uuid = str(uuid.uuid4()).upper()
    temporary_directory = os.path.join(temporary_directory, temporary_directory_uuid)
    sample_date_temporary_directory = os.path.join(temporary_directory, sample_date_string)

    date_exposed_tokens_url = \
        _radar_covid_api_endpoint_exposed_tokens_url + str(
            int((sample_datetime - _unix_epoch_datetime).total_seconds())) + "000"
    logging.info(
        f"Downloading exposed tokens for day '{sample_date_string}' from '{date_exposed_tokens_url}'...")
    date_exposed_tokens_response = requests.get(url=date_exposed_tokens_url)
    date_exposed_tokens_response.raise_for_status()
    date_exposed_tokens_bytes = date_exposed_tokens_response.content

    if len(date_exposed_tokens_bytes) == 0:
        raise radar_covid_exceptions.NoDataFoundForDateException(
            f"No exposed tokens found for day '{sample_date_string}'.")

    date_temporary_exposure_keys = []
    with io.BytesIO(date_exposed_tokens_bytes) as f:
        with zipfile.ZipFile(f, "r") as z:
            z.extractall(sample_date_temporary_directory)

            date_exposed_tokens_file = \
                os.path.join(sample_date_temporary_directory, "export.bin")
            with open(date_exposed_tokens_file, "rb") as ekf:
                g = TemporaryExposureKeyExport_pb2.TemporaryExposureKeyExport()
                ekf.read(16)
                g.ParseFromString(ekf.read())

            key_file_details = []
            key_file_details.append(f"Exposure Key File 'RadarCOVID-{sample_date_string}'")
            key_file_details.append(f"Timestamp Range: {str(g.start_timestamp)} -> {str(g.end_timestamp)}")
            key_file_details.append(f"Region: {str(g.region).upper()}")

            key_file_details.append("")
            key_file_details.append("Signature Details:")
            key_file_details.append(
                f"Verification Key Version: {str(g.signature_infos[0].verification_key_version).upper()}")
            key_file_details.append(f"Verification Key ID: {str(g.signature_infos[0].verification_key_id).upper()}")
            key_file_details.append(f"Signature Algorithm: {str(g.signature_infos[0].signature_algorithm).upper()}")

            key_file_details.append("")
            key_file_details.append(f"Exposure Keys ({len(g.keys)}):")
            for key in g.keys:
                key_uuid = uuid.UUID(bytes=key.key_data)
                date_temporary_exposure_keys.append(dict(
                    sample_datetime=sample_datetime,
                    sample_date_string=sample_date_string,
                    source_url=date_exposed_tokens_url,
                    region=str(g.region).upper(),
                    verification_key_version=str(g.signature_infos[0].verification_key_version).upper(),
                    verification_key_id=str(g.signature_infos[0].verification_key_id).upper(),
                    signature_algorithm=str(g.signature_infos[0].signature_algorithm).upper(),
                    key_data=key_uuid,
                    rolling_start_interval_number=key.rolling_start_interval_number,
                    rolling_period=key.rolling_period,
                    transmission_risk_level=key.transmission_risk_level,
                ))
                key_file_details.append(
                    f"{key_uuid} (rolling start interval number: {key.rolling_start_interval_number}, "
                    f"rolling period: {key.rolling_period}, "
                    f"transmission risk level: {key.transmission_risk_level})")

            key_file_details = "\n".join(key_file_details)
            logging.info(key_file_details)

    return pd.DataFrame.from_records(date_temporary_exposure_keys)


def download_last_radar_covid_exposure_keys(days=None) -> Any:
    if days is None:
        days = 14

    exposure_keys_df = pd.DataFrame()
    now_datetime = datetime.datetime.utcnow()

    for i in range(days):
        try:
            sample_datetime = now_datetime - datetime.timedelta(days=i)
            date_exposure_keys_df = download_radar_covid_exposure_keys(date=sample_datetime)
            exposure_keys_df = exposure_keys_df.append(date_exposure_keys_df)
        except radar_covid_exceptions.NoDataFoundForDateException as e:
            logging.warning(repr(e))
        except Exception as e:
            logging.warning(repr(e), exc_info=True)

    return exposure_keys_df
