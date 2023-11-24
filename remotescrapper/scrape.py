import requests
import xlwt
from xlwt import Workbook
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

BASE_URL = 'https://remoteok.com/api/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
REQUEST_HEADER = {
    'user-agent': USER_AGENT,
    'Accept-Language': 'en-US, en;q=0.5',
}


def get_job_postings():
    res = requests.get(url=BASE_URL, headers=REQUEST_HEADER)
    return res.json()


def output_jobs_to_xls(data):
    wb = Workbook()
    job_sheet = wb.add_sheet('Jobs')
    headers = list(data[0].keys())

    for i, header in enumerate(headers):
        job_sheet.write(0, i, header)

    for i, job in enumerate(data):
        values = list(job.values())
        for x, value in enumerate(values):
            job_sheet.write(i + 1, x, value)

    wb.save('remote_job.xls')


if __name__ == '__main__':
    job_data = get_job_postings()[1:]
    print(job_data)
    output_jobs_to_xls(job_data)
