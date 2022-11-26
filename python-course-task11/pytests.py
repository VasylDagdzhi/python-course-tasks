import pytest
from signers import Signer
from argparse import ArgumentParser
from main import args_parser


@pytest.fixture
def setup_signer():
    signer = Signer("A", "B")
    signer.paser = args_parser()
    return signer


@pytest.fixture
def setup_parser():
    paser = args_parser()
    return paser


def test_signer(setup_signer):
    assert isinstance(setup_signer, Signer), "signer is not an instance of Signer"


def test_parser(setup_parser):
    assert isinstance(setup_parser, ArgumentParser), "parser is not an instance of ArgumentParser"


def test_jwt_encode(setup_signer):
    payload = {
        "username": "name"
    }
    assert setup_signer.jwt_encode(payload) == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im5hbWUifQ." \
                                               "z2my_3vyHJgu5zLvInky8gUftLreI3Jz_YpLsFzLjvw", "jwt encode failed"


def test_jwt_decode(setup_signer):
    payload = {
        "username": "name"
    }
    assert setup_signer.jwt_decode(
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im5hbWUifQ.z2my_3vyHJgu5zLvInky"
        "8gUftLreI3Jz_YpLsFzLjvw") == payload, "jwt decode failed"


def test_itsdangerous_encode(setup_signer):
    payload = {
        "username": "name"
    }
    assert setup_signer.itsdangerous_encode(payload) == "eyJ1c2VybmFtZSI6Im5hbWUifQ.N_bLms0jCU_XH4H_Nm8irybixuM", \
        "itsdangerous encode failed"


def test_itsdangerous_decode(setup_signer):
    payload = {
        "username": "name"
    }
    assert setup_signer.itsdangerous_decode(
        "eyJ1c2VybmFtZSI6Im5hbWUifQ.N_bLms0jCU_XH4H_Nm8irybixuM") == payload, "itsdangerous decode failed"
