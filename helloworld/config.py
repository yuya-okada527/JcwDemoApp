# import os
# from pathlib import Path
#
# from dotenv import load_dotenv
#
# from helloworld.enums import Env
# from helloworld.logger import create_logger
#
# log = create_logger(__file__)
#
# ENV_FILE = os.path.join(
#     Path(__file__).resolve().parents[1],
#     ".env"
# )
#
# DEFAULT_FONT_PATH = os.path.join(
#     Path(__file__).resolve().parents[0],
#     "fonts",
#     "ttf",
#     "JapaneseLearners1.ttf"
# )
#
#
# class __Settings:
#
#     def __init__(self, path=ENV_FILE):
#         # 指定パスに.envファイルが存在する場合読み込む
#         if os.path.exists(path):
#             log.info(".env file exists loading from it")
#             load_dotenv(path, verbose=True)
#
#         # 環境変数をセット
#         self.env = Env.value_of(os.getenv("ENV", "local"))
#         self.s3_bucket_name = os.getenv("S3_BUCKET_NAME")
#         self.s3_access_key = os.getenv("S3_USER_ACCESS_KEY")
#         self.s3_secret_key = os.getenv("S3_USER_SECRET_KEY")
#
#
# settings = __Settings()
