import importlib

import pytest


def _load(dotted_path):
    return importlib.import_module(dotted_path)


@pytest.fixture(params=["v1", "v2"], ids=["pydantic-v1", "pydantic-v2"])
def pydantic_version(request):
    """The pydantic version string — used to derive all other fixtures."""
    return request.param


@pytest.fixture
def q_module(pydantic_version):
    """The _model module for the current pydantic version."""
    if pydantic_version == "v1":
        return _load("opensemantic.characteristics.quantitative.v1._model")
    return _load("opensemantic.characteristics.quantitative._model")


@pytest.fixture
def static_module(pydantic_version):
    """The _static module for the current pydantic version."""
    if pydantic_version == "v1":
        return _load("opensemantic.characteristics.quantitative.v1._static")
    return _load("opensemantic.characteristics.quantitative._static")


@pytest.fixture
def package_module(pydantic_version):
    """The top-level package for the current pydantic version."""
    if pydantic_version == "v1":
        return _load("opensemantic.characteristics.quantitative.v1")
    return _load("opensemantic.characteristics.quantitative")


@pytest.fixture
def osw_base_model(pydantic_version):
    """OswBaseModel for the current pydantic version."""
    if pydantic_version == "v1":
        return _load("opensemantic.v1").OswBaseModel
    return _load("opensemantic").OswBaseModel
