import unittest
from argparse import ArgumentParser
from main import args_parser

from signers import Signer


class TestSigner(unittest.TestCase):
    def setUp(self) -> None:
        self.signer = Signer("A", "B")
        self.parser = args_parser()

    def test_parser(self):
        self.assertIsInstance(self.parser, ArgumentParser)

    def test_jwt_encode(self):
        payload = {
            "username": "name"
        }
        self.assertEqual(self.signer.jwt_encode(payload),
                         "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im5hbWUifQ."
                         "z2my_3vyHJgu5zLvInky8gUftLreI3Jz_YpLsFzLjvw")

    def test_jwt_decode(self):
        payload = {
            "username": "name"
        }
        self.assertEqual(self.signer.jwt_decode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im5hbWUifQ."
                         "z2my_3vyHJgu5zLvInky8gUftLreI3Jz_YpLsFzLjvw"), payload)

    def test_itsdangerous_encode(self):
        payload = {
            "username": "name"
        }
        self.assertEqual(self.signer.itsdangerous_encode(payload),
                         "eyJ1c2VybmFtZSI6Im5hbWUifQ.N_bLms0jCU_XH4H_Nm8irybixuM")

    def test_itsdangerous_decode(self):
        payload = {
            "username": "name"
        }
        self.assertEqual(self.signer.itsdangerous_decode("eyJ1c2VybmFtZSI6Im5hbWUifQ.N_bLms0jCU_XH4H_Nm8irybixuM"),
                         payload)
