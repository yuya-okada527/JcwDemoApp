#!flask/bin/python
from flask import (
    Flask,
    request,
    render_template,
    make_response
)

from helloworld.domain.service import get_workbooks, get_workbook
from helloworld.domain.pdf import PdfWriter
from helloworld.flaskrun import flaskrun


application = Flask(__name__)


@application.route("/")
def index():
    return render_template("index.html", workbooks=get_workbooks())


@application.route("/create")
def create():

    # リクエストパラメータを取得
    text = request.args.get("text")

    # サンプルのPDFファイルを作成する
    pdf_writer = PdfWriter(text)
    pdf_file = pdf_writer.write()

    # レスポンスの作成
    response = make_response(pdf_file)
    response.headers['Content-Disposition'] = "attachment; filename=sample.pdf"
    response.mimetype = 'application/pdf'

    return response


@application.route("/download")
def download():

    # クエリパラメータからキーを取得
    key = request.args.get("key")

    # S3から教材を取得
    workbook = get_workbook(key)

    # レスポンスを作成する
    response = make_response(workbook)
    response.headers['Content-Disposition'] = "attachment; filename=" + "workbook.pdf"  # TODO ファイル名 オリジナルのキー名を使うと文字コード系のエラーがでる
    response.mimetype = 'application/pdf'
    return response


if __name__ == '__main__':
    flaskrun(application)
