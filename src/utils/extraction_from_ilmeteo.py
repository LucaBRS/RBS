import time

import pandas as pd
import requests
import io

from utils.parsing_table import ParsingTable

if __name__ == '__main__':
    months = [
        "Gennaio",
        "Febbraio",
        "Marzo",
        "Aprile",
        "Maggio",
        "Giugno",
        "Luglio",
        "Agosto",
        "Settembre",
        "Ottobre",
        "Novembre",
        "Dicembre"
    ]
    years = ['2020', '2021', '2022','2023' ]
    # Set headers to simulate a web browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    df_concat = pd.DataFrame()
    for year in years:
        for month in months:
            if year == '2023' and month in['Settembre' , 'Ottobre', 'Novembre' , 'Dicembre']:
                continue
            else:
                # URL of the CSV file
                csv_url = f"https://www.ilmeteo.it/portale/archivio-meteo/Roma/{year}/{month}?format=csv"

                # Send an HTTP GET request to the URL with headers

                response = requests.get(csv_url, headers=headers)
                time.sleep(1.5)  # Pause the script for 1.5 seconds

                # Read the CSV file directly from the URL into a pandas DataFrame
                if response.status_code == 200 :
                    print(f"CSV file downloaded YEAR:{year} MONTH:{month}")
                    # Get the content of the response
                    csv_content = response.content

                    # Save the content to a local CSV file
                    csv_month_test = pd.read_csv(io.BytesIO(csv_content), sep=";")
                    csv_month_test = csv_month_test.drop(columns=['TMIN °C', 'TMAX °C',
                                                                  'PUNTORUGIADA °C', 'VISIBILITA km', 'VENTOMEDIA km/h',
                                                                  'VENTOMAX km/h', 'RAFFICA km/h',
                                                                  'PIOGGIA mm', 'FENOMENI'])


                    df_concat = pd.concat([df_concat, csv_month_test], axis=0)
                else:
                    print(f"Failed to download the CSV file. Status code: {response.status_code}")

                df_concat.to_csv('../../resources/meteo.csv', sep=',')

    df_concat.to_csv('../../resources/meteo.csv', sep=',')
